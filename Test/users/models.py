from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        permissions = (
            ("can_go_in_View1", "To provide View1 facility"),
            ("can_go_in_View2", "To provide View2 facility"),
        )