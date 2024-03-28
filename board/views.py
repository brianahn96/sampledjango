from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import Http404
from .serializers import BlogSerializer
from .models import Blog


# Create your views here.
@api_view(["GET", "POST", "DELETE"])
def hello_rest_api(request):
    data = {"message": "Hello, REST API!"}
    return Response(data)


class HelloWorldListCreateView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get(self, _):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HelloWorldView(APIView):
    def get(self, _):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class HelloWorldDetail(APIView):
    def get_object(self, id):
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, _, id):
        queryset = self.get_object(id)
        serializer = BlogSerializer(queryset, many=False)
        return Response(serializer.data, status=200)

    def put(self, request, id):
        queryset = self.get_object(id)
        serializer = BlogSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = 201)
        return Response(serializer.errors, status=400)

    def delete(self, _, id):
        query = self.get_object(id)
        query.delete()
        return Response(status=204)

    def patch(self, request, id):
        patchobject = self.get_object(id)
        serializer = BlogSerializer(
            patchobject, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = 201)
        return Response(data="wrong parameters", status = 400)
