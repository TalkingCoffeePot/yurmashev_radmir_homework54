from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main_app.models import Product, Categories
# Create your views here.


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    print(products)
    return render(request, 'main_page.html', context)

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
