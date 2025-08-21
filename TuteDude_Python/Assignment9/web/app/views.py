from django.shortcuts import render, redirect
from app.forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()  # Clear the form after saving
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})