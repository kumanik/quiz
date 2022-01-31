from django.db import models
from gtts import gTTS


class Mcq(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)


class Question(models.Model):
    passage = models.TextField()
    audio = models.FileField(upload_to='audio/', blank=True)
    question1 = models.ForeignKey(
        Mcq, on_delete=models.CASCADE, related_name='question1')
    question2 = models.ForeignKey(
        Mcq, on_delete=models.CASCADE, related_name='question2')
    question3 = models.ForeignKey(
        Mcq, on_delete=models.CASCADE, related_name='question3')
    question4 = models.ForeignKey(
        Mcq, on_delete=models.CASCADE, related_name='question4')
    question5 = models.ForeignKey(
        Mcq, on_delete=models.CASCADE, related_name='question5')
    lang = models.CharField(
        max_length=2,
        default='en',
        choices=[('en', 'English'), ('bn', 'Bengali')]
    )

    def save(self):
        audio = gTTS(text=self.passage, lang=self.lang, slow=True)
        audio.save('audio/' + str(self.id) + self.passage[0:5] + '.mp3')
        self.audio = 'audio/' + str(self.id) + self.passage[0:5] + '.mp3'
        super(Question, self).save()


class Marks(models.Model):
    csv = models.FileField(upload_to='csv/', blank=True)
    total_marks = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)

    class Meta:
        unique_together = (('name', 'roll'))

    def __str__(self) -> str:
        return self.name + ' ' + self.roll
