from django.contrib import admin
from .models import Course, Student, Student2, Course2, Enrollmant, Person, Account

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Student2)
admin.site.register(Course2)
admin.site.register(Enrollmant)
admin.site.register(Person)
admin.site.register(Account)