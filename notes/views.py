from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.shortcuts import render
from .models import NotesData
from .forms import NoteForm
# Create your views here.
 
@login_required(login_url='/login/')
def home(request):
    context={}
    if request.user.is_authenticated:
        notes = NotesData.objects.filter(user=request.user)
        context['notes']=notes
        form = NoteForm(request.POST or None)
        context['form']=form
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.user=request.user
            save_it.save()
    return render(request, 'notes/note.html', context)


class NotesDeleteView(DeleteView):
    model=NotesData
    success_url = reverse_lazy('notes')

