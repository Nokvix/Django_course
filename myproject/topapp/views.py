from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note, Company


def fullname(request):
    notes = [f'{note.title} {note.text}; ' for note in Note.objects.all()]
    return HttpResponse(notes)


def poem(request):
    companies = [f'{company.name} {company.owner} {company.date_foundation}; ' for company in Company.objects.all()]
    return HttpResponse(companies)


def add_note(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    note = Note(title=title, text=text)
    note.save()

    return redirect('index')
