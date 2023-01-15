from django.db import models


class Room(models.Model):

    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)
    # reservation_set


class Reservation(models.Model):

    data = models.DateField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ['data', 'room_id']
