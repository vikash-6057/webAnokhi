from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#either get the post with id or throw 404
#name 'notice' is not defined will show up if 
#below command is not imported

#class based imports

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#class based imports

from .models import Gallery 
from .models import Events
from .models import Program
#class based views for events




class EventList(ListView):
    model = Events

class EventView(DetailView):
    model = Events

class EventCreate(CreateView):
    model = Events
    fields = ['title', 'decription']
    success_url = reverse_lazy('event_list')

class EventUpdate(UpdateView):
    model = Events
    fields = ['title', 'decription']
    success_url = reverse_lazy('event_list')

class EventDelete(DeleteView):
    model = Events
    success_url = reverse_lazy('event_list')

#class based views ends

def past(request):
	past = Events.objects.filter(published_date__lte=timezone.now())
	return render(request, 'event/past.html',{'past':past})

def upcoming(request):
	upcoming = Events.objects.filter(published_date__gt=timezone.now())
	return render(request, 'event/upcoming.html',{'upcoming':upcoming})


def detail(request,past_id):
	#pastdetail=get_object_or_404(Events, pk=past_id)
	p= Events.objects.get(pk=past_id)
	return render(request,'event/detail.html',#{'pastdetail':pastdetail}
		{'image':p})


@login_required
def addevent(request):
    if request.method == 'POST':
        ev = Events()
        ev.title = request.POST['title']
        ev.decription = request.POST['desc']
        ev.published_date = request.POST['date']
        ev.image = request.FILES['image']
        ev.save()
    ev = Events.objects.all()
    return render(request, 'event/addevent.html', {'event': ev})


@login_required
def deleteevent(request, ev_id):
    event = get_object_or_404(Events, pk=ev_id)
    event.delete()
    return redirect('event:addevent')

@login_required
def addimage(request):
    if request.method == 'POST':
        im = Gallery()
        im.image = request.FILES['image']
        event = request.POST['event']
        im.category = get_object_or_404(Events, title=event)
        im.save()
    im = Gallery.objects.all()
    events = Events.objects.all()
    return render(request, 'event/addimage.html', {'image': im, 'events': events})

@login_required
def deleteimage(request, ev_id):
    event = get_object_or_404(Gallery, pk=ev_id)
    event.delete()
    return redirect('event:addimage')

@login_required
def addpro(request):
    if request.method == 'POST':
        im = Program()
        im.image = request.FILES['image']
        im.description = request.POST['desc']
        im.title = request.POST['title']
        im.date = request.POST['date']
        im.save()
    im = Program.objects.all()
    return render(request, 'event/addpro.html', {'prog': im})

@login_required
def deletepro(request, ev_id):
    event = get_object_or_404(Program, pk=ev_id)
    event.delete()
    return redirect('event:addpro')



def program(request):
	past = Program.objects.all()
	return render(request, 'event/program.html',{'program':past})