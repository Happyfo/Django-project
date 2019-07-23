from django.shortcuts import render, get_object_or_404
from .models import Portfolio


def portfolio(request):
    portfolios = Portfolio.objects.all
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})


def detail(request, portfolio_id):
    detail_portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'portfolio/detail.html', {'portfolio': detail_portfolio})


