from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util

from random import choice
import markdown2

#


#
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

def random(request):
    return redirect(reverse("entry", kwargs={

        "title":choice(util.list_entries())

    }))

def search(request, query):

    if request.method == "POST":
        value = request.POST["search_query"]
        list_names = util.list_entries()
        if value in list_names:
            cont = markdown2.markdown(util.get_entry(value))
            return render(request, "encyclopedia/entry.html", {

                'content':cont,
                'title':value

            })
        else:
            controlList = []
            check = False
            for item in list_names:
                #check if the char of value is in list
                if value.lower() in item.lower():
                    controlList.append(item)
                    check = True
            
            return render(request, "encyclopedia/search.html", {

                "controlList":controlList,
                "check":check

            })

        





