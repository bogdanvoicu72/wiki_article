from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect
from django.http import HttpResponse
from   pyzbar.pyzbar import decode
from PIL import Image
from django.contrib import messages
from  .forms import HashCode
import blockchain
import dbConnect
import pymongo
from django.core.files.storage import FileSystemStorage
from bson import ObjectId
# Create your views here.
from .forms import HashCode,ImageForm
db_name = 'test'
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[db_name]

collection = 'products'
query_collection = db[collection]

def index(request):
    if request.method == 'POST':
        form2 = ImageForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            d = decode(Image.open('/Users/bogdanvoicu/PycharmProjects/BigPlan/media/image/TEST.png'))
            print(d[0].data.decode('ascii'))
            info=d[0].data.decode('ascii')
            what_split = str(info)
            split = what_split.split("and")
            argument1 = split[0]
            argument2 = split[1]
            print(argument1)
            print(argument2)
            q = query_collection.find_one(

                {'_id': ObjectId(str(argument1))}, {'tricou': {
                    '$elemMatch': {'Previous_Hash': str(argument2)

                                   }
                }}

            )
            print(q)
            dict = str(q)
            messages.info(request, dict, extra_tags='safe')

            return  redirect('index',)
    else:
        form2 = ImageForm()
    return render(request,'index.html', {'form2': form2})
#{'form': form},

def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html


def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')