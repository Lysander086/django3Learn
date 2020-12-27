from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.views import APIView

from users.serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):
    def get(self, req):
        serializer = UserDisplaySerializer(req.user)
        return Response(serializer.data)
