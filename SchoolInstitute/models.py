from django.db import models
from django.utils import timezone


class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.section}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    roll_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    admission_date = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Parent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Admission(models.Model):
    student_name = models.CharField(max_length=200)
    date_applied = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50, choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_name} - {self.status}"


class FeeManagement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - Due: {self.amount_due}"


class Homework(models.Model):
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} - {self.assigned_class}"


class Library(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    available_copies = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title


class Exam(models.Model):
    exam_name = models.CharField(max_length=100)
    exam_date = models.DateField()
    related_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exam_name} - {self.related_class}"


class Transport(models.Model):
    route_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.route_name


class Alumni(models.Model):
    student_name = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    current_occupation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Hostel(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    block_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - Room {self.room_number}"


class OnlineAssessment(models.Model):
    title = models.CharField(max_length=100)
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    posted_on = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HealthRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    checkup_date = models.DateField()
    health_issue = models.TextField(blank=True)
    doctor_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.checkup_date}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    attendees = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.date} - {'Present' if self.present else 'Absent'}"
