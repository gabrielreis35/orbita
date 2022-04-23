import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

User = get_user_model()

DEFAULT_PASSWORD = '123456'

users = User.objects.all()

for user in users:
    user.set_password(DEFAULT_PASSWORD)
    user.save()

print(f'Reset passowrds Django: Password: {DEFAULT_PASSWORD}')