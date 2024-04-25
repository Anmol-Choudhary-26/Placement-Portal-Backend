from rest_framework import serializers
from .models import Slot
from student.models import Student
class StudentListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.roll.username

    def to_internal_value(self, value):
        # print(Student.objects.get(roll__username = value))
        return Student.objects.get(roll__username = value)


class SlotSerializer(serializers.ModelSerializer):
    booked_by = serializers.CharField(required = False)
    author = StudentListingField(queryset = Student.objects.all(),write_only = True)
    class Meta:
        model = Slot
        fields = ['id', 'date', 'time', 'booked', 'title', 'description', 'duration', 'booked_by', "author"]

class Bookserializer(serializers.Serializer):
    slotID = serializers.CharField(help_text= "slot ID", max_length=256)
