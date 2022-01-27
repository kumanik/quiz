from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)


class Passage(models.Model):
    passage = models.TextField()
    audio = models.FileField(upload_to='audio/', blank=True)
    question1 = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question1')
    question2 = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question2')
    question3 = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question3')
    question4 = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question4')
    question5 = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question5')
