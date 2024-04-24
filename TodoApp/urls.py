from django.urls import path
from . import views
urlpatterns = [
    path('', views.todo_view,name='home'),
    path('add_task', views.add_task, name="add_task"),
    path('task_done/<int:id>', views.task_done, name="task_done"),
    path('update/<int:id>', views.task_update, name="task_update"),
    path('delete/<int:id>', views.task_delete, name="task_delete"),
    path('undo/<int:id>', views.task_undo, name="task_undo"),
    path('clear_all/',views.task_all_clear,name='all_clear')
    
]