# Create your views here.
import os
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext


# import gdata.spreadsheet
# import gdata.spreadsheet.service

def index(request):
    template = loader.get_template('swissmap/index.html')
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__)+ '/..')
    text =  os.path.join(PROJECT_DIR, 'media')
    context = Context({
        'welcome': text,
        })
    # client = gdata.spreadsheet.service.SpreadsheetsService()
    key = '0AqkKy6zvuhNJdDVZeXBjaGtkaDNkdm1hWUR6SWw0aFE'
    # client.email = 'volodymyr.fertak@nzz.ch'
    # client.password = 'rfhfvtkmrf_23'
    # vv = client.GetWorksheetsFeed(key=key,wksht_id=1, projection='full')
    # worksheets_feed = client.GetWorksheetsFeed(key, visibility='public')
    # print_function(worksheets_feed)

    data = {}
    i = 0
    # for entry in worksheets_feed.entry:
    #     data[i] = entry

    return render_to_response('swissmap/index.html', {'welcome': "SWISS MAP",
                                                      'data': data}, RequestContext(request));
    # return HttpResponse(template.render(context))