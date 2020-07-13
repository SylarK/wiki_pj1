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

def new(request):

    #the first time, open a default page
    if request.method == 'GET':
        return render(request, "encyclopedia/new_page.html")
    
    #after, we use the data for create a new page
    else :
        title = request.POST['title_page']
        cont = request.POST['text_page']

        #check if the title already exists
        
        if(util.get_entry(title)):
            msg = "Sorry, but a entry with the same name already exists in the database. Search the entry or change the title."

            return render(request, "encyclopedia/error.html", {

                "msg":msg

            })
        else:
            util.save_entry(title, cont)
            
            return redirect(reverse("entry", kwargs={

                "title":title

            }))

        


        





