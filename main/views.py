from acct.models import User,Profile
from django.shortcuts import render, redirect
from .forms import ContactForm, SubscribeForm
from project.utils import query_all, filter_query,get_object
from main.models import Portfolio, PortfolioCategory, Service, Client, Featured

# Create your views here.
def home_view(request):
    obj = {
        'client' : query_all(Client),
        'service' : query_all(Service),
        'featured' : query_all(Featured),
        'portfolio' : query_all(Portfolio),
        'category' : query_all(PortfolioCategory),
        'category' : query_all(PortfolioCategory),
        'team' : filter_query(Profile, team_member=True),
    }
    return render(request, 'main/index.html',obj)


def portfolio_view(request, id):
    return render(request, 'main/portfolio.html', {'portfolio': get_object(Portfolio, id=id)})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return redirect('home')
    
def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return redirect('home')
