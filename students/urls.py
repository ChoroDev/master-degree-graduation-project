from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:student_id>/', views.details, name = 'details'),
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('password-change/', views.PasswordChangeView.as_view()),
    path('<int:student_id>/post_comment/', views.post_comment, name='post_comment'),
    path('<int:student_id>/msg_list/', views.msg_list, name='msg_list'),
    path('<int:student_id>/post_mark/', views.post_mark, name='post_mark'),
    path('<int:student_id>/get_mark/', views.get_mark, name='get_mark'),
    path('new_student/', views.new_student, name='new_student'),
    path('new_student/add_new_student/', views.add_new_student, name='add_new_student'),
    path('edit_student/', views.edit_student, name='edit_student')
]