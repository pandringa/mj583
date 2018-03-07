from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# GET /polls
class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions."""
    return Question.objects.filter(
      pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

# GET /polls/<id>
class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'
  def get_queryset(self):
    """
    Excludes any questions that aren't published yet.
    """
    return Question.objects.filter(pub_date__lte=timezone.now())

# GET /polls/<id>/results
class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

# POST /polls/<id>/vote
def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice.",
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))