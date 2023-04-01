from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
import numpy as np

# Create your views here.

#model object 
model = load('.\model.joblib')
def index(request):
    if request.method == 'POST':
        #forms input 
        no_of_athletes = request.POST.get("athletes")
        prev_medals = request.POST.get("prev_medal")
        #coversion of integer to float
        data = np.array([no_of_athletes,prev_medals], dtype=float)
        #prediction of medals
        result = model.predict([data])
        #editing the answer
        s = str(result[0])
        if int(s[s.index('.')+1]) <= 5:
            result = s[:s.index('.')]
        else:
            result = int(s[:s.index('.')]) + 1
        #return the answer to result.html
        return render(request, "result.html",{'result':result})
        
    return render(request,'form.html') 


    