from django.shortcuts import render
from .models import Destination
from django.contrib import messages
from django.core.mail import send_mail
def index(request):

    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

#suchen
def fetchdata(request) :

    data=Destination.objects.all()
    if request.method == 'POST':
        srh=Destination.objects.filter(name__iexact=request.POST['City'] ,
                                       start=request.POST['Departure'],
                                       end=request.POST['Arrival'],
                                       price=request.POST['Budget'],
                                       )

        cnt={'srh':srh}
        if not srh :
            messages.info(request, 'no resault found ')


    return render(request,'news.html',cnt)




def contactus(request):
    if request.method=='POST' :
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        #'send from ' +" "+name+ "\n" +message
        message1 = "{} from {}".format(message,name)



        send_mail(subject,message1,'zaherabb12@gmail.com',[email],fail_silently=False)

        return render(request,'contact.html',{'name':name})

    return render(request,'contact.html')



# def newsletter(request):
#     if request.POST =='POST':
#         pass
#     return