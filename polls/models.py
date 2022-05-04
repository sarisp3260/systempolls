
from django.db import models

class Poll(models.Model):
    question = models.TextField()
    #option_one = models.CharField(max_length=30)
    #option_two = models.CharField(max_length=30)
    #option_three = models.CharField(max_length=30)
    #option_one_count = models.IntegerField(default=0)
    #option_two_count = models.IntegerField(default=0)
    #option_three_count = models.IntegerField(default=0)

    #def total(self):
    #    return self.option_one_count + self.option_two_count + self.option_three_count

class Answers(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option= models.CharField(max_length=30)

    def __str__(self):
        return self.option

    def get_votes(self):
        return Votes.objects.filter(answer=self).count()

class Votes(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)

    def get_total(self):
        return Votes.objects.all().count()

    
