from django.db.models import Q
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from apps.user.models import *
from apps.user.forms import *
from apps.teacher.models import *
from apps.student.models import *
from apps.teacher.forms import *
from apps.salary.models import *
from apps.student.forms import *
from apps.transaction.models import *
from .models import *
from .forms import *
from apps.user.utils import is_admin


@login_required(login_url='login')
@is_admin
def dashboard(request):
    current_month = datetime.now().month
    current_year = datetime.now().year

    expected_profit = sum([i.to_pay for i in Student.objects.all() if i.to_pay])
    transactions_amount = sum(
            [i.amount for i in Transaction.objects.filter(Q(date__year=current_year) & Q(date__month=current_month))]
        )
    salaries_amount = sum(
            [i.amount for i in Salary.objects.filter(Q(date__year=current_year) & Q(date__month=current_month))]
        )
    remainder = expected_profit - transactions_amount
    course_count, group_count, student_count, teacher_count = Course.objects.count(), Group.objects.count(), Student.objects.count(), Teacher.objects.count()
    last_five_transactions = Transaction.objects.order_by('-id')[:5]
    last_five_salaries = Salary.objects.order_by('-id')[:5]

    context = {
        'expected_profit': expected_profit,
        'transactions_amount': transactions_amount,
        'salaries_amount': salaries_amount,
        'last_five_transactions': last_five_transactions,
        'last_five_salaries': last_five_salaries,
        'course_count': course_count,
        'group_count': group_count,
        'student_count': student_count,
        'teacher_count': teacher_count,
        'remainder': remainder
    }
    return render(request, 'dashboard/dashboard.html', context)