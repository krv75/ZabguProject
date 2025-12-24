from django.contrib import admin
from guest import models


admin.site.register(models.Category)
admin.site.register(models.TeacherInfo)
admin.site.register(models.DepartmentInfo)
admin.site.register(models.ContactData)
admin.site.register(models.News)