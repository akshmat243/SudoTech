from django.db import models

class LabPatient(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PatientCard(models.Model):
    patient = models.OneToOneField(LabPatient, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100, unique=True)
    issued_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {self.card_number}"


class LabAppointment(models.Model):
    patient = models.ForeignKey(LabPatient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {self.appointment_date}"


class LabTestRequest(models.Model):
    appointment = models.ForeignKey(LabAppointment, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    requested_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test_name} for {self.appointment.patient.name}"


class LabInventory(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class LabBilling(models.Model):
    patient = models.ForeignKey(LabPatient, on_delete=models.CASCADE)
    bill_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {'Paid' if self.paid else 'Unpaid'}"


class LabResult(models.Model):
    lab_test = models.ForeignKey(LabTestRequest, on_delete=models.CASCADE)
    result_file = models.FileField(upload_to='lab_results/')
    comments = models.TextField(blank=True, null=True)
    reported_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Result for {self.lab_test}"


class PatientHistory(models.Model):
    patient = models.ForeignKey(LabPatient, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    description = models.TextField()
    record_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name} - {self.condition}"


class LabSystemSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
