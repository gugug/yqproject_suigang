# coding=utf-8

from django import forms
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from yuqing.jsondump import *
from yqproject.settings import *
from yuqing.main_run import *
from crawler.class_event import *

# Create your views here.


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


def homepage(request):
    data = dump_time_line()
    # print data
    # data = [{'topic':u'烧鸡公双方了时间','month':4L,'day':30L},{'topic':u'222','month':4L,'day':15L},{'topic':u'111','month':4,'day':1}]
    # data = [{'a':'aaa'},{'b':'bbb'}]
    return render_to_response('index.html', {'data': data})

class SearchForm(forms.Form):
    input_words = forms.CharField(max_length=100)

def network(request):
    if request.method == 'GET':
        print request.GET
    node_data = dump_force()[0]
    edge_data = dump_force()[1]
    return render(request, 'network.html', {'node_data': node_data, 'edge_data': edge_data})


def line_chart(request):
    event_id =''
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            search_words = sf.cleaned_data['input_words']
            event_id = Event().search_topic(search_words)
        else:
            print 'invalid form'
        print event_id

    if event_id == '000':
        return render_to_response('error.html')

    else:
        inc = Increment()
        rows = inc.get_data(event_id)
        event = Event().get_topic_by_id(event_id)
        print 'rows',rows
        print event
        if len(rows) ==0:
            return render(request,'lineChart.html',{'default':True,'event':event['topic']})
        xaxis = str(inc.time_list)
        yaxis = []
        seris_data = str(inc.scale_rate)
        old_file = open(BASE_DIR + '/static/scripts/lineChart.js', 'rw')
        new_file = open(BASE_DIR + '/static/scripts/line_chart.js', 'w+')
        a = old_file.readlines()
        a[40] = a[40].replace('xaxis', xaxis)
        a[71] = a[71].replace('seris_data', seris_data)
        for i in a:
            new_file.write(i)
        return render(request, 'lineChart.html',{'default':False})
