from django.contrib import admin
from .models import Subject, Teacher, Class, EventType, Event, Grade

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Grade)