import os
from PIL import Image, ImageOps

# Directory & filenames
image_directory = r'C:\Users\domin\Desktop\patrick-portfolio\assets'
reference_image = 'amy.jpg'
target_images = ['main.jpg']     # ← only main.jpg will be processed

# Load reference, apply any EXIF rotation, grab its size + EXIF blob
ref_path = os.path.join(image_directory, reference_image)
with Image.open(ref_path) as ref_img:
    ref = ImageOps.exif_transpose(ref_img)
    target_size = ref.size                # (width, height)
    exif_data = ref.info.get('exif', None)
    jpeg_quality = 95                     # adjust if you know amy.jpg’s exact quality

for name in target_images:
    path = os.path.join(image_directory, name)
    try:
        with Image.open(path) as img:
            img = ImageOps.exif_transpose(img)

            # Center-crop & resize to exact same box
            fitted = ImageOps.fit(
                img,
                target_size,
                method=Image.Resampling.LANCZOS,
                centering=(0.5, 0.5)
            )

            save_kwargs = {
                'format': 'JPEG',
                'quality': jpeg_quality,
                'optimize': True,
            }
            if exif_data:
                save_kwargs['exif'] = exif_data

            fitted.save(path, **save_kwargs)
            print(f"Resized '{name}' → {target_size} @JPEG q={jpeg_quality}")
    except FileNotFoundError:
        print(f"❌ '{name}' not found at {path}")
    except Exception as e:
        print(f"❌ Error with '{name}': {e}")

print("Done resizing main.jpg.")
