from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist.')
    return render(request, 'polls/index.html', {'question': question})
