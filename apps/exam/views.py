from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Exam, Question, StudentExam, Answer
from .forms import QuestionForm, ExamForm, AnswerForm
from apps.student.models import Student
from datetime import datetime


@login_required(login_url='login')
def create(request):
    form = ExamForm()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam-create')
    context = {
        'form': form,
    }
    return render(request, 'exam/create.html', context)


@login_required(login_url='login')
def update(request, pk):
    exam = Exam.objects.get(id=pk)
    form = ExamForm(instance=exam)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exam-details', pk=exam.id)


    context = {
        'form': form,
    }
    return render(request, 'exam/update.html', context)


@login_required(login_url='login')
def question_create(request, pk):
    exam = Exam.objects.get(id=pk)
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.instance.exam = exam
            form.save()
            return redirect('exam-details', pk=pk)
    context = {
        'form': form,
        'exam': exam
    }
    return render(request, 'exam/question_create.html', context)


@login_required(login_url='login')
def answer_create(request, pk):
    question = Question.objects.get(id=pk)
    answers = Answer.objects.filter(question=question)
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.instance.question = question
            form.save()
            return redirect('exam-answer-create', pk=pk)
    context = {
        'form': form,
        'question': question,
        'answers': answers
    }
    return render(request, 'exam/answer_create.html', context)


@login_required(login_url='login')
def list(request):
    exams = Exam.objects.all()
    if request.user.role == 'student':
        exams = Exam.objects.filter(groups__in=request.user.student.group.all())
    context = {
        'exams': exams,
    }
    return render(request, 'exam/list.html', context)


@login_required(login_url='login')
def student_exam_list(request):
    if StudentExam.objects.filter(student=request.user).exists():

        exams = Exam.objects.filter(groups__in=request.user.student.group.all(), studentexam__completed=False)
    else:
        exams = Exam.objects.filter(groups__in=request.user.student.group.all())

    context = {
        'exams': exams,
    }
    return render(request, 'exam/student_exam_list.html', context)


@login_required(login_url='login')
def details(request, pk):
    exam = Exam.objects.get(id=pk)
    questions = Question.objects.filter(exam=exam)
    context = {
        'exam': exam,
        'questions': questions
    }
    return render(request, 'exam/details.html', context)


def start(request, pk, question_id):
    exam = Exam.objects.get(id=pk)
    question = Question.objects.get(id=question_id)
    questions = Question.objects.filter(exam=exam)
    student_exam, created = StudentExam.objects.get_or_create(student=request.user, exam=exam)

    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        answer = Answer.objects.get(id=answer_id)
        student_exam.answers.add(answer)
        if answer.is_correct:
            student_exam.score += 1
            
            student_exam.save()
        next_question = questions.filter(id__gt=question.id).first()

        if next_question:
            return redirect('exam-start', pk=exam.id, question_id=next_question.id)
        else:
            return redirect('exam-finish', pk=student_exam.id)

    context = {
        'exam': exam,
        'question': question,
        'questions': questions
    }
    return render(request, 'exam/start.html', context)


def finish(request, pk):
    student_exam = StudentExam.objects.get(id=pk)
    student_exam.completed = True
    student_exam.end_time = datetime.now()
    student_exam.save()

    if student_exam.score >= student_exam.exam.pass_points:
        result = True
    else:
        result = False


    context = {
        'student_exam': student_exam,
        'result': result
    }
    return render(request, 'exam/finish.html', context)


def result_list(request):
    student_exams = StudentExam.objects.all()

    context = {
        'student_exams': student_exams
    }
    return render(request, 'exam/result_list.html', context)


@login_required(login_url='login')
def result_details(request, pk):
    student_exam = StudentExam.objects.get(id=pk)
    answers = student_exam.answers.all()
    context = {
        'student_exam': student_exam,
        'answers': answers,
    }
    return render(request, 'exam/result_details.html', context)


@login_required(login_url='login')
def delete(request, pk):
    exam = Exam.objects.get(id=pk)
    exam.delete()
    return redirect('exam-list')


@login_required(login_url='login')
def question_delete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return redirect('exam-details', pk=question.exam.id)


@login_required(login_url='login')
def answer_delete(request, pk):
    answer = Answer.objects.get(id=pk)
    answer.delete()
    return redirect('exam-answer-create', pk=answer.question.id)