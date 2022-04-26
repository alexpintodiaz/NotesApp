from django.db import models

# Create your models here.

class NotesApp(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto. format(self.title,self.create_date)
        

    