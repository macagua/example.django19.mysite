# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from webflix.models import TvSerie
from webflix.serializers import TvSerieSerializer


@csrf_exempt
def tv_serie_list(request):
    """
    List all code Tv serie, or create a new Tv serie.
    """
    if request.method == 'GET':
        tv_series = TvSerie.objects.all()
        serializer = TvSerieSerializer(tv_series, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TvSerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def tv_serie_detail(request, pk):
    """
    Retrieve, update or delete a Tv serie.
    """
    try:
        tv_serie = TvSerie.objects.get(pk=pk)
    except TvSerie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TvSerieSerializer(tv_serie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TvSerieSerializer(tv_serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tv_serie.delete()
        return HttpResponse(status=204)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
