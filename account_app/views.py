from django.shortcuts import render
from django.views import View
# from django.http import JsonResponse
# from .models import UserModel



# def index(request):
#     user = UserModel()
#     context = {'user': user}
#     return JsonResponse({'hello': 'world'}, context)

class RegisterView(View):
    def get(self, request):
        return render(request, 'account_app/register.html')
