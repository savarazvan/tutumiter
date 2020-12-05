from django.db import models

class Country(models.Model):
    name = models.CharField(max_length = 35)
    tags = models.CharField(max_length = 70, default = '',null=True, blank=True)
    advices = models.CharField(max_length = 4000)
    open_for_f = models.CharField(max_length = 7)
    open_for_t = models.CharField(max_length = 7)
    quarantine = models.CharField(max_length = 7)

    def __str__(self):
        return self.name


class Atraction(models.Model):
    title = models.CharField(max_length = 50)
    text = models.CharField(max_length = 1000)
    tags = models.CharField(max_length = 50, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title