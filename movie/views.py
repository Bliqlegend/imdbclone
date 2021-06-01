from django.shortcuts import render
from .serializer import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def MovieViewset(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def MovieDetailViewset(request,pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({
                'Error': 'Movie not found',
            },status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        serializer = MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)