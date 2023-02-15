from django.shortcuts import render
from rest_framework import mixins
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from booking.models import Cat
from booking.serializers import CatsSerializer


class CatView(ModelViewSet):
    queryset = Cat.objects.all().prefetch_related()
    serializer_class = CatsSerializer

    @action(methods=['get'], detail=False)
    def cats_booking(self, request):
        if request.method == 'GET':
            cats = Cat.objects.all()
            cats_booking = [i for i in cats if i.booking]
            serializer = CatsSerializer(cats_booking, context={'request': request}, many=True)
            return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def cats_free(self, request):
        if request.method == 'GET':
            cats = Cat.objects.all()
            cats_booking = [i for i in cats if i.booking == False]

            serializer = CatsSerializer(cats_booking, context={'request': request}, many=True)
            return Response(serializer.data)
