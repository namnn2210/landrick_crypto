from django.shortcuts import render, redirect, get_object_or_404
from .models import AskModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def ask(request):
    list_asks = AskModel.objects.filter(status=1)
    return render(request=request, template_name='crypto-ask.html', context={'list_ask': list_asks})

@login_required(login_url='login')
def add_ask(request):
    if request.method == 'POST':
        ask_input = request.POST.get('ask', '')
        ask_obj = AskModel(user=request.user, ask=ask_input)
        ask_obj.save()
        return redirect('ask')


def ask_detail(request, ask_id):
    ask = get_object_or_404(AskModel, pk=ask_id)
    return render(request=request, template_name='crypto-ask-detail.html', context={'ask': ask})
