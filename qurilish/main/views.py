from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    # http_method_names = ['post', 'get']


# @api_view(http_method_names=['PATCH'])
# def director_view(request, pk):
#     if request.method == "PATCH":
#         try:
#             director = Director.objects.get(pk=pk)
#         except director.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = DirectorSerializer(director, data=request.data, context={'request': request})
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response({
#                 'state': 0,
#                 'message': f"{serializer.errors}"
#             })


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    # http_method_names = ['post', 'get']


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    depth = 4


class SubsystemViewSet(viewsets.ModelViewSet):
    queryset = Subsystem.objects.all()
    serializer_class = SubsystemSerializer
    depth = 3


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    depth = 2


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    depth = 4


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
