from django.shortcuts import render
import pyshorteners
from django.contrib import messages
# Create your views here.
def index(request):
    short_url = ''
    url = ''
    if request.method == 'POST':
        url = request.POST.get('url')
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        messages.success(request, 'URL Shortened Successfully !')
        
    contex = {
        'short_url': short_url,
        'url': url
    }
    return render(request, 'index.html', contex)