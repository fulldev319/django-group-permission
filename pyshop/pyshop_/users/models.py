from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(_('First Name of User'),
                                  blank=True, max_length=20)

    last_name = models.CharField(_('Last Name of User'),
                                 blank=True, max_length=20)

    class Meta:
        permissions = (
            ("can_go_in_Group1", "To provide Group1 facility"),
            ("can_go_in_Group2", "To provide Group2 facility"),
        )
