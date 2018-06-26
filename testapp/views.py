from django.shortcuts import render
from django.http import HttpResponse
from .forms import CourseForm


def index(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()
    return render(request, 'test_form.html', {'form': form})
