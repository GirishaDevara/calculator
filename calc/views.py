from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calc(request):
    if request.method == 'POST':
        value1 = int(request.POST.get('value1'))
        value2 = int(request.POST.get('value2'))
        operation = request.POST.get('operation')
    else:
        value1 = int(request.GET.get('value1'))
        value2 = int(request.GET.get('value2'))
        operation = request.GET.get('operation')
    if operation == ' ':
        ans = value1 + value2
    elif operation == '-':
        ans = value1 - value2
    elif operation == '*':
        ans = value1 * value2
    elif operation == '/':
        ans = value1 / value2
    return JsonResponse({'Output': ans})
