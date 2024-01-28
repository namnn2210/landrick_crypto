from django.shortcuts import render, redirect, get_object_or_404
from .models import AskModel, AskCategoryModel
from django.contrib.auth.decorators import login_required
import requests


# Create your views here.
def ask(request):
    list_asks = AskModel.objects.filter(status=1)
    list_asks_category = AskCategoryModel.objects.filter(status=1)
    return render(request=request, template_name='crypto-ask.html',
                  context={'list_ask': list_asks, 'list_asks_category': list_asks_category})


def ask_category(request, slug):
    ask_category_obj = get_object_or_404(AskCategoryModel, slug=slug, status=1)
    ask_by_category = AskModel.objects.filter(category=ask_category_obj)
    print(ask_by_category)
    return render(request=request, template_name='crypto-ask-category.html',
                  context={'ask_category_obj': ask_category_obj, 'ask_by_category': ask_by_category})


@login_required(login_url='login')
def add_ask(request):
    if request.method == 'POST':
        ask_input = request.POST.get('ask', '')
        ask_obj = AskModel(user=request.user, ask=ask_input)
        ask_obj.save()
        return redirect('ask')


def ask_detail(request, slug):
    ask = get_object_or_404(AskModel, slug=slug, status=1)
    list_format_exchanges = get_trending_exchanges()
    return render(request=request, template_name='crypto-ask-detail.html',
                  context={'ask': ask, 'list_format_exchanges': list_format_exchanges})


def get_trending_exchanges():
    list_format_exchanges = []
    url = "https://api.coingecko.com/api/v3/exchanges"

    # Optional: You can specify parameters to customize your request, e.g., per_page and page.
    params = {
        "per_page": 10,  # Number of exchanges per page
        "page": 1,  # Page number
    }

    # Make the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        exchange_data = response.json()
        for item in exchange_data:
            list_format_exchanges.append(
                {'name': item['name'], 'thumb': item['image'], 'trust_score': item['trust_score'],
                 'trust_score_rank': item['trust_score_rank'],
                 'trade_volume_24h_btc': item['trade_volume_24h_btc']})
        return list_format_exchanges
    return None
