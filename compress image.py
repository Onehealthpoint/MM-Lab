from PIL import Image


def compress_image(input_image_path, output_image_path, quality=55):
    with Image.open(input_image_path) as img:
        img.save(output_image_path, "JPEG", quality=quality)


input_image_path = 'input.jpg'
output_image_path = 'output.jpg'
compress_image(input_image_path, output_image_path)

