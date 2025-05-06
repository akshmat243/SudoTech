from django.db import models

class GoogleSheet(models.Model):
    sheet_name = models.CharField(max_length=255, verbose_name="Sheet Name")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Updated On")

    def __str__(self):
        return self.sheet_name
