from django import forms
from .models import NotesData
 
class NoteForm(forms.ModelForm):
    class Meta:
        model = NotesData
        fields=["text"]