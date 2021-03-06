from django.db import models
from rest_framework import serializers
from .models import Movie,StreamPlatforms,Review,Upcoming,Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class UpcomingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upcoming
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True,read_only=True)

    
    class Meta:
        model = Movie
        # fields = "__all__"
        fields = "__all__"

    def get_len_name(self,object):
        leng = len(object.name)
        return leng



class SpSerialzier(serializers.HyperlinkedModelSerializer):
    movies = MovieSerializer(many=True,read_only=True)
    # movies = serializers.HyperlinkedRelatedField(
    #     many=True,read_only=True,view_name="movie-detail"
    # )

    class Meta:
        model = StreamPlatforms
        fields = "__all__"

# class MovieSerializer(serializers.Serializer):
#     id  = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     active  = serializers.BooleanField()
#     description  = serializers.CharField(max_length=255)

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different")
#         else:
#             return data

#     def validate_name(self,value):

#         if len(value) < 2:
#             raise serializers.ValidationError("Name is Too Short")
#         else:
#             return value

