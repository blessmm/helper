Image Tile Splitter

Splits images horizontally into square tiles based on image height.
If the last tile is smaller, it gets padded with transparency.
All tiles accumulate in the output folder across multiple runs.

Usage:
    python split_image.py image1.png [image2.png] [image3.png] ...

Tiles are saved to a "tiles" folder in the current directory.
