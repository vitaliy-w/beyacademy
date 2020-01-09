from django.contrib import admin

from .models import Student
from .models import LoginForm


admin.site.register(Student)
admin.site.register(LoginForm)
