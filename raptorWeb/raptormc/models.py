from tkinter import CASCADE
from django.db import models

# Create your models here.

class Server(models.Model):

    server_name = models.CharField(max_length=50, default="none", unique=True)

    server_state = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.server_name

class PlayerData(models.Model):

    server = models.ForeignKey(Server, default=0, on_delete=models.CASCADE)
    
    player_count = models.IntegerField(unique=False)

    player_names = models.TextField(max_length=1500, unique=False)

    def __str__(self) -> str:
        
        return str(self.player_count) + ", " + str(self.player_names)

    def get_count(self):

        return self.player_count

    def get_names(self):

        return self.player_names

    def get_state(self):

        return self.server_state
