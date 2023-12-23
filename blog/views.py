from django.shortcuts import render, get_object_or_404
from .models import BlogModel
from django.core.paginator import Paginator


# Create your views here.
def blog(request):
    list_blogs = BlogModel.objects.filter(status=1)
    items_per_page = 10
    paginator = Paginator(list_blogs, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request=request, template_name='crypto-blog.html', context={'page': page})


def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogModel, pk=blog_id, status=1)
    return render(request, 'crypto-blog-detail.html', {'blog': blog})
