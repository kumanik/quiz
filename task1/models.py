from django.db import models
from gtts import gTTS


class Word(models.Model):
    word = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    audio = models.FileField(upload_to='audio/', blank=True)
    lang = models.CharField(
        max_length=2,
        default='en',
        choices=[('en', 'English'), ('bn', 'Bengali')]
    )

    def __str__(self):
        return self.word

    def save(self):
        audio = gTTS(text=self.word, lang=self.lang, slow=True)
        audio.save('audio/' + str(self.id) + self.word + '.mp3')
        self.audio = 'audio/' + str(self.id) + self.word + '.mp3'
        super(Word, self).save()


class Question(models.Model):
    word1 = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='word1')
    word2 = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='word2')
    word3 = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='word3')

    def __str__(self):
        return self.word1.word + ' ' + self.word2.word + ' ' + self.word3.word


class Marks(models.Model):
    csv = models.FileField(upload_to='csv/', blank=True)
    total_marks = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)

    class Meta:
        unique_together = (('name', 'roll'))

    def __str__(self) -> str:
        return self.name + ' ' + self.roll