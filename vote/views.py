from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import *
from .serializers import *

class LikesViewSet(ModelViewSet):
    queryset = Like_And_DisLike.objects.filter(type='like')
    serializer_class = Like_And_DisLike_Serializer


class DisLikesViewSet(ModelViewSet):
    queryset = Like_And_DisLike.objects.filter(type='dislike')
    serializer_class = Like_And_DisLike_Serializer


class ChangeType(APIView):

    def post(self , request):
        if self.request.POST.get('type') == 'like':
            pk = self.request.POST.get('id')
            like_and_dislike = Like_And_DisLike.objects.get(pk=pk)
            like_and_dislike.type = 'like'
            like_and_dislike.save()

            return Response({'detail': ('like_and_dislike type has been set LIKE')}, 200)
        else:
            pk = self.request.POST.get('id')
            like_and_dislike = Like_And_DisLike.objects.get(pk=pk)
            like_and_dislike.type = 'dislike'
            like_and_dislike.save()

            return Response({'detail': ('like_and_dislike type has been set DISLIKE')}, 200)