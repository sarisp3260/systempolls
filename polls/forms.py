from django.forms import ModelForm

from .models import Poll, Answers

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['id','question']

class CreateAnswerForm(ModelForm):
    class Meta:
        model = Answers
        fields = ['id','poll','option']