from django.db import models

class SideMenuBuilder(models.Model):
    menu_name = models.CharField(max_length=100)
    menu_type = models.CharField(max_length=100)
    parent_module = models.CharField(max_length=100)
    which_window = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)      

    def __str__(self):
        return self.menu_name
