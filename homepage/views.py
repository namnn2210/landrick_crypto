from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request=request, template_name='index.html')


def about(request):
    return render(request=request, template_name='crypto-about.html')


def market(request):
    return render(request=request, template_name='crypto-market.html')


def token(request):
    return render(request=request, template_name='crypto-token.html')


def services(request):
    return render(request=request, template_name='crypto-services.html')


def faqs(request):
    return render(request=request, template_name='crypto-faqs.html')


def whitepapers(request):
    return render(request=request, template_name='crypto-whitepaper.html')


def blogs(request):
    return render(request=request, template_name='crypto-blog.html')
