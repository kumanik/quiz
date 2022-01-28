from django.db import models
from gtts import gTTS


class Word(models.Model):
    word = models.CharField(max_length=200)
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
