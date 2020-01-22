from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Page

# Create your views here.

def index(request):
    pages_list = Page.objects.order_by('-pub_date')[:5]
    context = {'pages_list' : pages_list }
    return render(request, 'testsite/index.html', context)

def page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'testsite/page.html', {'page':page})

