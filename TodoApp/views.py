from django.shortcuts import render,redirect,get_object_or_404
from .models import todo_model
from datetime import date,datetime

# Create your views here.
def todo_view(request):
    incomplete_tasks=todo_model.objects.filter(task_status=False)
    complete_tasks=todo_model.objects.filter(task_status=True)
    task_status_completed=complete_tasks.count()
    task_status_pending=incomplete_tasks.count()

    pr_count=todo_model.objects.count()

    progress_count= round((task_status_completed / pr_count) * 100, 2)
    progress_count_pending= round((task_status_pending / pr_count) * 100, 2)
    # time_=datetime.now()
    # time_current=time_.strftime('%I,%M,%P')
    # if time_current=='12:00 AM':
    #     incomplete_tasks.delete()
    #     complete_tasks.delete()


    todays_date=date.today()
    d={
        "incomplete_tasks":incomplete_tasks,
        "complete_tasks":complete_tasks,
        "task_status_completed":task_status_completed,
        "task_status_pending":task_status_pending ,
        "todays_date":todays_date,
        'progress_count':progress_count,
        'progress_count_pending':progress_count_pending
    
    }

    return render(request,'TodoApp/index.html',d )

def add_task(request):
    data=request.POST['task_input']
    todo_model.objects.create(task_name=data)
    return redirect('home')

def task_done(request,id):
    task=get_object_or_404(todo_model,id=id)
    task.task_status=True
    task.save()
    return redirect('home')
def task_update(request,id):
    record=get_object_or_404(todo_model,id=id)
    if request.method=='POST':
        data=request.POST['updated_task']
        record.task_name=data
        record.save()
        return redirect('home')

    taskname=record.task_name
    return render(request,'TodoApp/update.html',context={'task_name':taskname ,'record':record})

def task_delete(request,id):
    record=get_object_or_404(todo_model,id=id)
    record.delete()
    return redirect('home')

def task_undo(request,id):
    record=get_object_or_404(todo_model,id=id)
    record.task_status=False
    record.save()
    return redirect('home')
    
def task_all_clear(request):
    complete_tasks=todo_model.objects.filter(task_status=True)
    complete_tasks.delete()
    return redirect('home')