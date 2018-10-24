from django.http import JsonResponse
import time
from models import Question
import elasticapm

@elasticapm.capture_span('send_http_request')
def send_http_request(index):
    time.sleep(0.05)

def index(request):
    for _ in range(3):
        results = Question.objects.all().values()
        results = list(results)
        send_http_request(_)
    return JsonResponse({
        "questions": results
    }, safe=False)
