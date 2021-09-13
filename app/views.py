from django.shortcuts import render

# Create your views here.
from .models import Emp
from .serializers import EmpSerializer  #EmpSerializer is resp for conv qs into json data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#NON-ID based operations
class EmpListView(APIView):
    def get(self,request):  #db-->qs
        qs = Emp.objects.all()   #getting data using orm query(conv into sql)
        #qs ---> dict
        dict_data = EmpSerializer(qs,many=True)  #if multiple records are there then we've keep many=True
        #dict ---> json
        return Response(dict_data.data) #serializer obj.data we've to use

    def post(self,request):
        #data = request.data #user sending data
        dict_data = EmpSerializer(data=request.data)

        if dict_data.is_valid():
            dict_data.save()
            return Response(dict_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(dict_data.errors,status=status.HTTP_400_BAD_REQUEST)

import json
class EmpDetailView(APIView):
    def get(self,request,id):
        try:
            emp = Emp.objects.get(id=id)    #single obj
        except Emp.DoesNotExist:
            json_data = json.dumps({"msg":"Requested data not found"})
            return Response(json_data,status=status.HTTP_404_NOT_FOUND)
        else:
            dict_data = EmpSerializer(emp)  #so many=true not req
            return Response(dict_data.data,status=status.HTTP_200_OK)

    def get_object_by_id(self,id):
        try:
            emp = Emp.objects.get(id=id)    #single obj
        except Emp.DoesNotExist:
            emp=None
        return emp

    def put(self,request,id):
        emp = self.get_object_by_id(id) #will get object or None val

        if emp is None:
            json_data = json.dumps({"msg": "Requested data not found to GET"})
            return Response(json_data, status=status.HTTP_404_NOT_FOUND)

        dict_data = EmpSerializer(emp,data=request.data)

        if dict_data.is_valid():
            dict_data.save()
            return Response(dict_data.data,status=status.HTTP_200_OK)

        else:
            return Response(dict_data.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        emp = self.get_object_by_id(id)

        if emp is None:
            json_data = json.dumps({"msg": "Requested data not found to Update"})
            return Response(json_data, status=status.HTTP_404_NOT_FOUND)

        emp.delete()
        json_data = json.dumps({"msg": "Requested data Deleted Successfully"})
        return Response(json_data, status=status.HTTP_404_NOT_FOUND)
