from pathlib import Path
import cv2


def preprocess_image(image_path):
    """Load an image and improve contrast for OCR."""
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(
            f"Unable to load image: {image_path}. "
            "Make sure it is a valid PNG/JPG image."
        )

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised = cv2.GaussianBlur(gray, (3, 3), 0)
    processed = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11,
    )
    return processed
