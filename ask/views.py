from django.shortcuts import render, redirect
from .models import AskModel


# Create your views here.
def ask(request):
    list_asks = AskModel.objects.filter(status=1)
    return render(request=request, template_name='crypto-ask.html', context={'list_ask': list_asks})


def add_ask(request):
    if request.method == 'POST':
        ask_input = request.POST.get('ask', '')
        ask_obj = AskModel(user=request.user, ask=ask_input)
        ask_obj.save()
        return redirect('ask')
