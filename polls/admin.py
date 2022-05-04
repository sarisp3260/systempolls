from django.contrib import admin
from .models import Answers
from .models import Poll
from .models import votes

# Register your models here.
admin.site.register(Answers)
admin.site.register(Poll)
admin.site.register(votes)