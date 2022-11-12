from django.shortcuts import render
from django.http import HttpResponse
from scripts.reddit_part import get_opinion

def home(request):
    context = {}
    if request.method == 'GET':
        name = request.GET.get('name')
        subbredit = request.GET.get('subreddit')
        if name and subbredit:
            sentiment, examples = get_opinion(name, subbredit)

            context['sentiment'] = sentiment
            context['examples'] = examples
        
    return render(request, 'home.html', context)

def handel_not_found(request, exception):
    return render(request, 'not_found.html')