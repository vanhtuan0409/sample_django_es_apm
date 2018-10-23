from django.http import JsonResponse
import time
from models import Question

def index(request):
    for _ in range(3):
        results = Question.objects.all().values()
        results = list(results)
        time.sleep(0.1)
    return JsonResponse({
        "questions": results
    }, safe=False)
