from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

# Create your views here.
def index(request):

    feat1 = Features()
    feat1.id = 1
    feat1.name = "Forex Trading"
    feat1.details = "FOREX fund with an average profit of 5% and a risk of 2%"
    feat1.is_true = True

    feat2 = Features()
    feat2.id = 2
    feat2.name = "Analytics"
    feat2.details = "Test and analyze potential model performance. Overfit avoidance"
    feat2.is_true = True

    feat3 = Features()
    feat3.id = 3
    feat3.name = "Trading Infrastructure"
    feat3.details = "We develop tailored trading infrastructure, to protect you strategy from being snooped"
    feat3.is_true = False

    feat4 = Features()
    feat4.id = 4
    feat4.name = "Trading Infrastructure"
    feat4.details = "We develop tailored trading infrastructure, to protect you strategy from being snooped"
    feat4.is_true = False

    features = [feat1, feat2, feat3, feat4]
    context = {'features':features}

    return render(request, 'index.html', context)

def counter(request):
    text = request.GET['text']
    words = len(text.split(" "))
    context = {'words' : words}

    return render(request, 'counter.html',context)

def counter_post(request):
    text = request.POST['text']
    words = len(text.split(" "))
    context = {'words' : words}

    return render(request, 'counter.html',context)
