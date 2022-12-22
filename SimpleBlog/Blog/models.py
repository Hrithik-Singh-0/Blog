from django.db import models

class blogger(models.Model):
    ID = models.CharField(max_length=10)
    Name = models.CharField(max_length=20)
    Date = models.DateField()
    Image = models.ImageField(upload_to='images')
    Content = models.TextField(max_length=10000)

    def __str__(self):
        return self.Name