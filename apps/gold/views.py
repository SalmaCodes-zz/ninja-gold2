from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime


# Create your views here.


# '/' root page.
def index(request):
    if 'gold' not in request.session.keys():
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'gold/index.html')


# '/process_money' handles POST data when location/gold forms are submitted.
def process_money(request):
    golds = 0
    time = strftime("%Y/%m/%d %H:%M %p", gmtime())
    if request.POST['building'] == 'farm':
        golds = random.randrange(10, 21)
        request.session['activities'].append({
            'message': "Earned {} golds from the Farm! ({})".format(golds, time),
            'color': 'green'
        })
    elif request.POST['building'] == 'cave':
        golds = random.randrange(5, 11)
        request.session['activities'].append({
            'message': "Earned {} golds from the Cave! ({})".format(golds, time),
            'color': 'green'
        })
    elif request.POST['building'] == 'house':
        golds = random.randrange(2, 6)
        request.session['activities'].append({
            'message': "Earned {} golds from the House! ({})".format(golds, time),
            'color': 'green'
        })
    elif request.POST['building'] == 'casino':
        golds = random.randrange(-50, 51)
        if golds >= 0:
            request.session['activities'].append({
                'message': "Earned {} golds from the Casino! ({})".format(golds, time),
                'color': 'green'
            })
        else:
            request.session['activities'].append({
                'message': "Entered a Casino and lost {} golds... Ouch... ({})".format(abs(golds), time),
                'color': 'red'
            })

    request.session['gold'] += golds

    return redirect('/')


# '/reset' handles POST data when 'reset' button is clicked.
def reset(request):
    request.session.pop('gold')
    return redirect('/')


