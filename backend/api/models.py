from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,default=99.99,max_digits=15)

class League(models.Model):
    name = models.CharField(max_length=150, unique= True)
    numOfTeams = models.IntegerField()

    def __str__(self) -> str:
        return "%s" % (self.name)

class FootballClub(models.Model):
    name = models.CharField(max_length=150,unique=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    numOfPlayers = models.IntegerField()

    def __str__(self) -> str:
        return "%s ( %s ) : %d players" % (self.name, self.league.name, self.numOfPlayers)
