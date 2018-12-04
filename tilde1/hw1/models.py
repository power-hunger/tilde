from django.db import models


class Person(models.Model):
    person_id = models.CharField(max_length=200)

    def __str__(self):
        return self.person_id


class Action(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)


