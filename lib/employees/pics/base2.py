"""
This shows how to load, resize, and save the resized images.

This uses the images in the original/ directory.
It will then store the resized images in a resized/ directory.
"""

import cv2
from pathlib import Path


def resize_img(img_file: Path, output_dir: Path):
    print(f"{img_file.as_posix()}")

    img_original = cv2.imread(img_file.as_posix(), cv2.IMREAD_COLOR)
    print(f"  original={img_original.shape}")

    img_resized_file = output_dir.joinpath(
        img_file.stem + "_resized" + img_file.suffix)
    img_resized = cv2.resize(img_original, (100, 100 ))
    print(f"  resized={img_resized.shape}")

    cv2.imshow(img_resized_file.name, img_resized)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    cv2.imwrite(img_resized_file.as_posix(), img_resized)


supported_img_ext = ("*.jpg", "*.png")

original_imgs_dir = Path("original")
original_imgs = []
for ext in supported_img_ext:
    original_imgs.extend(original_imgs_dir.glob(ext))

resized_imgs_dir = original_imgs_dir.parent.joinpath("resized")
if not resized_imgs_dir.exists():
    resized_imgs_dir.mkdir()

for img in original_imgs:
    resize_img(img, resized_imgs_dir)
