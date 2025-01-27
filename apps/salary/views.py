from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import Q
from datetime import datetime
from apps.user.utils import is_admin
from django.contrib import messages

@login_required(login_url='login')
@is_admin
def create(request):

    form = SalaryForm()
    if request.method == 'POST':
        
        form = SalaryForm(request.POST)
        if request.method == 'POST':
            form = SalaryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Транзакция успешна добавлена')
                return redirect('salary-create')
    
    return render(request, 'salary/create.html', {'form': form})


@login_required(login_url='login')
@is_admin
def list(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    date = request.GET.get('date', '')
    if date:
        current_month = date.split('-')[1]
        current_year = date.split('-')[0]

    salaries = Salary.objects.filter(Q(date__year=current_year) & Q(date__month=current_month)).order_by('-id')
    total = sum([salary.amount for salary in salaries])
    context = {
        'salaries': salaries,
        'current_month': current_month,
        'current_year': current_year,
        'total': total
    }
        
    return render(request, 'salary/list.html', context)


@login_required(login_url='login')
@is_admin
def update(request, pk):
    salary = Salary.objects.get(id=pk)
    form = SalaryForm(instance=salary)
    if request.method == 'POST':
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('salary-list')
    context = {
        'salary': salary,
        'form': form
    }
    return render(request, 'salary/update.html', context)

@login_required(login_url='login')
@is_admin
def delete(request, pk):
    salary = Salary.objects.get(id=pk)
    salary.delete()
    return redirect('salary-list')