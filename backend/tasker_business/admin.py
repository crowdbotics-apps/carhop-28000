from django.contrib import admin
from .models import TaskerSkill, BusinessPhoto, Timeslot, TaskerAvailability

admin.site.register(BusinessPhoto)
admin.site.register(TaskerAvailability)
admin.site.register(Timeslot)
admin.site.register(TaskerSkill)

# Register your models here.
