from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('course/<int:course_id>/lessons/', views.course_lessons, name='course_lessons'),
    path('logout/', views.logout_view, name='logout'),
]
