from django import template
from .models import UpDownVotesAnswer, UpDownVotesQuestion

register = template.Library()
 
 
def updown_ans(ans, updown):
    return UpDownVotesAnswer.objects.filter(answer_id=ans, up_down=updown).count()

def updown_question(question, updown):
    return UpDownVotesQuestion.objects.filter(question_id=question, up_down=updown).count()

def calculate_score(user):
    q_up = UpDownVotesQuestion.objects.filter(question_id__user_id=user, up_down=1).count()
    q_down = UpDownVotesQuestion.objects.filter(question_id__user_id=user, up_down=0).count()
    a_up = UpDownVotesAnswer.objects.filter(answer_id__user_id=user, up_down=1).count()
    a_down = UpDownVotesAnswer.objects.filter(answer_id__user_id=user, up_down=0).count()
    return ((q_up+a_up)*1.5) - ((q_down+a_down)*2)


register.filter('calculate_score',calculate_score)
register.filter('updown_ans',updown_ans)
register.filter('updown_question',updown_question)				