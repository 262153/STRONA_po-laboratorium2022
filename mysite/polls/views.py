from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Type, Meals, Review


class TypeView(generic.ListView):
    template_name = 'polls/type_list.html'
    context_object_name = 'type_list'
    def get_queryset(self):
        return Type.objects.all()


class MealsView(generic.ListView):
    template_name = 'polls/meals.html'
    context_object_name = 'meals_list'
    def get_queryset(self):
        return Meals.objects.filter(type__type_name=self.kwargs['type_name']).all()

class IngredientsView(generic.DetailView):
    model = Meals
    template_name = 'polls/ingredients.html'


class ReviewView(generic.DetailView):
    model = Meals
    template_name = 'polls/review.html'
    context_object_name = 'review'
    def get_queryset(self):
        return Meals.objects.filter(pk=self.kwargs['pk']).all()


def on_vote(request, meals_id):
    on = get_object_or_404(Meals, pk=meals_id)
    try:
        selected_choice = on.review_set.get(pk=request.POST['choice'])
    except (KeyError, Review.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/ingredients.html', {
            'meals': on,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:review', args=(on.id,)))