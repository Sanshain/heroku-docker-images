import time
from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest

from .services.signs import get_sign


# Create your views here.
def get_sign_to_globe(request: HttpRequest):
    start = time.monotonic()
    try:        
        _date = datetime.strptime(request.GET.get('date'), r'%Y-%m-%d')
    except Exception as ex:
        return HttpResponseBadRequest('неправильный формат: %s' % ex)
    sign = get_sign(_date)
    
    print(time.monotonic() - start)
    return HttpResponse(sign)

def check(request):
    return render(request, 'base.html')