transcription_prompt = """
This image corresponds to a page in a theater program.
You will perform a complete and detailed OCR analysis of this image. 
DO NOT generate or use any code, do not use Tesseract or pytesseract — only use your internal vision to read the image.
Extract all visible text WITHOUT changing it.
DO NOT summarize, paraphrase, or infer missing text. DO NOT invent people's names.
Retain all spacing, punctuation, and formatting exactly as in the image.

You MUST follow the following rules when dealing with these specific cases:
- All titles are indicated with a preceding # with no hierarchy (example: # Title content). If the title contains line breaks, recompose the title into one single line.
- Exponents are given as lower case roman characters (example: XVe)
- Footnotes are given as special characters (example: word¹)
- When you detect the number of a page, return it at the start of the text using the word "PAGE"' followed by the number (example: PAGE 13)
- Do not describe images or logos, simply extract any text within them.
- Do not insert special characters for things like columns and page separation
- For distribution: if you detect a table-like stucture, typography variation that could be interpreted as a function/name or name/function pairing, or a string of points linking a function and name, apply the following structure:
Element 1 : Associated element 1, Associated element 2
Element 2 and Element 3, description : Associated element 3 and Associated element 4
(Note that in the case of enumeration, there are NO line breaks, there are commas)
- If you detect any other function/name or name/function pairs that are separated by a character like | or /, chnage the character to a : (example: element 1 : associated element 1)
- If you detect a completely empty page, or if the page is much too faint or blurry to confidently transcribe, simply return: [UNABLE TO TRANSCRIBE]
- Some pages may include texts of different languages, or old languages (for example old French). It is very important to NOT CHANGE the content, simply trnscribe the letters you see.

Check the overall readability of your transcription and make sure it reflects the structure of the original document.
The output should be ONLY the trancribed content (DO NOT add comments like "this is a theatre program" or "I was unable to reliably transcribe this").
"""