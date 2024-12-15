from PIL import Image


def center_image_on_white_background(image_path, output_path):
    """
    画像を白背景の正方形キャンバスの中心に配置

    Args:
        image_path (str): 入力画像のパス
        output_path (str): 出力画像のパス

    Returns:
        None

    Examples:
        >>> center_image_on_white_background("input.jpg", "output.jpg")
    """

    image = Image.open(image_path)

    # 画像の元の幅と高さを取得
    original_width, original_height = image.size

    # 正方形のキャンバスサイズを決定（元の画像の幅と高さのうち大きい方に合わせる）
    canvas_size = max(original_width, original_height)

    # 白背景の正方形キャンバスを作成
    canvas = Image.new("RGB", (canvas_size, canvas_size), "white")

    # 画像をキャンバスの中心に配置
    offset_x = (canvas_size - original_width) // 2
    offset_y = (canvas_size - original_height) // 2
    canvas.paste(image, (offset_x, offset_y))

    # 結果の画像を保存
    canvas.save(output_path)

    # print(f"画像が'{output_path}'に保存されました。")




def center_image_with_padding(input_path, output_path, padding=0.1):
    """
    画像を白背景の正方形キャンバスの中心に配置し、横に余白を追加

    Args:
        input_path (str): 入力画像のパス
        output_path (str): 出力画像のパス
        padding (float): 余白の割合（0.0～1.0）

    Returns:
        None

    Examples:
        >>> center_image_with_padding("input.jpg", "output.jpg", padding=0.1)
    """


    image = Image.open(input_path)

    # 元の幅と高さを取得
    original_width, original_height = image.size

    # 余白を追加した新しいキャンバスの幅を計算
    new_width = int(original_width * (1 + padding))
    new_height = max(new_width, original_height)  # 正方形になるように調整

    # 白背景の正方形キャンバスを作成
    canvas = Image.new("RGB", (new_width, new_width), "white")

    # 中心に画像を配置
    offset_x = (new_width - original_width) // 2
    offset_y = (new_width - original_height) // 2
    canvas.paste(image, (offset_x, offset_y))

    # 結果を保存
    canvas.save(output_path)

    # print(f"画像が'{output_path}'に保存されました。")




# test
'''
if __name__ == "__main__":
    input_image_path = "../image/image.jpg"   # imput
    output_image_path = "../output/image.jpg" # output
    output_image_path_2 = "../output/image_2.jpg"
    center_image_on_white_background(input_image_path, output_image_path)
    center_image_with_padding(input_image_path, output_image_path_2, padding=0.05)
'''
