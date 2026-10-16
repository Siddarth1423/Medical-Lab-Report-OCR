from pathlib import Path
import pytesseract
from PIL import Image


def configure_tesseract():
    """Find Tesseract in common Windows locations or through PATH."""
    candidates = [
        Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
        Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
    ]

    for candidate in candidates:
        if candidate.exists():
            pytesseract.pytesseract.tesseract_cmd = str(candidate)
            return

    # If Tesseract is on PATH, pytesseract will find it automatically.


def recognize_text(image):
    """Recognize text in a processed image using Tesseract OCR."""
    configure_tesseract()
    try:
        return pytesseract.image_to_string(
            Image.fromarray(image),
            config="--psm 6",
        ).strip()
    except pytesseract.TesseractNotFoundError as exc:
        raise RuntimeError(
            "Tesseract OCR was not found. Install it from "
            "https://github.com/UB-Mannheim/tesseract/wiki and ensure it is "
            "installed at C:\\Program Files\\Tesseract-OCR or added to PATH."
        ) from exc
