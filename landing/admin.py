from django.contrib import admin
from .models import Register
# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'mobile', 'email', 'job', 'education', 'experience']


admin.site.register(Register, RegisterAdmin)