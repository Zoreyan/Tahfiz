
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.dashboard.forms import *
from django.db.models import Sum, Avg, F
from django.db.models.functions import Round
from .models import *
from .forms import *
from apps.teacher.models import *
from apps.group.models import *
from apps.transaction.models import *
from apps.user.utils import generate_password, is_admin
from django.contrib import messages
from apps.schedule.models import *


@login_required(login_url='login')
@is_admin
def create(request):

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            password = generate_password()
            user = User.objects.create_user(username=password, password=password, role='student')
            form.instance.user = user
            form.instance.status = True
            form.save()
            messages.success(request, 'Студент создан')
            return redirect('student-create')

    context = {
        'form': form
    }
    return render(request, 'student/create.html', context)


@login_required(login_url='login')
@is_admin
def list(request):
    students = Student.objects.all().order_by('-id')

    context = {
        'students': students,
    }
    return render(request, 'student/list.html', context)



@login_required(login_url='login')
@is_admin
def details(request, pk):

    student = get_object_or_404(Student, id=pk)
    form = StudentForm(instance=student)
    total = Transaction.objects.filter(student=student).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-details', pk=pk)

    transactions = Transaction.objects.filter(student=student).order_by('-id')

    context = {
        'student': student,
        'form': form,
        'total_amount': total,
        'transactions': transactions
        }
    
    return render(request, 'student/details.html', context)


@is_admin
def delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    user = User.objects.get(student=student)
    student.delete()
    user.delete()
    return redirect('student-list')


def rating_list(request):
    subject = Subject.objects.get(id=1)
    students = Student.objects.annotate(
        rating_sum=Sum('grade__mark'), filter=Q(grade__subject=subject),
        average=Round(Avg('grade__mark', filter=Q(grade__subject=subject)), 2) ).order_by('-rating_sum')

    context = {
        'students': students
    }
    return render(request, 'student/rating_list.html', context)


def rating_details(request, pk):
    subject = Subject.objects.get(id=pk)
    month, year = datetime.now().month, datetime.now().year

    students = Student.objects.annotate(
        points=Sum('grade__mark', filter=Q(grade__subject=subject) & Q(grade__date__month=month) & Q(grade__date__year=year)),
        pages=Sum('grade__pages', filter=Q(grade__subject=subject) & Q(grade__date__month=month) & Q(grade__date__year=year)),
        weighted_score=Sum(F('grade__mark') * F('grade__pages'), filter=Q(grade__subject=subject) & Q(grade__date__month=month) & Q(grade__date__year=year)),
        average=Round(Avg('grade__mark', filter=Q(grade__subject=subject) & Q(grade__date__month=month) & Q(grade__date__year=year)), 2)  # округление до 2 знаков
    ).order_by('-weighted_score')


    context = {
        'students': students,  # если вам нужны студенты отдельно
        'subject': subject
    }
    return render(request, 'student/rating_details.html', context)

