from django.db import models

class Spreadsheet(models.Model):
    file_or_folder_name = models.CharField(max_length=255, verbose_name="File / Folder Name")
    related = models.CharField(max_length=255, verbose_name="Related", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_or_folder_name
