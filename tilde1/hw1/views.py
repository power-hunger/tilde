
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import Person, Action
from .forms import NameForm, ActionForm


class IndexView(generic.ListView):
    template_name = 'hw1/index.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()


def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        action_list = Action.objects.filter(person_id=person_id)
        balance = 0
        for entry in action_list:
            balance = balance + int(entry.amount)

    except Person.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'hw1/detail.html', {'person': person, 'balance': balance}, )


def registration(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            person_name = form.cleaned_data['your_name']
            Person(person_id=person_name).save()
    return HttpResponseRedirect('/hw1/')


def action(request, person_id):
    if request.POST:
        form = ActionForm(request.POST)

        if form.is_valid():
            operation = form.cleaned_data['action']
            size = form.cleaned_data['amount']
            if operation == "Lend":
                size = -size
            Action(person_id=person_id, action=operation, amount=size).save()
    return HttpResponseRedirect('/hw1/')






