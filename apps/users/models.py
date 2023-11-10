from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.base.models import BaseModel


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f"{self.pk}. {self.username}"

    def is_employee(self):
        return hasattr(self, 'employee')

    def is_client(self):
        return hasattr(self, 'client')


class Employee(BaseModel):
    class Meta:
        db_table = 'employee'
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    user = models.OneToOneField(to="User", verbose_name=_("User"), on_delete=models.CASCADE, related_name='employee')
    first_name = models.CharField(verbose_name=_("First name"), max_length=200)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=200)
    middle_name = models.CharField(verbose_name=_("Middle name"), max_length=200)
    birth_date = models.DateField(verbose_name=_("Birth date"))

    def __str__(self):
        return f"{self.pk}. {self.get_full_name()}"

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Client(BaseModel):
    class Meta:
        db_table = 'client'
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    user = models.OneToOneField(to="User", verbose_name=_("User"), on_delete=models.CASCADE, related_name='client')
    first_name = models.CharField(verbose_name=_("First name"), max_length=200)
    last_name = models.CharField(verbose_name=_("Last name"), max_length=200)
    middle_name = models.CharField(verbose_name=_("Middle name"), max_length=200)
    birth_date = models.DateField(verbose_name=_("Birth date"))

    def __str__(self):
        return f"{self.pk}. {self.get_full_name()}"

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
