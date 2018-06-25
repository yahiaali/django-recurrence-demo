from django.shortcuts import render
from django.http import HttpResponse
from .forms import CourseForm


def index(request):
    form = CourseForm()
    return render(request, 'test_form.html', {'form': form})
