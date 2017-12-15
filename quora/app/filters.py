from django import template
from .models import UpDownVotesAnswer, UpDownVotesQuestion

register = template.Library()
 
 
def updown_ans(ans, updown):
    return UpDownVotesAnswer.objects.filter(answer_id=ans, up_down=updown).count()

def updown_question(question, updown):
    return UpDownVotesQuestion.objects.filter(question_id=question, up_down=updown).count()

register.filter('updown_ans',updown_ans)
register.filter('updown_question',updown_question)