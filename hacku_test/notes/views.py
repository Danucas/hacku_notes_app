from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from . import forms


def notes_endpoint(request):
    if request.method == "POST":
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=True)
            notes = models.Note.objects.order_by("created_at")
            return HttpResponseRedirect(
                f"/notes?success={new_note.id}"
            )
    else:
        form = forms.NoteForm()
        notes = models.Note.objects.order_by("-created_at")
        return render(
            request,
            "note_form.html",
            {"form": form, "notes": notes, "success": request.GET.get("success")},
        )
