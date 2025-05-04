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
    user = UserProfileSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'expertise']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': True},
            'expertise': {'required': True}
        }
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserProfile.objects.create(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': True},
            'enrollment_date': {'required': True}
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserProfile.objects.create(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

    def validate_name(self, value):
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Une catégorie avec ce nom existe déjà.")
        return value


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    category = CategorySerializer()
    students = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'teacher', 'students']
    
    def create(self, validated_data):
        teacher_data = validated_data.pop('teacher')
        category_data = validated_data.pop('category')
        students_data = validated_data.pop('students', [])

        user_data = teacher_data.pop('user')
        user = UserProfile.objects.create(**user_data)
        teacher = Teacher.objects.create(user=user, **teacher_data)

        category, _ = Category.objects.get_or_create(**category_data)

        course = Course.objects.create(teacher=teacher, category=category, **validated_data)
        course.students.set(students_data)
        return course

    def update(self, instance, validated_data):
        teacher_data = validated_data.pop('teacher', None)
        category_data = validated_data.pop('category', None)
        students_data = validated_data.pop('students', None)

        if teacher_data:
            user_data = teacher_data.pop('user', {})
            for attr, value in user_data.items():
                setattr(instance.teacher.user, attr, value)
            instance.teacher.user.save()
            for attr, value in teacher_data.items():
                setattr(instance.teacher, attr, value)
            instance.teacher.save()

        if category_data:
            category, _ = Category.objects.get_or_create(**category_data)
            instance.category = category

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if students_data is not None:
            instance.students.set(students_data)

        instance.save()
        return instance


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ['id', 'student', 'course', 'score', 'date_assigned']
    
    def validate_score(self, value):
        if not (0 <= value <= 20):
            raise serializers.ValidationError("Le score doit être entre 0 et 20.")
        return value
