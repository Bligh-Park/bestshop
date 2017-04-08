from django.contrib import admin

# Register your models here.
from user.models import UserLevel, UserInfo, PointHistory

admin.site.register(UserLevel)
admin.site.register(UserInfo)
admin.site.register(PointHistory)