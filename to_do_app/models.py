from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    desc = models.TextField(max_length=1000, null=True, blank=True)
    complete = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['create_date']
