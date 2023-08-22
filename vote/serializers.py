from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from music.models import Music
from music.serializers import MusicSerializer
from story.models import Story
from story.serializers import StorySerializer
from .models import *


class Like_And_DisLiked_ObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Music):
            serializer = MusicSerializer(value)
        elif isinstance(value, Story):
            serializer = StorySerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')
        return serializer.data


class Like_And_DisLike_Serializer(ModelSerializer):
    content_object = Like_And_DisLiked_ObjectRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        queryset=User.objects.all(), write_only=True
    )

    class Meta:
        model = Like_And_DisLike
        fields = '__all__'
        depth = 1
