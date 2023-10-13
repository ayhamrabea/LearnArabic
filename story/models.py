from django.db import models

# Create your models here.

class Story(models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='story/images',blank=True, null=True)
    audio = models.FileField(upload_to='story/audios', blank=True, null=True)

    class Meta:

        verbose_name = 'Story'
        verbose_name_plural = 'Storys'

    def __str__(self):
        return self.title
    

class Parargraph(models.Model):

    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    section = models.TextField()
    class Meta:

        verbose_name = 'Parargraph'
        verbose_name_plural = 'Parargraphs'

    def __str__(self):
        return self.story.title

