from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from random import choice


from .models import ShortUrl

def check(name):
    unavailable = ShortUrl.objects.all()
    for url in unavailable:
        if url.name == name:
            return True
    return False

def index(request):
    entries = ShortUrl.objects.all()
    return render(request, 'shorter/index.html', {'entries': entries})


def entry(request):
    length = 4
    i = 0
    long = 'http://'
    long += request.POST['url_entry']
    name = request.POST['custom_name_text']
    if name == '':
        while i < length:
            name += choice('abcdefghijklmnopqrstuvwxyz0123456789')
            i += 1
            print(check(name))
            if i == length and check(name):
                i = 0
                name=''
    name = name.lower()
    if check(name):
        return render(request, 'shorter/index.html', {
            'error_message': 'Short URL "%s" already taken, please choose another.' % name
        })
    short = ShortUrl(name=name, long=long)
    short.save()
    return HttpResponseRedirect(reverse('shorter:success', kwargs={'name': name, 'long': long}))

def success(request, name, long):
    entries = ShortUrl.objects.all()
    return render(request, 'shorter/index.html', {'entries': entries, 'name': name, 'long': long})

def go(request, search):
    entries = ShortUrl.objects.all()
    search = search.lower()
    for entered in entries:
        if entered.name == search:
            return render(request, 'shorter/go.html', {'shorty': entered})
    return render(request, 'shorter/index.html', {
        'entries': entries,
        'error_message': 'Short URL "%s" not found in entries.' % search
    })