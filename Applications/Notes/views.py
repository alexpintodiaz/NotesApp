from django.shortcuts import render, redirect
from .models import NotesApp
from django.contrib import messages

# Create your views here.


def index(request):
    allNotes = NotesApp.objects.all()
    """ messages.success(request, 'Notes listed') """
    return render(request, "gestionNotas.html", {"allNotes": allNotes})


def registerNote(request):
    title=request.POST['txtNote']
    description=request.POST['txtDescription']

    newNote = NotesApp.objects.create(title=title, description=description)
    messages.success(request, 'Note created!')
    return redirect('/')


def editNote(request, title):
    edNote = NotesApp.objects.get(title=title)
    return render(request, "editNotes.html", {"edNote": edNote})


def editingNote(request):
    title=request.POST['txtNote']
    description=request.POST['txtDescription']

    edNote = NotesApp.objects.get(title=title)
    edNote.title = title
    edNote.description = description
    edNote.save()
    messages.success(request, 'Note updated!')
    return redirect('/')

def deleteNote(request, title):
    delNote = NotesApp.objects.filter(title=title)
    delNote.delete()

    messages.success(request, 'Note removed!')

    return redirect('/')

