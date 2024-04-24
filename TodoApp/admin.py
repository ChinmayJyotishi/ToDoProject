from django.contrib import admin
from .models import todo_model
# Register your models here.
@admin.register(todo_model)
class todo_model_Admin(admin.ModelAdmin):
    list_display=['task_name','task_status']