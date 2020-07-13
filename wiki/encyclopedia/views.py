from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


import random
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    #check if is not empty
    if util.get_entry(title):
        cont = markdown2.markdown(util.get_entry(title))
    else:
        cont = ""
    return render(request, "encyclopedia/entry.html", {

        'content':cont,
        'title':title

    })

def randomic(request):
    title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry", kwargs={"title":title}))


