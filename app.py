import argparse
from pathlib import Path

from src.preprocessing import preprocess_image
from src.patch_processing import split_into_patches
from src.ocr_engine import recognize_text


def extract_report_text(image_path: Path) -> str:
    processed_image = preprocess_image(image_path)
    patches = split_into_patches(processed_image, patch_height=1000, overlap=100)
    results = []

    for index, patch in enumerate(patches, start=1):
        print(f"Processing section {index}/{len(patches)}...")
        text = recognize_text(patch)
        if text:
            results.append(text)

    return "\n\n".join(results)


def main():
    parser = argparse.ArgumentParser(
        description="Medical Laboratory Report Text Detection and Recognition"
    )
    parser.add_argument("image", help="Path to the report image")
    parser.add_argument(
        "--output",
        default="outputs/extracted_text.txt",
        help="Output text file (default: outputs/extracted_text.txt)",
    )
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.is_file():
        parser.error(f"Image file does not exist: {image_path}")

    try:
        text = extract_report_text(image_path)
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")

        print("\n" + "=" * 50)
        print("EXTRACTED REPORT TEXT")
        print("=" * 50)
        print(text or "(No text detected)")
        print(f"\nResults saved to: {output_path.resolve()}")
    except (FileNotFoundError, RuntimeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
