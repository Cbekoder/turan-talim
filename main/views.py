import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core.utils import send_request
from exams.models import Direction
from main.models import Language


class HomeView(View):
    def get(self, request):
        context = {'is_user':False}
        if request.user.is_authenticated:
            context.update({
                'user': request.user,
                'is_user':True,
            })
        return render(request, 'homepage.html', context)



class ExamsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'user': request.user,
                'directions': Direction.objects.all()

            }
            return render(request, 'directions.html', context)
        return redirect('signing')

    def post(self, request):
        if request.user.is_authenticated:
            pass

            return redirect('exams')
        return redirect('signing')

@csrf_exempt
def send_to_ai(request):
    data = json.loads(request.body)
    user_message = data.get('message')
    response = send_request(user_message)
    return JsonResponse({'response': response})

