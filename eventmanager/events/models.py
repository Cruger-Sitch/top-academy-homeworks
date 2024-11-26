from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=300)

    def __str__(self)->str:
        return f'{self.title} by {self.description} by {self.event_date} by {self.location}'


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self)->str:
        return f'{self.name} by {self.email} by {self.message}'
