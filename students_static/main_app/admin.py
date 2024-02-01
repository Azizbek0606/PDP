from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Gander)
class GanderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'male_famale']

@admin.register(Lavel)
class LavelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'students_lavel']

    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'student_name' , 'slug_name' , "age"]
    prepopulated_fields = {"slug_name":("student_name" , )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user_name']