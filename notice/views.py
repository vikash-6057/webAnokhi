
#class view imports
from django.http import HttpResponse
#from django.views.generic import ListView, DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#class views import ends


#either get the post with id or throw 404
#name 'notice' is not defined will show up if 
#below command is not imported

from django.shortcuts import render, redirect, get_object_or_404

from notice.forms import NoticesForm
from django.contrib.auth.decorators import login_required

from .models import Notices

def notices(request):
	notice = Notices.objects
	return render(request, 'notice/noticeall.html',{'notice':notice})

def ndetail(request,notices_id):
	detailnotice=get_object_or_404(Notices, pk=notices_id)
	return render(request,'notice/details.html',{'notice':detailnotice})

#def timetable(request):
#	timetable = Timetable.objects
#	return render(request, 'notice/timetable.html',{'timetable':timetable})

#def timetabledetail(request,timetable_id):
#	detailtable=get_object_or_404(Timetable, pk=timetable_id)
#	return render(request,'notice/timetabledetail.html',{'timetable':detailtable})
def noti(request):
    print("ASDFGTREWQ")  
    if request.method == "POST": 
        print("ASDFGHGFD")
        form = NoticesForm(request.POST) 
        print(form)
        if form.is_valid(): 
            print("INSIDE IF") 
            try:
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = NoticesForm()  
    return render(request,'notice/index.html',{'form':form}) 
def show(request):  
    notices = Notices.objects.all()  
    return render(request,"notice/show.html",{'notices':notices})  
def edit(request, id):  
    notice = Notices.objects.get(id=id)  
    return render(request,'notice/edit.html', {'notice':notice})  
def update(request, id):  
    notices = Notices.objects.get(id=id)  
    form = NoticesForm(request.POST, instance = notices)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'notice/edit.html', {'notices': notices})  
def destroy(request, id):  
    notices = Notices.objects.get(id=id)  
    notices.delete()  
    return redirect("/show")  












