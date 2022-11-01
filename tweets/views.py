# from django.http import JsonResponse
# from .models import Tweet
# from .serializers import TweetSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET', 'POST'])
# def list_tweets(request):
#   if request.method == 'GET':
#     tweets = Tweet.objects.all()
#     serializer = TweetSerializer(tweets, many=True)
#     return JsonResponse({'tweets': serializer.data})
  
#   if request.method == 'POST':
#     serializer = TweetSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)

from rest_framework.viewsets import ModelViewSet
from .models import Tweet
from .serializers import TweetSerializer

class TweetViewSet(ModelViewSet):
  queryset = Tweet.objects.all()
  serializer_class = TweetSerializer