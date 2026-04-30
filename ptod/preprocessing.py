import os
import fitz
from PIL import Image, ImageEnhance
import numpy as np
from .utils import collect_files
import cv2

def pdf_to_img(path, out, **kwargs):
    doc = fitz.open(path)

    if os.path.isdir(out) == False:
        os.makedirs(out, exist_ok=True)

    for i in range(doc.page_count):
        page = doc[i] 
        pix = page.get_pixmap(dpi = kwargs.get("dpi", 300))

        # Define output image path
        filename = os.path.splitext(os.path.basename(path))[0]
        image_path = os.path.join(out, f"{filename}_page_{i + 1}.png")

        # Save image
        pix.save(image_path)

def preprocess_images(pdf_file, OUTPUT_FOLDER, **kwargs):
    source_folder = os.path.join(OUTPUT_FOLDER, "images", os.path.splitext(os.path.basename(pdf_file))[0], "raw-png")
    source_files = collect_files(source_folder, ["png"])
    for source_file in source_files:
        image_loaded = load_image(
            source_file, col = kwargs.get("color_mode", "L"), 
            boost_contrast = kwargs.get("boost_contrast", False), 
            contrast_amount = kwargs.get("contrast_amount", 2.0), 
            max_dims = kwargs.get("max_dims", 3000))
        
        out_path = os.path.join(OUTPUT_FOLDER, "images", os.path.splitext(os.path.basename(pdf_file))[0], "preprocessed", f"{os.path.splitext(os.path.basename(source_file))[0]}.jpg")
        preprocessed_folder = os.path.join(OUTPUT_FOLDER, "images", os.path.splitext(os.path.basename(pdf_file))[0], "preprocessed")
        preprocessed_small_folder = os.path.join(OUTPUT_FOLDER, "images", os.path.splitext(os.path.basename(pdf_file))[0], "preprocessed-small")

        if os.path.isdir(preprocessed_folder) == False:
            os.makedirs(preprocessed_folder, exist_ok = True)
        if os.path.isdir(preprocessed_small_folder) == False:
            os.makedirs(preprocessed_small_folder, exist_ok = True)
        
        save_image(out_path, image_loaded)

        compress_image_to_size(out_path, preprocessed_small_folder, kwargs.get("max_image_size", 5))

def get_image_info(file_path):
    with Image.open(file_path) as img:
        width, height = img.size
        exif_data = img._getexif()
        return {
            "width": width,
            "height": height
            #"exif_data": exif_data,
            #"color_mode" : img.mode,
            #"bit_depth" : img.bits
        }

def load_image(path, **kwargs):
    """
    kwargs:
    - col ("RGB"= color, "L" = greyscale)
    - boost_contrast = bool
    - contrast_amount = float
    - max_dims = int
    """
    image_info = get_image_info(path)

    with Image.open(path) as img:
        img = img.convert(kwargs.get("col", "RGB"))
        new_w, new_h = resize_with_aspect_ratio(image_info["width"], image_info["height"], kwargs.get("max_dims", 1000), kwargs.get("max_dims", 1000))
        img = img.resize((new_w, new_h))
        
        if kwargs.get("boost_contrast", False):
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(kwargs.get("contrast_amount", 2.0))  
        
        image = np.array(img)

    return image

def resize_with_aspect_ratio(orig_width, orig_height, max_width, max_height):
    # Calculate the scale ratios
    width_ratio = max_width / orig_width
    height_ratio = max_height / orig_height

    # Choose the smaller ratio to ensure both dimensions fit
    scale = min(width_ratio, height_ratio)

    # Compute new dimensions
    new_width = int(orig_width * scale)
    new_height = int(orig_height * scale)

    return new_width, new_height

def save_image(out_path, image, **kwargs):
    if kwargs.get("is_rgb", True):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(out_path, image)

def compress_image_to_size(input_path, output_folder, max_size_mb = 5):
    max_size_bytes = max_size_mb * 1024 * 1024

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    filename_wo_ext = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_folder, f"{filename_wo_ext}.jpg")  # Always save as JPG

    with Image.open(input_path) as img:
        img = img.convert("RGB")
        scale_factor = 1.0
        quality = 85

        while True:
            width, height = img.size
            new_dimensions = (int(width * scale_factor), int(height * scale_factor))

            try:
                resized_img = img.resize(new_dimensions, resample=Image.Resampling.LANCZOS)
            except AttributeError:
                resized_img = img.resize(new_dimensions, resample=Image.LANCZOS)

            resized_img.save(output_path, format="JPEG", quality=quality)

            if os.path.getsize(output_path) <= max_size_bytes or scale_factor < 0.1:
                break

            scale_factor *= 0.9
            quality = max(quality - 5, 50)