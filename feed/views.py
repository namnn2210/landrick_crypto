from django.shortcuts import render, redirect
from .models import FeedModel, FeedCommentModel
from django.core.paginator import Paginator
from urllib.parse import urlparse


# Create your views here.
def feed(request):
    list_feeds = FeedModel.objects.filter(status=1).order_by('-created_at')
    items_per_page = 10
    paginator = Paginator(list_feeds, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request=request, template_name='feed-list.html', context={'page': page})


def feed_detail(request, slug):
    current_url = request.build_absolute_uri()
    parsed_url = urlparse(current_url)
    domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
    feed_obj = FeedModel.objects.get(slug=slug, status=1)
    feed_comments = FeedCommentModel.objects.filter(feed=feed_obj, status=1).order_by('-created_at')
    if feed_obj.hashtags is not None or feed_obj.hashtags != '':
        hashtags = feed_obj.hashtags.split(',')
    else:
        hashtags = None
    return render(request=request, template_name='feed-detail.html',
                  context={'feed': feed_obj, 'comments': feed_comments, 'domain': domain, 'hashtags': hashtags})


def add_comment(request, slug):
    if request.method == 'POST':
        feed_obj = FeedModel.objects.get(slug=slug, status=1)
        feed_comment = FeedCommentModel(feed=feed_obj, comment=request.POST['comment'])
        feed_comment.save()
        return redirect('feed_detail', slug=slug)
