## -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

class Tweet(APIView):
    def post(self, request, format=None):
        return Response("hallo")

def save_oauth_token(request):

    user_id = request.GET.get('user_id')
    twitter_token = request.GET.get('twitter_token')
    twitter_token_sercret = request.GET.get('twitter_token_sercret')

    if user_id and twitter_token and twitter_token_sercret:
        user = User(user_id=user_id,
                    twitter_token=twitter_token,
                    twitter_token_sercret=twitter_token_sercret
                )
        user.save()
        return HttpResponse("Success")

    return HttpResponse("False")
