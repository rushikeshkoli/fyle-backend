from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.db.models import Q
from django.core import serializers
from rest_framework.response import Response
from . import models


# Create your views here.

def hello(request):
    return HttpResponse('hello')


class BranchesList(APIView):
    def get(self, request):
        city = request.GET.get('q')
        limit = int(request.GET.get('limit'))
        offset = int(request.GET.get('offset'))
        data = list(models.Branches.objects.filter(city__iexact=city).order_by('ifsc')[offset: offset + limit])
        print(data)

        # print(serializers.serialize("json", data))
        data_json = []
        for branch in data:
            data_json.append(
                {'ifsc': branch.ifsc, 'bank_id': branch.bank_id, 'branch': branch.branch, 'address': branch.address,
                 'city': branch.city, 'district': branch.district, 'state': branch.state})
        return Response({'branches': data_json})


class BranchesAuto(APIView):
    def get(self, request):
        search_text = request.GET.get('q')
        limit = int(request.GET.get('limit'))
        offset = int(request.GET.get('offset'))
        print(search_text, limit, offset)
        data = list(
            models.Branches.objects.filter(Q(branch__icontains=search_text) | Q(ifsc__icontains=search_text) | Q(
                bank__name__icontains=search_text) | Q(address__icontains=search_text) | Q(city__icontains=search_text) | Q(
                district__icontains=search_text) | Q(state__icontains=search_text)).order_by('ifsc')[
            offset: limit + offset])
        data_json = []
        for branch in data:
            data_json.append(
                {'ifsc': branch.ifsc, 'bank_id': branch.bank_id, 'branch': branch.branch, 'address': branch.address,
                 'city': branch.city, 'district': branch.district, 'state': branch.state})
        # data = list(Branches.objects.all()[0: 3])
        print(data)
        return Response({'branches': data_json})
