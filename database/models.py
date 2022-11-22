from django.db import models

class User(models.Model):
    userID = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=88)
    age = models.IntegerField(default=0)

class Artist(models.Model):
    artistID = models.CharField(primary_key=True, max_length=30)
    artistName = models.CharField(max_length=20)
    artistRate = models.IntegerField(default=0)

class Song(models.Model):
    songID = models.CharField(primary_key=True, max_length=30)
    songTitle = models.CharField(max_length=30)
    releaseDate = models.DateField()
    popularity = models.IntegerField()
    rating = models.IntegerField()
    explicit = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Playlist(models.Model):
    playlistID = models.IntegerField(primary_key=True)
    playlistTitle = models.CharField(max_length=20)
    playlistLength = models.TimeField()
    numberOfSongs = models.IntegerField()
    #songs = models.ManyToManyField(Song, through='addToPlaylist')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
