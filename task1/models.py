from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    audio = models.FileField(upload_to='audio/', blank=True)


class Question(models.Model):
    word1 = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='word1')
    word2 = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='word2')
    word3 = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='word3')

    def __str__(self):
        return self.word1.word + ' ' + self.word2.word + ' ' + self.word3.word
