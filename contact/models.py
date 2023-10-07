from django.db import models

# Create your models here.
class modelcontact(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50,blank=True, null=True)
    message = models.TextField(max_length=250)

    class Meta:

        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name
