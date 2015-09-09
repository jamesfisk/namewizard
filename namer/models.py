from django.db import models


class Matrix(models.Model):
    gender = models.CharField(max_length=1)
    year = models.IntegerField(default=0)

    probability_matrix = models.TextField()
    pi = models.TextField()

    def __str__(self):
        return self.gender + str(self.year)
