from django.contrib import admin

from .models import Student, Message, Mark

admin.site.register(Student)
admin.site.register(Message)
admin.site.register(Mark)