#!/usr/bin/env python3
"""Convert prepared photo to ASCII art and generate SVG."""

from PIL import Image

def image_to_ascii(image_path, width=100, chars="@%#*+=-:. "):
    """Convert image to ASCII art."""
    img = Image.open(image_path).convert("L")
    img = img.resize((width, int(width * 0.55)))  # Adjust for terminal aspect ratio

    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += chars[min(len(chars) - 1, pixel // 26)]  # Map pixel brightness to ASCII char

    # Format into lines
    width_chars = width
    ascii_lines = [ascii_str[i:i+width_chars] for i in range(0, len(ascii_str), width_chars)]
    return ascii_lines

def ascii_to_svg(ascii_lines, output_path="ascii-portrait.svg", font_size=8, char_width=5):
    """Convert ASCII lines to SVG."""
    height = len(ascii_lines) * font_size
    width = max(len(line) for line in ascii_lines) * char_width

    svg_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">')
    svg_lines.append('<style>')
    svg_lines.append('  text { font-family: "Courier New", monospace; font-size: 8px; font-weight: bold; fill: #0d1117; }')
    svg_lines.append('  svg { background: #ffffff; }')
    svg_lines.append('</style>')

    y = 12
    for line in ascii_lines:
        svg_lines.append(f'  <text x="2" y="{y}">{line}</text>')
        y += font_size

    svg_lines.append('</svg>')

    with open(output_path, 'w') as f:
        f.write('\n'.join(svg_lines))

    print(f"✓ ASCII portrait SVG generated: {output_path}")

if __name__ == "__main__":
    ascii_lines = image_to_ascii("photo.jpg", width=92)
    ascii_to_svg(ascii_lines, "avi-ascii.svg")
