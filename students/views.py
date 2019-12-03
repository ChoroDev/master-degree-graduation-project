from .models import Student, Message, Mark
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.db.models import Avg
import json


def index(request):
  message = None
  error_message = None
  if "message" in request.GET:
    message = request.GET["message"]
  if "error_message" in request.GET:
    error_message = request.GET["error_message"]
  
  return render(
    request,
    "index.html",
    {
      "all_students": Student.objects.order_by('-faculty')[:5],
      "message": message,
      "error_message": error_message
    })


def details(request, student_id):
  error_message = None
  student = get_object_or_404(Student, pk = student_id)
  if "error_message" in request.GET:
      error_message = request.GET["error_message"]
    
  return render(
    request,
    "student_info.html",
    {
      "student": student,
      "error_message": error_message,
      "user_rating": Mark.objects.filter(author_id = request.user.id).filter(student_id = student_id).aggregate(Avg('mark'))["mark__avg"],
      "avg_mark": Mark.objects.filter(student_id = student_id).aggregate(Avg('mark'))["mark__avg"],
      "already_rated_by_user": Mark.objects.filter(author_id = request.user.id).filter(student_id = student_id).count(),
      "latest_messages": Message.objects.filter(chat_id = student_id).order_by('-pub_date')[:5]
    }
  )


def post_comment(request, student_id):
  msg = Message()
  msg.message = request.POST['message']
  if not request.POST['message'].strip():
    error_message = "?error_message=Пустые комментарии теперь запрещены"
    return HttpResponseRedirect(app_url+str(student_id) + error_message)
  msg.author = request.user
  msg.chat = get_object_or_404(Student, pk = student_id)
  msg.pub_date = datetime.now()
  msg.save()
  return HttpResponseRedirect(app_url+str(student_id))


def msg_list(request, student_id):
  res = list(Message.objects.filter(chat_id = student_id).order_by('-pub_date')[:5].values('author__username','pub_date','message'))
  for r in res:
    r['pub_date'] = r['pub_date'].strftime('%d.%m.%Y %H:%M:%S')
  return JsonResponse(json.dumps(res), safe=False)


def post_mark(request, student_id):
  mark = Mark()
  mark.author = request.user
  mark.student = get_object_or_404(Student, pk = student_id)
  mark.mark = request.POST['mark']
  mark.pub_date = datetime.now()
  mark.save()
  return HttpResponseRedirect(app_url + str(student_id))


def get_mark(request, student_id):
  res = Mark.objects.filter(student_id = student_id).aggregate(Avg('mark'))
  return JsonResponse(json.dumps(res), safe=False)


def new_student(request):
  error_message = None
  if "error_message" in request.GET:
    error_message = request.GET["error_message"]
  return render(request, "new_student.html", {
    "error_message": error_message
  })


def add_new_student(request):
  is_superuser = request.user.is_superuser
  error_message = None
  if is_superuser != 1:
    error_message = '?error_message=You must be admin to do that!'
    return redirect('/students/' + error_message)
  name = None
  surname = None
  group = None
  faculty = None
  specialty = None
  entry_date = None
  if 'name' in request.POST:
    name = request.POST['name']
    if not name.strip():
      error_message = '?error_message=Name should be defined'
      return redirect('/students/new_student/' + error_message)
  else:
    error_message = '?error_message=Name should be defined'
    return redirect('/students/new_student/' + error_message)
  if 'surname' in request.POST:
    surname = request.POST['surname']
    if not surname.strip():
      error_message = '?error_message=Surname should be defined'
      return redirect('/students/new_student/' + error_message)
  else:
    error_message = '?error_message=Surname should be defined'
    return redirect('/students/new_student/' + error_message)

  is_exists = Student.objects.filter(name = name).filter(surname = surname)
  if is_exists:
    return redirect('/students/new_student/?error_message=Student already exists')

  if 'group' in request.POST:
    group = request.POST['group']
    if not group.strip():
      error_message = '?error_message=Group should be defined'
      return redirect('/students/new_student/' + error_message)
  else:
    error_message = '?error_message=Group should be defined'
    return redirect('/students/new_student/' + error_message)
  if 'faculty' in request.POST:
    faculty = request.POST['faculty']
    if not faculty.strip():
      error_message = '?error_message=Faculty should be defined'
      return redirect('/students/new_student/' + error_message)
  else:
    error_message = '?error_message=Faculty should be defined'
    return redirect('/students/new_student/' + error_message)
  if 'specialty' in request.POST:
    specialty = request.POST['specialty']
    if not specialty.strip():
      error_message = '?error_message=Specialty should be defined'
      return redirect('/students/new_student/' + error_message)
  else:
    error_message = '?error_message=Specialty should be defined'
    return redirect('/students/new_student/' + error_message)
  if 'entry_date' in request.POST:
    entry_date = request.POST['entry_date']
    if not entry_date.strip():
      error_message = '?error_message=Entry date should be defined'
      return redirect('/students/new_student/' + error_message)
  else:
    error_message = '?error_message=Entry date should be defined'
    return redirect('/students/new_student/' + error_message)
  message = '?message=New student added: ' + name + ' ' + surname
  student = Student()
  student.name = name
  student.surname = surname
  student.group = group
  student.faculty = faculty
  student.specialty = specialty
  student.entry_date = entry_date
  student.save()
  return redirect("/students/" + message)


def edit_student(request, student_id):
  return redirect('/students/' + str(student_id))


app_url = "/students/"
class RegisterFormView(FormView):
  form_class = UserCreationForm
  success_url = app_url + "login/"
  template_name = "reg/register.html"


  def form_valid(self, form):
      form.save()
      return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
  form_class = AuthenticationForm
  template_name = "reg/login.html"
  success_url = app_url
  def form_valid(self, form):
    self.user = form.get_user()
    login(self.request, self.user)
    return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
  def get(self, request):
    logout(request)
    return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
  form_class = PasswordChangeForm
  template_name = 'reg/password_change_form.html'
  success_url = app_url + 'login/'
  def get_form_kwargs(self):
    kwargs = super(PasswordChangeView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    if self.request.method == 'POST':
      kwargs['data'] = self.request.POST
    return kwargs
  def form_valid(self, form):
    form.save()
    return super(PasswordChangeView, self).form_valid(form)