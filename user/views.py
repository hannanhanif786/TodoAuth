from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer
from rest_framework import status

class CreateUser(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
