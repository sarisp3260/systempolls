from django.contrib import admin
from .models import Answers, Poll, Votes


# Register your models here.
admin.site.register(Answers)
admin.site.register(Poll)
admin.site.register(Votes)