from django.contrib import admin
from TestApp.models import teacher, student, book


# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name',]

class teacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation',]

class bookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author',]


admin.site.register(student, studentAdmin)
admin.site.register(teacher, teacherAdmin)
admin.site.register(book, bookAdmin)
