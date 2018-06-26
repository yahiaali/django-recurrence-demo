from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    class Media:
        js = ('recurrence/js/recurrence.js',
              'recurrence/js/recurrence-widget.js')
        css = {
            'all': ('recurrence/css/recurrence.css',)
        }
