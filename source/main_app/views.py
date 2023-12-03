from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# def main_list(request):
#     tasks = Task.objects.all()
#     context = {
#         'tasks': tasks
#     }
#     return render(request, 'main_page.html', context)

# #############################################################################
# def new_task(request):
#     context = {
#         'status_choices': status_choices
#     }
#     return render(request, 'add_task.html', context)

# #############################################################################
# def add_task(request):
#     description = request.POST.get('description')
    
#     status = request.POST.get('status')
#     for x in status_choices:
#         if x[0] == status:
#             status = x[1]

#     date = request.POST.get('date')
#     details = request.POST.get('details')

#     Task.objects.create(description=description, task_status=status, date=date, details=details)
#     task = Task.objects.all()

#     context = {
#         'tasks': task
#     }
#     return redirect('tasks')

# ##############################################################################
# def detailed_view(request, pk):
#     task = Task.objects.get(pk=pk)
#     context = {
#         'task': task
#     }
#     return render(request, 'detailed_task.html', context)
