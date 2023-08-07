from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
job_choice = (
("علاقه مند یا دانشجو", "علاقه مند یا دانشجو"),
("دستیار مدیر محصول", "دستیار مدیر محصول"),
("مدیر محصول", "مدیر محصول"),
("مدیر محصول ارشد", "مدیر محصول ارشد"),
)

education_choice = (
("کمتر از کارشناسی", "کمتر از کارشناسی"),
("کارشناسی", "کارشناسی"),
("کارشناسی ارشد", "کارشناسی ارشد"),
("دکتری", "دکتری"),
("دیگر", "دیگر"),
)

experience_choice = (
("کمتر از یک سال", "کمتر از یک سال"),
("بین یک تا سه سال", "بین یک تا سه سال"),
("بین سه تا پنج سال", "بین سه تا پنج سال"),
("بیشتر از پنج سال", "بیشتر از پنج سال"),
)

class MyUserManager(BaseUserManager):
    def create_user(self, mobile, first_name, last_name, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, first_name, last_name, email, password=None, **other_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            mobile=mobile, first_name=first_name, last_name=last_name, email=email,
            password=password, **other_fields
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    mobile = models.CharField(max_length=11, verbose_name='شماره موبایل')
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    job = models.CharField(null=True, blank=True, max_length=100, choices=job_choice, default="A4")
    education = models.CharField(null=True, blank=True, max_length=100, choices=education_choice, default="A4")
    experience = models.CharField(null=True, blank=True, max_length=100, choices=experience_choice, default="A4")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')



    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'مدیریت کاربران'
        verbose_name_plural = 'مدیریت کاربران'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin












#
# class Register(models.Model):
#
#     firstname = models.CharField(null=True, blank=True, max_length=100)
#     lastname = models.CharField(null=True, blank=True, max_length=100)
#     mobile = models.CharField(null=True, blank=True, max_length=11)
#     email = models.CharField(null=True, blank=True, max_length=100)

#
#     def __str__(self):
#         return f"{self.mobile} {self.email}"

