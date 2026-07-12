#!/usr/bin/env python3
"""Prepare photo for ASCII conversion: resize and optimize contrast."""

import sys
from PIL import Image, ImageEnhance

def prep_photo(input_path, output_path="photo.jpg", width=100, height=100):
    """Resize and enhance contrast for better ASCII art."""
    img = Image.open(input_path).convert("L")  # Convert to grayscale
    img = img.resize((width, height), Image.Resampling.LANCZOS)

    # Enhance contrast for better ASCII differentiation
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

    img.save(output_path)
    print(f"✓ Photo prepared: {output_path}")

if __name__ == "__main__":
    input_photo = sys.argv[1] if len(sys.argv) > 1 else "input.jpg"
    prep_photo(input_photo, "photo.jpg", width=100, height=60)
