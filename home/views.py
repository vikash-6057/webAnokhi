from turtle import back
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    news = News.objects.all()
    return render(request, 'home/home.html', {'news': news})


def achieve(request):
	return render(request, 'home/achieve.html')


def contact(request):
	return render(request, 'home/contact.html')


def antyodaya(request):
	return render(request, 'home/antyodaya.html')


def evening(request):
	time = Evening.objects.filter(type=True)
	list = Evening.objects.filter(type=False)
	return render(request, 'home/evening.html',{'time': time, 'list': list})


@login_required
def add_list(request):
	if request.method == 'POST':
		n = Evening()
		n.title = request.POST['title']
		n.file = request.FILES['file']
		n.type = request.POST['type']
		n.save()
	pdf = Evening.objects.all()
	return render(request, 'home/addlist.html',{'pdf': pdf})


@login_required
def del_list(request,pk):
	pdf = get_object_or_404(Evening, pk=pk)
	pdf.delete()
	pdf = Evening.objects.all()
	return render(request, 'home/addlist.html', {'pdf': pdf})


@login_required
def add_news(request):
	if request.method == 'POST':
		n = News()
		n.title = request.POST['title']
		n.desc = request.POST['desc']
		n.pic = request.FILES['image']
		n.date = request.POST['date']
		n.save()
		return render(request, 'home/home.html')
	else:
		news = News.objects.all()
		return render(request, 'home/news.html', {'news': news})


@login_required
def del_news(request, news_id):
	new = get_object_or_404(News, pk=news_id)
	new.delete()
	return render(request, 'home/home.html')


@login_required
def add_team(request):
	if request.method == 'POST':
		n = Team()
		n.title = request.POST['title']
		n.description = request.POST['desc']
		n.image = request.FILES['im']
		n.batch = request.POST['batch']
		n.save()
	news = Team.objects.all()
	return render(request, 'home/addteam.html', {'team': news})


@login_required
def del_team(request, team_id):
	new = get_object_or_404(Team, pk=team_id)
	new.delete()
	return redirect('add_team')


def team(request):
	te = Team.objects.all()
	final_year = Team.objects.filter(batch='Final')
	third_year = Team.objects.filter(batch='Third')
	alumni_First = Alumni.objects.filter(batch='First')
	alumni_Second = Alumni.objects.filter(batch='Second')
	return render(request, 'home/team.html', {'team': te,'final':final_year,'third':third_year,'alumni_First':alumni_First,'alumni_Second':alumni_Second})


def admin_home(request):
    return render(request, 'home/adminhome.html')


def connect(request):
	if request.method == 'POST':
		member = Member.objects.all()
		for x in member:
			print("APM" + str(x.id))
			if "APM" + str(x.id) != request.POST['mem']:
				continue

			else:
				n = Volunteer()
				n.description = request.POST['desc']
				n.mem_id = request.POST['mem']
				n.type = request.POST['type']
				n.date = request.POST['date']
				n.save()
				messages.success(request,
								 f'We will contact you soon once your request for being Volunteer in accepted.')
				return render(request, 'home/home.html')
				print("success")
				break

		messages.success(request, f'You are not in our members list.')
	return render(request, 'home/connect.html')


@login_required
def deletecon(request, con_id):
    con = get_object_or_404(Volunteer, pk=con_id)
    con.delete()

    return redirect('allconnect')


@login_required
def allconnect(request):
    don = Volunteer.objects.all()
    return render(request, 'home/allconnect.html', {'connect': don})


@login_required
def allmember(request):
    don = Member.objects.all()
    return render(request, 'home/allmember.html', {'member': don})


def addmember(request):
	n = Member()
	n.name = request.POST['name']
	n.about = request.POST['about']
	n.mob = request.POST['mob']
	n.mail = request.POST['mail']
	n.loc = request.POST['loc']
	n.batch = request.POST['batch']
	n.alum = request.POST['alum']
	n.save()
	mem = get_object_or_404(Member, mob=n.mob)
	messages.success(request, f'Your membership id: APM{ mem.pk }')
	return render(request, 'home/connect.html')


@login_required
def delmem(request, mem_id):
	con = get_object_or_404(Member, pk=mem_id)
	con.delete()
	return redirect('allmember')