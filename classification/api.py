from django.http import JsonResponse

from rest_framework.decorators import api_view
from . import classifier


@api_view(['POST'])
def predict(request):
    req = request.data
    result = classifier.predict_disease(req["symptoms"])
    data = {
        "result": result
    }
    return JsonResponse(data, safe=False)