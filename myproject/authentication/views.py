from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, LessonForm
from .models import Course, Lesson

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    course = lesson.course  # Lấy khóa học liên quan đến bài học

    # Tìm bài học trước và sau
    previous_lesson = Lesson.objects.filter(course=course, order__lt=lesson.order).last()
    next_lesson = Lesson.objects.filter(course=course, order__gt=lesson.order).first()

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)  # Pass the instance for updating
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson updated successfully.')
            return redirect('lesson_detail', lesson_id=lesson_id)
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'lesson_detail.html', {
        'lesson': lesson,
        'form': form,
        'course': course,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson
    })


def course_lessons(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.all()  # Lấy danh sách bài học của khóa học

    return render(request, 'course_lessons.html', {'course': course, 'lessons': lessons})



