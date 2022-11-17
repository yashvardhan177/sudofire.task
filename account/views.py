from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED

from account.models import Customer


@api_view(["POST"])
def create_customer(request):
    user = User.objects.create(
        first_name=request.data.get('first_name'),
        last_name=request.data.get('last_name'),
        email=request.data.get('email'),
        mobile_num=request.data.get('mobile_num')
    )
    Customer.objects.create(
        user=user
    )
    return JsonResponse({"status": HTTP_201_CREATED, "message": "Customer Created"})
