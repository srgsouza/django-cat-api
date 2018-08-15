from django.shortcuts import render, redirect

from .models import Cat
from .forms import CatForm

## API-related imports
from rest_framework import generics
from .serializers import CatSerializer

# Decorator.  Gets called before a function that has '@login_required' preceeding it.  
from django.contrib.auth.decorators import login_required

class CatList(generics.ListCreateAPIView):
  queryset = Cat.objects.all()
  serializer_class = CatSerializer

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cat.objects.all()
  serializer_class = CatSerializer


############################### CAT ###############################

# @login_required
def cat_list(request):
  cats = Cat.objects.all()
  return render(request, 'tunr/cat_list.html', {'cats': cats})

# Cat Show
# @login_required
def cat_detail(request, pk):
  cat = Cat.objects.get(id=pk)
  return render(request, 'tunr/cat_detail.html', {'cat': cat})

# Cat Create
# @login_required
def cat_create(request):
  if request.method == 'POST':
    form = CatForm(request.POST)
    if form.is_valid():
      cat = form.save()
      return redirect('cat_detail', pk=cat.pk)
  else:
    form = CatForm()
  return render(request, 'tunr/cat_form.html', {'form': form})

# Cat Edit

def cat_edit(request, pk):
  cat = Cat.objects.get(pk=pk)
  if request.method == 'POST':
    form = CatForm(request.POST, instance=cat)
    if form.is_valid():
      cat = form.save()
      return redirect('cat_detail', pk=cat.pk)
  else:
    form = CatForm(instance=cat)
  return render(request, 'tunr/cat_form.html', {'form': form})

# Cat Delete

def cat_delete(request, pk):
  Cat.objects.get(id=pk).delete()
  return redirect('cat_list')
