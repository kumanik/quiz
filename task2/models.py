from django.db import models
from gtts import gTTS


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)
    audio = models.FileField(upload_to='audio/', blank=True)
    lang = models.CharField(
        max_length=2,
        default='en',
        choices=[('en', 'English'), ('bn', 'Bengali')]
    )

    def save(self, *args, **kwargs):
        audio = gTTS(text=self.question_text, lang=self.lang, slow=True)
        audio.save('audio/' + str(self.id) + self.question_text[0:5] + '.mp3')
        self.audio = 'audio/' + str(self.id) + self.question_text[0:5] + '.mp3'
        super(Question, self).save(*args, **kwargs)


class Marks(models.Model):
    csv = models.FileField(upload_to='csv/', blank=True)
    total_marks = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)

    class Meta:
        unique_together = (('name', 'roll'))

    def __str__(self) -> str:
        return self.name + ' ' + self.roll