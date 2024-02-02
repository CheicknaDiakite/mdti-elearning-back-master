import base64
import random
import time

from django.core.files.base import ContentFile


def base64_to_image(data):
    try:
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]
    except:
        return None

    return ContentFile(base64.b64decode(imgstr), name=f"{random.randint(0,18000)}/{time.time()}." + ext)  # You can save this as file instance.
