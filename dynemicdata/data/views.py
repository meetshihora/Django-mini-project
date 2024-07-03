from django.shortcuts import render
from data.models  import Data
# Create your views here.

def data(request):
    datadetail = Data.objects.all().order_by('roll')
    data = {'datadetail': datadetail}

    return(render(request, 'data.html', data))