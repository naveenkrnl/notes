from django.urls import path, include
from .views import home, NotesDeleteView

urlpatterns = [
    path('notes/', home, name='notes'),
    path('<pk>/delete/', NotesDeleteView.as_view(), name='notes_delete'),
]
