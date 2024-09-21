from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Profile(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)


class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)



