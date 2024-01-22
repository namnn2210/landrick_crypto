import re

from django.shortcuts import render, get_object_or_404
from .models import BlogModel
from django.core.paginator import Paginator
import requests

from django.db.models import Q


# Create your views here.
def blog(request):
    list_blogs = BlogModel.objects.filter(status=1).order_by('-created_at')
    items_per_page = 10
    paginator = Paginator(list_blogs, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request=request, template_name='crypto-blog.html', context={'page': page})


def get_trending_latest():
    list_format_latest = []
    url = 'https://api.coingecko.com/api/v3/search/trending'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['coins']
        for item in data[:10]:
            price_regex = r'(?<=\$)[0-9,]+\.(?:[0-9]+|<sub title="[0-9]+\.[0-9]+">[0-9]+<\/sub>[0-9]+)'
            price_str = item['item']['data']['price']
            price_match = re.findall(price_regex, price_str)
            price = float(price_match[0].replace(',', ''))
            list_format_latest.append(
                {'name': item['item']['name'], 'thumb': item['item']['thumb'], 'symbol': item['item']['symbol'],
                 'price': price})
        return list_format_latest
    return None


def blog_detail(request, slug):
    blog = get_object_or_404(BlogModel, slug=slug, status=1)
    category = blog.category
    list_related_blogs = BlogModel.objects.filter(category=category).exclude(slug=slug)[:3]
    print(list_related_blogs)
    list_trending_latest = get_trending_latest()
    return render(request, 'crypto-blog-detail.html',
                  {'blog': blog, 'list_format_latest': list_trending_latest, 'list_related_blogs': list_related_blogs})
