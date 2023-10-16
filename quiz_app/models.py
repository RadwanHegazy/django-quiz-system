from django.db import models
from users_app.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from uuid import uuid4

class Quiz (models.Model):
    title = models.CharField(max_length=100)
    uuid = models.UUIDField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    time = models.PositiveIntegerField()

    def __str__(self) : 
        return f"{self.title}"

class Question (models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    q = models.CharField(max_length=300)
    a_1 = models.CharField(max_length=300)
    a_2 = models.CharField(max_length=300)
    a_3 = models.CharField(max_length=300)
    a_4 = models.CharField(max_length=300)
    correct_answer = models.CharField(choices=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    ),max_length=2)



@receiver(post_save,sender=Quiz)
def CreateQuizUuid(created,instance,**kwargs) :
    if created :
        instance.uuid = uuid4()
        instance.save()