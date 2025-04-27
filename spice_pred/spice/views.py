from functools import reduce
from itertools import product
from multiprocessing import reduction
from django.shortcuts import render
from django.http import HttpResponse
import pickle
import os
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR,'spice_model.pkl')
with open(model_path,'rb')as file:
    model=pickle.load(file)


# Create your views here.
def home(request):
    result=None
    if request.method == "POST":
        dom=float(request.POST['dom'])
        area=float(request.POST['area'])
        item=float(request.POST['item'])
        year=float(request.POST['year'])
        imp=float(request.POST['imp'])
        exp=float(request.POST['exp'])
        prod=float(request.POST['prod'])
        input_data = [[dom, area, item, year, imp, exp, prod]]
        prediction = model.predict(input_data)
        result = prediction[0] 
    context= {
            "product": result
        }       
    return render (request,"index.html",context)