from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from collections import defaultdict
from django.contrib import messages
from apps.user.utils import is_admin

@login_required(login_url='login')
def schedule(request):
    schedules = Schedule.objects.all()
    groups = Group.objects.all()
    days = Day.objects.all()
    
    subject_count = defaultdict(int)
    for schedule in schedules:
        subject_count[schedule.subject.name] += 1

    context = {
        'schedules': schedules,
        'groups': groups,
        'days': days,
        'subject_count': dict(subject_count)
    }
    return render(request, 'schedule/list.html', context)


@login_required(login_url='login')
@is_admin
def create(request):
    if request.user.role == 'student' or request.user.role == 'teacher':
        return redirect('schedule')
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.cleaned_data["group"]} - {form.cleaned_data["day"]} - {form.cleaned_data["subject"]} успешно создан')
            return redirect('schedule-create')
    context = {
        'form': form
    }
    return render(request, 'schedule/schedule_create.html', context)


@is_admin
def delete(request, pk):
    schedule = Schedule.objects.get(id=pk)
    schedule.delete()
    return redirect('schedule')


@login_required(login_url='login')
@is_admin
def subject_create(request):
    if request.user.role == 'student' or request.user.role == 'teacher':
        return redirect('schedule')

    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject-create')
    context = {
        'form': form
    }
    return render(request, 'schedule/subject_create.html', context)