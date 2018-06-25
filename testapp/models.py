from django.db import models
from recurrence.fields import RecurrenceField


class Course(models.Model):
    title = models.CharField(max_length=200)
    recurrences = RecurrenceField()
