from rest_framework import serializers
from .models import UserProfile, Teacher, Student, Category, Course, Grade


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True}
        }

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'expertise']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': True},
            'expertise': {'required': True}
        }
