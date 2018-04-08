from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse
import json
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Teacher, Subject, Student, Grade

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html', {'body_class': 'text-center', 'location': 'dashboard'})
    else:
        return HttpResponseForbidden()

def json_test(request):
    response_data = {'test': 2, 'qwerty': 'test'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

class TeacherList (ListView):
    model = Teacher
    def get_context_data(self, **kwargs):
        context = super(TeacherList, self).get_context_data(**kwargs)
        context['name'] = self.model.__name__ + 's'
        context['location'] = 'teachers'
        return context

class TeacherCreate(CreateView):
    model = Teacher
    fields = ['name', 'surname', 'description', 'subject', 'on_d`uty']
    success_url = reverse_lazy('teachers')
    template_name_suffix = '_create_form'

class TeacherUpdate(UpdateView):
    model = Teacher
    fields = ['name', 'surname', 'description', 'subject', 'on_duty']
    success_url = reverse_lazy('teachers')
    template_name_suffix = '_update_form'

class TeacherDelete(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers')
    template_name_suffix = '_delete_form'

class SubjectList (ListView):
    model = Subject
    def get_context_data(self, **kwargs):
        context = super(SubjectList, self).get_context_data(**kwargs)
        context['name'] = self.model.__name__ + 's'
        context['location'] = 'subjects'
        return context

class SubjectCreate(CreateView):
    model = Subject
    fields = ['name']
    success_url = reverse_lazy('subjects')
    template_name_suffix = '_create_form'

class SubjectUpdate(UpdateView):
    model = Subject
    fields = ['name']
    success_url = reverse_lazy('subjects')
    template_name_suffix = '_update_form'

class SubjectDelete(DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects')
    template_name_suffix = '_delete_form'

class StudentList (ListView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentList, self).get_context_data(**kwargs)
        context['name'] = self.model.__name__ + 's'
        context['location'] = 'students'
        return context

class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'surname', 'description', 'grade', 'on_duty']
    success_url = reverse_lazy('students')
    template_name_suffix = '_create_form'

class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'surname', 'description', 'grade', 'on_duty']
    success_url = reverse_lazy('students')
    template_name_suffix = '_update_form'

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    template_name_suffix = '_delete_form'

class GradeList (ListView):
    model = Grade
    def get_context_data(self, **kwargs):
        context = super(GradeList, self).get_context_data(**kwargs)
        context['name'] = self.model.__name__ + 's'
        context['location'] = 'grades'
        return context

class GradeCreate(CreateView):
    model = Grade
    fields = ['name']
    success_url = reverse_lazy('grades')
    template_name_suffix = '_create_form'

class GradeUpdate(UpdateView):
    model = Grade
    fields = ['name']
    success_url = reverse_lazy('grades')
    template_name_suffix = '_update_form'

class GradeDelete(DeleteView):
    model = Grade
    success_url = reverse_lazy('grades')
    template_name_suffix = '_delete_form'