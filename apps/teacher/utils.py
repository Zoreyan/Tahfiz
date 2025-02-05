import random
from django.utils import timezone
from .models import Code
from datetime import timedelta

def generate_code():
    code = f"{random.randint(1000, 9999)}"
    if Code.objects.exists():
        latest = Code.objects.latest('created_at') 
        if timezone.now() - latest.created_at < timedelta(minutes=5):
            pass
        else:
            Code.objects.create(value=code, created_at=timezone.now())
    else:
        Code.objects.create(value=code, created_at=timezone.now())