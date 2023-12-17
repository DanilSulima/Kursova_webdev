from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions
from getfood.models import Category
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
    return render(request,'index.html', {'name': 'danil'})
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

