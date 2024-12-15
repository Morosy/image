from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(image_path):
    """
    画像のEXIF情報を取得

    Args:
        image_path (str): 画像のパス

    Returns:
        dict: 画像のEXIF情報

    Examples:
        >>> exif = get_exif("image.jpg")
    """

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
    path = "../image/image.jpg"
    exif = get_exif(path)
    for tag, value in exif.items():
        print(f"{tag}: {value}")
'''
