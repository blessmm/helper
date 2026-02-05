# Разделитеть фото кубами

Скрипт для разделения изображений на квадратные тайлы по горизонтали.
Подходит для создания кастомных эмоджи в Telegram.

## Установка

```bash
pip install Pillow
```

## Использование

Одна картинка:
```bash
python split_image.py image.png
```

Несколько картинок:
```bash
python split_image.py image1.png image2.png image3.png
```

## Как это работает

Скрипт берёт высоту картинки как размер квадрата и нарезает по горизонтали.

Например, фото 500x100:
```
┌──────────────────────────────────────────────────┐
│                   500 x 100                      │
└──────────────────────────────────────────────────┘
                        ↓
┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
│ 1  │ │ 2  │ │ 3  │ │ 4  │ │ 5  │ 
└────┘ └────┘ └────┘ └────┘ └────┘
```

Если ширина не делится ровно (например 530x100) — последний тайл дополняется прозрачным фоном до квадрата.

Результат сохраняется в папку `tiles/` в формате PNG с прозрачностью.


## Пример вывода

```
image.png
tile_1: 100x100
tile_2: 100x100
tile_3: 100x100
tile_4: 100x100
tile_5: 30x100
Done
```




# Image Tile Splitter

A script for splitting images into square tiles horizontally.
Useful for creating custom emoji in Telegram.

## Installation

```bash
pip install Pillow
```

## Usage

Single image:
```bash
python split_image.py image.png
```

Multiple images:
```bash
python split_image.py image1.png image2.png image3.png
```

## How it works

The script uses the image height as the tile size and slices horizontally.

For example, a 500x100 image:
```
┌──────────────────────────────────────────────────┐
│                   500 x 100                      │
└──────────────────────────────────────────────────┘
                        ↓
┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
│ 1  │ │ 2  │ │ 3  │ │ 4  │ │ 5  │  
└────┘ └────┘ └────┘ └────┘ └────┘
```

If the width doesn't divide evenly (e.g. 530x100), the last tile is padded with transparency to form a square.

Tiles are saved to a `tiles/` folder in PNG format with transparency.


## Output example

```
image.png
tile_1: 100x100
tile_2: 100x100
tile_3: 100x100
tile_4: 100x100
tile_5: 30x100
Done
```



