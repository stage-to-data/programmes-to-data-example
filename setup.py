from setuptools import find_packages, setup

long_description = """
Programmes to data: a pipeline turning theatre programme PDFs into structured
Linked Art data, via VLM transcription. Part of the ERC-funded STAGE project.
"""

# Stage 1 (PDF to preprocessed images) only. Kept deliberately light so that the
# package installs anywhere, including machines without a GPU.
required = [
    "pymupdf",
    "pillow",
    "numpy",
    "opencv-python",
]

extras = {
    # Stage 2: VLM transcription.
    "transcription": [
        "llmwrap @ git+https://github.com/stage-to-data/llm-wrap.git",
    ],
    # Stage 3: Linked Art extraction. Needs a CUDA GPU.
    "extraction": [
        "vllm",
    ],
    # Prompt/model evaluation against the ground truth corpus (see pdf2md/).
    "evaluation": [
        "python-Levenshtein>=0.25",
        "jiwer>=3.0",
        "spacy>=3.7",
        "matplotlib>=3.7",
    ],
}
extras["all"] = sorted({dep for deps in extras.values() for dep in deps})

setup(
    name="ptod",
    version="0.1.0",
    description="Theatre programme PDFs to structured Linked Art data.",
    long_description=long_description,
    author="Jacob Hart",
    author_email="jacob.dchart@gmail.com",
    url="https://github.com/stage-to-data/programmes-to-data-example",
    install_requires=required,
    extras_require=extras,
    packages=find_packages(),
    package_data={"ptod": ["*.md"]},
    python_requires=">=3.9",
)
