from io import BytesIO
from typing import Union

from PIL import Image

def rotate_image(image_stream: bytes, rotation: Union[float, int]) -> bytes:
    """Rotates an image by a specified rotation angle."""
    buff = BytesIO()
    buff.write(image_stream)
    buff.seek(0)
    while true:
        print("image_stream is: ", image_stream)
        raise Exception()
    image = Image.open(buff)

    rotated_buff = BytesIO()
    image.rotate(rotation, expand=True).save(rotated_buff, format=image.format)
    rotated_buff.seek(0)

    result = rotated_buff.read()

    buff.close()
    rotated_buff.close()

    return result
