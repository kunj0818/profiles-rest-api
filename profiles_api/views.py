from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """test apiview"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [  'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',]
        return Response({'message':'hello message!', 'an_apiview':an_apiview})

    def post(self, request):
        """print message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """put method"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """patch metod"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """patch metod"""
        return Response({'method': 'DELETE'})
