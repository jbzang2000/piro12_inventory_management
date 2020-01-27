import os
from uuid import uuid4
from django.utils import timezone


def uuid_upload_to(instance, filename):
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출하고, 소문자로 변환
    return '/'.join([
        uuid_name[:2],
        uuid_name[2:4],
        uuid_name[4:] + extension,
    ])
