from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from datetime import datetime
from .models import *
from .forms import *
from apps.user.utils import is_admin
from django.contrib import messages

@login_required(login_url='login')

def list(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    date = request.GET.get('date', '')
    
    if request.user.role == 'student':
        student_transactions= Transaction.objects.filter(student=request.user.student)
    else:
        student_transactions = Transaction.objects.all()

    if date:
        current_month = date.split('-')[1]
        current_year = date.split('-')[0]

    transactions = Transaction.objects.filter(Q(date__year=current_year) & Q(date__month=current_month)).order_by('-id')
    total = transactions.aggregate(total=Sum('amount'))['total']
    context = {
        'transactions': transactions,
        'current_month': current_month,
        'current_year': current_year,
        'total': total,
        'student_transactions': student_transactions
    }

    return render(request, 'transaction/list.html', context)


@login_required(login_url='login')
@is_admin
def update(request, pk):
    transaction = Transaction.objects.get(id=pk)
    form = TransactionForm(instance=transaction)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction-list')
    context = {
        'transaction': transaction,
        'form': form
    }
    return render(request, 'transaction/update.html', context)


@login_required(login_url='login')
@is_admin
def create(request, pk):
    transactions = Transaction.objects.filter(student_id=pk)
    student = Student.objects.get(id=pk)
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.instance.student = student
            form.save()
            messages.success(request, 'Транзакция успешна добавлена')
            return redirect('transaction-create', pk=student.id)

    context = {
        'form': form,
        'transactions': transactions,
        'student': student
    }
    return render(request, 'transaction/create.html', context)


@login_required(login_url='login')
@is_admin
def delete(request, pk, student):
    transaction = Transaction.objects.get(id=pk)
    transaction.delete()
    return redirect('transaction-create', pk=student)