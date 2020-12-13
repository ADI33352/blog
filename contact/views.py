from django.shortcuts import render
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']

    return render(request, 'contact.html')
