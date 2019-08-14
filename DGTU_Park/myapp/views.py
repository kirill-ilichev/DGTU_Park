from django.core.serializers import serialize
from django.http import HttpResponse

from myapp.models.ObjectModel import Object


def objects_output(request):
    object = serialize('geojson', Object.objects.all())
    return HttpResponse(object, content_type='json')
