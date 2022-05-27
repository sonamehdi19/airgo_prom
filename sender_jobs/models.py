from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Account
# Create your models here.


class SenderJobs(models.Model):
    location = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    due_date = models.DateField()
    contact_number = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    add_image = models.ImageField(upload_to='upload_images')
    additional_note = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return '{} looking for  one that goes to {}'.format(self.owner,
                                                            self.destination)


class CarrierJobs(models.Model):
    location = models.CharField(max_length=150)
    departure_date = models.DateField()
    destination = models.CharField(max_length=150)
    arrival_date = models.DateField()
    contact_number = models.CharField(
        max_length=50, null=False, blank=False, unique=True)
    additional_note = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return '{} is ready to carry to {}'.format(self.owner,
                                                   self.destination)
