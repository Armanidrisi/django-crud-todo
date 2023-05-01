from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title