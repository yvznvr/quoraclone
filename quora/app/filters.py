from django import template
from .models import UpDownVotesAnswer

register = template.Library()
 
 
def updown_ans(ans, updown):
    return UpDownVotesAnswer.objects.filter(answer_id=ans, up_down=updown).count()

 
register.filter('updown_ans',updown_ans)