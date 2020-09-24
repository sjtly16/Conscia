from django.shortcuts import render
from .serializers import LoginUserSerializer,
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from knox.models import AuthToken

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token = AuthToken.objects.create(user)[1]
            return Response({
                "error": False,
                "message": "success",
                "user": LoginUserSerializer(user, context=self.get_serializer_context()).data,
                "token": token
            })
        else:
            return Response({
                "error": True,
                "message": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
