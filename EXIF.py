from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(image_path):
    exif_data = Image.open(image_path)._getexif()
    if exif_data:
        exif = {
            TAGS.get(tag, tag): value
                for tag, value in exif_data.items()
        }

        return exif

# Test
'''
if __name__ == "__main__":
    exif = get_exif("../image/image.jpg")
    for tag, value in exif.items():
        print(f"{tag}: {value}")
'''
