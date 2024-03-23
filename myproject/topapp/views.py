from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note, Company
from .forms import ModelForm


def fullname(request):
    notes = [f'{note.title} {note.text}; ' for note in Note.objects.all()]
    return HttpResponse(notes)


def poem(request):
    companies = [f'{company.name} {company.owner} {company.date_foundation}; ' for company in Company.objects.all()]
    return HttpResponse(companies)


def create_record(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)

        title = request.POST.get('title')
        text = request.POST.get('text')
        note = Note(title=title, text=text)
        note.save()
        print('success')
    else:
        form = ModelForm()

    return render(request, 'add_note.html', {'form': form})


def add_note(request):
    return redirect('create_record')
