from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
def home(request):
    if request.method == 'POST':
        try:
            body = request.body.decode()
            content = json.loads(body)
            x = int(content['x'])
            n = int(content['n'])
            answer = calculate(x, n)
            return JsonResponse({'answer': answer})
        except Exception as e:
            print(e)
            return JsonResponse({'answer': 'error'})


def calculate(x, n):
    try:
        ans = 0
        for i in range(1, n + 1):
            ans += 1 / (x**i)
        return ans
    except Exception as e:
        print(e)
        return None
