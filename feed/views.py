from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(request=request, template_name='feed-list.html')

def feed_detail(request):
    return render(request=request, template_name='feed-detail.html')