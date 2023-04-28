from django.shortcuts import render

# Create your views here.

import datetime
def Filter_inbuilt(request):
    x=datetime.datetime.now()
    d={'data':'Hai This Is AchyuthKumar','x':x,'a':1,'b':2}
    return render(request,'Filter_inbuilt.html',d)