from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import GrantGoal


from .serializers import ListGrantGoalSerializer, DetailGrantGoalSerializer
# Create your views here.


####API GRANTGOAL###

##CREATE

##RETRIEVE

##LIST
class ListGrantGoalAPIView(APIView):
    def get(self, request):
        queryset = GrantGoal.objects.all()
        data = ListGrantGoalSerializer(queryset, many=True).data
        return Response(data)
#DETAIL
class DetailGrantGoalAPIView(APIView):
    def get(self, request, pk):
        data = DetailGrantGoalSerializer(GrantGoal.objects.get(pk=pk)).data
        return Response(data)
##UPDATE
