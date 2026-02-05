from PIL import Image
import os
import sys


def split_image(image_path, output_dir="tiles"):
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    tile_size = height

    os.makedirs(output_dir, exist_ok=True)

    existing = [f for f in os.listdir(output_dir) if f.startswith("tile_") and f.endswith(".png")]
    if existing:
        start = max(int(f.split("_")[1].split(".")[0]) for f in existing)
    else:
        start = 0

    num_full = width // tile_size
    remainder = width % tile_size
    total = num_full + (1 if remainder > 0 else 0)

    for i in range(total):
        left = i * tile_size
        right = min(left + tile_size, width)
        crop = img.crop((left, 0, right, height))

        if crop.width < tile_size:
            tile = Image.new("RGBA", (tile_size, tile_size), (0, 0, 0, 0))
            tile.paste(crop, (0, 0))
        else:
            tile = crop

        num = start + i + 1
        tile_path = os.path.join(output_dir, f"tile_{num}.png")
        tile.save(tile_path)
        print(f"tile_{num}: {crop.width}x{crop.height}")

    print("Done")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_image.py image1 image2 image3 ...")
        sys.exit(1)

    for path in sys.argv[1:]:
        print(f"\n{os.path.basename(path)}")
        split_image(path)
