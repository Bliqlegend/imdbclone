import re
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.shortcuts import render
from .serializer import MovieSerializer,SpSerialzier,ReviewSerializer,UpcomingSerializer,GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie,StreamPlatforms,Review,Upcoming,Genre
from rest_framework import serializers, status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .permissions import AdminorReadonly,ReviewUserorReadonly

class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class UpcomingViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Upcoming.objects.all()
        serializer = UpcomingSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk):
        queryset = Upcoming.objects.all()
        upcoming = get_object_or_404(queryset,pk=pk)
        serializer = UpcomingSerializer(upcoming)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = UpcomingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        upcoming = Upcoming.objects.get(pk=pk)
        serializer = UpcomingSerializer(upcoming,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        upcoming = Upcoming.objects.get(pk=pk)
        upcoming.delete()
        serializer = UpcomingSerializer(upcoming)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
 
class ReviewViewset(generics.ListAPIView):
    permission_classes = [AdminorReadonly]
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


    
class ReviewCreateViewset(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(movie=movie,username=review_user)
        if review_queryset.exists():
            raise ValidationError("You Have already added a Review for this movie")
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
        movie.number_rating = movie.number_rating +1
        movie.save()
        # else:
        serializer.save(movie=movie,username=review_user)

class ReviewDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReviewUserorReadonly]
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer


# class ReviewViewset(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class ReviewDetailViewset(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)


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