from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ravintolat.models import Ravintola
from ravintolat.serializers import RavintolaSerializer

@csrf_exempt
def ravintola_list(request):
    """
    List all code Ravintolas, or create a new Ravintola.
    """
    if request.method == 'GET':
        Ravintolat = Ravintola.objects.all()
        serializer = RavintolaSerializer(Ravintolat, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RavintolaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ravintola_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        ravintola = Ravintola.objects.get(pk=pk)
    except Ravintola.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RavintolaSerializer(ravintola)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RavintolaSerializer(ravintola, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ravintola.delete()
        return HttpResponse(status=204)