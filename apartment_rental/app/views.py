from django.shortcuts import render, redirect, get_object_or_404
from .models import People
from .forms import PeopleForm


def people_list(request):
    people = People.objects.all()
    return render(request, 'people_list.html', {'people': people})


def people_detail(request, pk):
    people = get_object_or_404(People, pk=pk)
    return render(request, 'people_detail.html', {'people': people})


def people_create(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people_list')
    else:
        form = PeopleForm()
    return render(request, 'people_form.html', {'form': form})


def people_edit(request, pk):
    people = get_object_or_404(People, pk=pk)
    if request.method == 'POST':
        form = PeopleForm(request.POST, instance=people)
        if form.is_valid():
            form.save()
            return redirect('people_list')
    else:
        form = PeopleForm(instance=people)
    return render(request, 'people_form.html', {'form': form})



def people_delete(request, pk):
    people = get_object_or_404(People, pk=pk)
    if request.method == 'POST':
        people.delete()
        return redirect('people_list')
    return render(request, 'people_confirm_delete.html', {'people': people})
