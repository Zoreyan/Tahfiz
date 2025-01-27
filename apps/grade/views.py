from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from datetime import datetime
from apps.user.utils import is_teacher


def group_list(request):
    groups = Group.objects.order_by('title')

    if request.user.role == 'teacher':
        groups = groups.filter(teacher=request.user.teacher)
    context = {
        'groups': groups
    }
    return render(request, 'grade/group_list.html', context)


def diary(request):
    student = request.user.student
    subjects = Subject.objects.order_by('name')
    grades = Grade.objects.filter(student=student).order_by('date')
    date = request.GET.get('month')
    
    if date:
        year, month = date.split('-')
        grades = grades.filter(Q(date__month=month) & Q(date__year=year))
    else:
        date = f'{datetime.now().year}-{datetime.now().month:02}'

    days = grades.dates('date', 'day')
    context = {
        'student': student,
        'grades': grades,
        'subjects': subjects,
        'days': days,
        'date': date
    }
    
    return render(request, 'grade/diary.html', context)


def subject_list(request, pk):
    group = Group.objects.get(id=pk)
    subjects = Subject.objects.order_by('name')
    context = {
        'subjects': subjects,
        'group': group
    }
    return render(request, 'grade/subject_list.html', context)


def list(request, group_pk, subject_pk):
    group = Group.objects.get(id=group_pk)
    subject = Subject.objects.get(id=subject_pk)
    students = Student.objects.filter(group=group)
    grades = Grade.objects.filter(subject=subject)
    
    date = request.GET.get('month')
    
    if date:
        year, month = date.split('-')
        grades = grades.filter(Q(date__month=month) & Q(date__year=year))
    else:
        grades = grades.filter(Q(date__month=datetime.now().month) & Q(date__year=datetime.now().year))
        date = f'{datetime.now().year}-{datetime.now().month:02}'
    if request.user.role == 'teacher':
        teacher = request.user.teacher
        students = students.filter(group__in=teacher.group.all())
        grades = grades.filter(teacher=teacher)

        if request.method == 'POST':
            mark = request.POST.get('mark')
            pages = request.POST.get('pages', 0)
            student_id = request.POST.get('student_id')
            student = Student.objects.get(id=student_id)
            date = request.POST.get('date')
            Grade.objects.create(teacher=teacher, student=student, mark=mark, subject=subject, date=date, pages=pages)

    days = grades.dates('date', 'day')
    

    context = {
        'students': students,
        'subject': subject,
        'days': days,
        'date':date,
        'group': group,
    }
    return render(request, 'grade/list.html', context)


def details(request, pk):
    grade = get_object_or_404(Grade, id=pk)

    context = {
        'grade': grade
    }
    return render(request, 'grade/details.html', context)


def delete(request, group_pk, subject_pk, pk):
    grade = get_object_or_404(Grade, id=pk)

    grade.delete()
    return redirect('grade-list', group_pk=group_pk, subject_pk=subject_pk)
