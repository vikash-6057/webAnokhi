from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from home.models import Member
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Donors
from django.contrib import messages
import razorpay
from django.utils import timezone

client = razorpay.Client(auth=("rzp_test_3xUWNIS6fYe00a", "pUZEGcblut9XqCz4MLl6ADtj"))


def donate(request):
    donor = Donors.objects.filter(verified=True)
    return render(request, 'donate.html', {'donors': donor})


@login_required
def verify(request, don_id):
    don = get_object_or_404(Donors, pk=don_id)
    don.verified = True
    don.save()
    don = Donors.objects.all()
    return redirect('viewdon')


@login_required
def deletedon(request, don_id):
    don = get_object_or_404(Donors, pk=don_id)
    don.delete()
    don = Donors.objects.all()
    return redirect('viewdon')


@login_required
def viewdon(request):
    don = Donors.objects.all()
    return render(request, 'donors.html', {'donors': don})




def payment(request, don_id):


    if request.method == 'POST':
        payment_id = request.POST['razorpay_payment_id']
        username = request.user.username
        print("Making new payment")
        razor_payment = client.payment.fetch(payment_id)
        print(razor_payment)

        print(amount)
        member = get_object_or_404(Donors, pk=don_id)

        context = {'title': "Success!", 'success': True, 'payment_id': "{}".format(payment_id)}
        if not razor_payment.get('status') == 'failed':
            member.tran_id = razor_payment['id']
            member.verified = True
            member.save()
        else:

            context['success'] = False

        return render(request, 'status.html', context=context)


def amount(request):
    if request.method == 'POST':
        member = Member.objects.all()
        for x in member:
            print("APM" + str(x.id))
            if "APM" + str(x.id) != request.POST['mem']:
                continue

            else:
                amount = request.POST['amount']
                mem = request.POST['mem']
                mess = request.POST['mess']
                key = "rzp_test_3xUWNIS6fYe00a"
                order_currency = 'INR'
                amount = int(amount)
                amount = amount * 100
                print(amount)
                mem = mem[3:]
                mem = int(mem)
                member = get_object_or_404(Member, pk=mem)
                user = member.name
                mob = member.mob
                mail = member.mail
                don = Donors()
                don.name = user
                don.mode = "razorpay"
                don.mob = mob
                don.message = mess
                don.amount = amount / 100
                don.date = timezone.datetime.now()
                don.mem_id = "APM" + str(mem)
                don.save()
                donor = Donors.objects.last()
                print(donor)
                don_id = donor.id
                context = {
                    'title': "PAYMENT",
                    'user': user,
                    'key_id': key,
                    'currency': order_currency,
                    'mob': mob,
                    'mess': mess,
                    'mail': mail,
                    'don_id': don_id,
                    'user_id': don.mem_id,
                    'amount': amount
                }
                return render(request, 'payment.html', context=context)

        messages.success(request, f'You are not in our members list.')
    return render(request, 'donate.html')

