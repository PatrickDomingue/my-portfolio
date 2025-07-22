import os
from PIL import Image

# Set image directory
image_directory = r'C:\Users\domin\Desktop\patrick-portfolio\assets'

# Reference image
reference_image = 'finance.png'
target_images = ['ecoco.png']

# Get full path to reference image
reference_path = os.path.join(image_directory, reference_image)

try:
    with Image.open(reference_path) as ref_img:
        target_size = ref_img.size  # (width, height)
except FileNotFoundError:
    print(f"Reference image '{reference_image}' not found.")
    exit()

# Resize target images
for img_name in target_images:
    img_path = os.path.join(image_directory, img_name)
    try:
        with Image.open(img_path) as img:
            resized = img.resize(target_size, Image.Resampling.LANCZOS)
            resized.save(img_path)
            print(f"Resized {img_name} to match {reference_image}")
    except FileNotFoundError:
        print(f"Image '{img_name}' not found.")
    except Exception as e:
        print(f"Error resizing {img_name}: {e}")

print("Resize process completed.")
