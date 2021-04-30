from django.http import HttpResponse
from django.template import loader
from pip._vendor import requests

# Create your views here.
def index(request):
    url = 'https://icanhazdadjoke.com/'
    res = requests.get(url, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()

    template = loader.get_template('polls/index.html')
    context = {
        'dad_joke': res["joke"],
    }

    return HttpResponse(template.render(context, request))