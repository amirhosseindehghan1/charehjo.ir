from django.db import models

# Create your models here.


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

class Register(models.Model):

    firstname = models.CharField(null=True, blank=True, max_length=100)
    lastname = models.CharField(null=True, blank=True, max_length=100)
    mobile = models.CharField(null=True, blank=True, max_length=11)
    email = models.CharField(null=True, blank=True, max_length=100)
    job = models.CharField(null=True, blank=True, max_length=100, choices=job_choice, default="A4")
    education = models.CharField(null=True, blank=True, max_length=100, choices=education_choice, default="A4")
    experience = models.CharField(null=True, blank=True, max_length=100, choices=experience_choice, default="A4")

    def __str__(self):
        return f"{self.mobile} {self.email}"

