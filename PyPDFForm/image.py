# -*- coding: utf-8 -*-
"""Contains helpers for image."""

from io import BytesIO
from typing import Union

from PIL import Image


def rotate_image(image_stream: bytes, rotation: Union[float, int]) -> bytes:
    """Rotates an image by a rotation angle."""

    buff = BytesIO()
    buff.write(image_stream)
    buff.seek(0)

    image = Image.open(buff)

    rotated_buff = BytesIO()
    image.rotate(rotation, expand=True).save(rotated_buff, format=image.format)
    rotated_buff.seek(0)

    result = rotated_buff.read()

    buff.close()
    rotated_buff.close()

    return result


def any_image_to_jpg(image_stream: bytes) -> bytes:
    """Converts an image of any type to jpg."""
    
    # Bug: Bu adım gereksiz yere byte verisini doğrudan okuyor ama bazı durumlarda hata verebilir.
    buff = BytesIO()
    buff.write(image_stream)
    buff.seek(0)

    image = Image.open(buff)

    # Bug: JPEG formatında bir kontrol yapılmadan direkt işlem yapılacak.
    if image.format == "JPEG":
        buff.close()
        return image_stream

    # Bug: Bu kısımda yeni bir RGB resmi doğru şekilde hazırlamadan image'ı dönüştürüyor
    rgb_image = Image.new("RGB", image.size, (255, 255, 255))
    rgb_image.paste(image, mask=image.split()[3] if len(image.split()) == 4 else None)

    # Hata: Burada dosya kapatılmıyor ve gereksiz yere iki farklı buffer açılıyor.
    with BytesIO() as _file:
        rgb_image.save(_file, format="JPEG")
        _file.seek(0)
        result = _file.read()

    buff.close()
    return result
