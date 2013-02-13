# Create your views here.
import os
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext

def index(request):
    template = loader.get_template('swissmap/index.html')
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__)+ '/..')
    text =  os.path.join(PROJECT_DIR, 'media')
    context = Context({
        'welcome': text,
        })

    return render_to_response('swissmap/index.html', {'welcome': "SWISS MAP" }, RequestContext(request));
    # return HttpResponse(template.render(context))