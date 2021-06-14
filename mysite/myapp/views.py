from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "title":"CINS465 Hello World",
        "body":"Body",
        "note":"Hover the title for effect!",
    }
    return render(request, "index.html",context=context)