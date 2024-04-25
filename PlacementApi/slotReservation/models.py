from student.models import Student

# Create your models here.
# Register your models here.
from django.db import models

class Slot(models.Model):
    author = models.ForeignKey(Student,blank=True, null=True, related_name="slotAuthor" ,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    booked = models.BooleanField(default=False)
    booked_by =models.ForeignKey(Student,blank=True, null=True, related_name="slotBookedBy",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title