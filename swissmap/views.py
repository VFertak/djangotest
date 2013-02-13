# Create your views here.
import os
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader

def index(request):
    template = loader.get_template('swissmap/index.html')
    text =  os.path.join(os.path.dirname(__file__),'media').replace('\\','/');#'welcome to the hell';
    context = Context({
        'welcome': text,
        })

    return render_to_response('swissmap/index.html', ['welcome']);
    # return HttpResponse(template.render(context))