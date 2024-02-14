from django.shortcuts import render, redirect, get_object_or_404
from .models import AskModel, AskCategoryModel, AdminAskRatingModel
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import F, ExpressionWrapper, FloatField
import requests


# Create your views here.
def ask(request):
    list_asks = AskModel.objects.filter(status=1)
    list_asks_category = AskCategoryModel.objects.filter(status=1)
    queryset = AdminAskRatingModel.objects.filter(status=True).annotate(
        rating_per_count=ExpressionWrapper(
            F('rating') / F('rating_count'),
            output_field=FloatField()
        )
    )
    queryset = queryset.order_by('-rating_per_count')
    top_3_users = queryset[:3]
    for item in top_3_users:
        print(item.rating_per_count)
    return render(request=request, template_name='crypto-ask.html',
                  context={'list_ask': list_asks, 'list_asks_category': list_asks_category, 'top_admin': top_3_users})


def ask_category(request, slug):
    ask_category_obj = get_object_or_404(AskCategoryModel, slug=slug, status=1)
    pinned_asks = AskModel.objects.filter(category=ask_category_obj, pinned=True)
    other_asks = AskModel.objects.filter(category=ask_category_obj, pinned=False)
    ask_by_category = list(pinned_asks) + list(other_asks)
    list_asks_category = AskCategoryModel.objects.filter(status=1)
    return render(request=request, template_name='crypto-ask-category.html',
                  context={'ask_category_obj': ask_category_obj, 'ask_by_category': ask_by_category,
                           'list_asks_category': list_asks_category})


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
    list_asks_category = AskCategoryModel.objects.filter(status=1)
    return render(request=request, template_name='crypto-ask-detail.html',
                  context={'ask': ask, 'list_format_exchanges': list_format_exchanges,
                           'list_asks_category': list_asks_category})


def rate_ask(request):
    if request.method == 'POST':
        ask_id = request.POST.get('askId')
        rating = request.POST.get('rating')

        print('****************', ask_id, rating)

        ask = get_object_or_404(AskModel, pk=ask_id, status=1)
        try:
            admin_ask = AdminAskRatingModel.objects.get(user=ask.user, status=True)
            admin_ask.rating += rating
            admin_ask.rating_count += 1
        except AdminAskRatingModel.DoesNotExist:
            admin_ask = AdminAskRatingModel(user=ask.user, rating=rating, rating_count=1)
        admin_ask.save()
        ask.rating += rating
        ask.rating_count += 1
        ask.save()
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
