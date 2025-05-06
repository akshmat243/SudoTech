from django.db import models

class EyeCarePatient(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EyeTestPrescription(models.Model):
    patient = models.ForeignKey(EyeCarePatient, on_delete=models.CASCADE)
    test_date = models.DateField()
    right_eye_power = models.CharField(max_length=20)
    left_eye_power = models.CharField(max_length=20)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {self.test_date}"


class EyeCareAppointment(models.Model):
    patient = models.ForeignKey(EyeCarePatient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {self.date}"


class EyewearCustomization(models.Model):
    patient = models.ForeignKey(EyeCarePatient, on_delete=models.CASCADE)
    frame_type = models.CharField(max_length=100)
    lens_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    additional_features = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name}'s Custom Eyewear"


class EyewearOrder(models.Model):
    patient = models.ForeignKey(EyeCarePatient, on_delete=models.CASCADE)
    order_date = models.DateField()
    customization = models.ForeignKey(EyewearCustomization, on_delete=models.SET_NULL, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {self.status}"
