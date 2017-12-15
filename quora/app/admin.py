from django.contrib import admin
from .models import *


admin.site.register(Answers)
admin.site.register(Questions)
admin.site.register(Tags)
admin.site.register(SubAnswers)
admin.site.register(UpDownVotesAnswer)
admin.site.register(UpDownVotesQuestion)
