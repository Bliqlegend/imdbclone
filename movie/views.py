import re
from django.shortcuts import render
from .serializer import MovieSerializer,SpSerialzier
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie,StreamPlatforms
from rest_framework import status
# Create your views here.
class StreamPlatformViewset(APIView):
    def get(self,request):
        platform = StreamPlatforms.objects.all()
        serializer = SpSerialzier(platform,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer =  SpSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SpdetailViewset(APIView):

    def get(self, request,pk):
        platform = StreamPlatforms.objects.get(pk=pk)
        serializer = SpSerialzier(platform,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request,pk):
        platform = StreamPlatforms.objects.get(pk=pk)
        serializer = SpSerialzier(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        platform = StreamPlatforms.objects.get(pk=pk)
        platform.delete()
        serializer = SpSerialzier(platform)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

class MovieViewset(APIView):

    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class MovieDetailViewset(APIView):

    def get(self, request,pk):
        movie =  Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        serializer = MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def MovieViewset(request):

#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def MovieDetailViewset(request,pk):

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({
#                 'Error': 'Movie not found',
#             },status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)