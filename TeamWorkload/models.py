from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    role = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(TeamMember, related_name='tasks', on_delete=models.CASCADE)
    priority = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WorkloadOverview(models.Model):
    total_tasks = models.IntegerField()
    tasks_in_progress = models.IntegerField()
    tasks_completed = models.IntegerField()
    tasks_pending = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_overview(self):
        total = Task.objects.count()
        in_progress = Task.objects.filter(status='In Progress').count()
        completed = Task.objects.filter(status='Completed').count()
        pending = Task.objects.filter(status='Not Started').count()

        self.total_tasks = total
        self.tasks_in_progress = in_progress
        self.tasks_completed = completed
        self.tasks_pending = pending
        self.save()

    def __str__(self):
        return f"Workload Overview - Total Tasks: {self.total_tasks}"


class WorkloadSettings(models.Model):
    max_tasks_per_member = models.IntegerField(default=10)
    allow_task_assignment = models.BooleanField(default=True)
    notify_on_task_due = models.BooleanField(default=True)
    work_hours_per_day = models.IntegerField(default=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Settings: Max Tasks Per Member - {self.max_tasks_per_member}"
