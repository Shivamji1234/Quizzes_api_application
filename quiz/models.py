from django.db import models
from django.utils import timezone

# Create your models here.
class Quiz(models.Model):
    QUESTION_STATUS = (
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('finished', 'Finished'),
    )
    question=models.CharField(max_length=100)
    options=models.JSONField()
    right_answer=models.IntegerField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    Stauts=models.CharField(max_length=10,choices=QUESTION_STATUS,default="inactive")
    
    def save(self, *args, **kwargs):
        now = timezone.now()
        if now < self.start_date:
            self.status = 'inactive'
        elif self.start_date <= now <= self.end_date:
            self.status = 'active'
        else:
            self.status = 'finished'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Quiz {self.pk}: {self.question}"


    
    
    