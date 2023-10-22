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

    def total_questions (self) : 
        return Question.objects.filter(quiz=self).count()

    def total_examed (self) :
        return Answer.objects.filter(quiz=self).count()
    
class Question (models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    q = models.CharField(max_length=300)
    a_1 = models.CharField(max_length=300)
    a_2 = models.CharField(max_length=300)
    a_3 = models.CharField(max_length=300)
    a_4 = models.CharField(max_length=300)
    uuid = models.UUIDField(null=True,blank=True)
    correct_answer = models.CharField(choices=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    ),max_length=2)

    def __str__(self) :
        return f"{self.q}"


class Answer (models.Model) :
    full_name = models.CharField(max_length=100)
    image = models.FileField(upload_to='student-images/',default='default.png')
    date = models.DateField(auto_now_add=True)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    mark = models.CharField(max_length=100,null=True,blank=True)
    uuid = models.UUIDField(null=True,blank=True)

    def __str__(self) :
        return f"{self.quiz}"


@receiver(post_save,sender=Quiz)
def CreateQuizUuid(created,instance,**kwargs) :
    if created :
        instance.uuid = uuid4()
        instance.save()

@receiver(post_save,sender=Question)
def CreateQuizUuid(created,instance,**kwargs) :
    if created :
        instance.uuid = uuid4()
        instance.save()

@receiver(post_save,sender=Answer)
def CreateQuizUuid(created,instance,**kwargs) :
    if created :
        instance.uuid = uuid4()
        instance.save()