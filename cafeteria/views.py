from django.http import HttpResponse
from django.template import RequestContext, loader

from cafeteria.models import Station


def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'stations': Station.objects.all(),
    })
    return HttpResponse(template.render(context))
