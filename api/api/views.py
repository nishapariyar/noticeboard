# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics


from .models import Noticelist
from .serializers import NoticeSerializer

# Create your views here.


class CreateView(generics.ListCreateAPIView):
    queryset = Noticelist.objects.all()
    serializer_class = NoticeSerializer

    def perform_create(self, serializer):
        serializer.save()

