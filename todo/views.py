from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.utils import timezone

from .models import ItemToBuy
from .forms import AddItemForm


def index(request):
    return HttpResponseRedirect("/todo")


def tasks_list(request):
    items = ItemToBuy.objects.all()
    return render(request, 'todo/index.html', {'items': items})


def add_new_item(request):
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = AddItemForm()
    return render(request, 'todo/add_new.html', {'form': form})
