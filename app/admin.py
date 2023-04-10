from django.contrib import admin

from app.models import *
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


# Register your models here.
admin.site.register(CustomUser, UserModel)
admin.site.register(District)
admin.site.register(Province)
admin.site.register(Local_Level)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Petrolpump)
admin.site.register(FuelType)
admin.site.register(FiscalYear)
admin.site.register(FuelExpense)
admin.site.register(WorkPlace)
admin.site.register(Objective)
admin.site.register(Budget)
