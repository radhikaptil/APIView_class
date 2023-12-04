from django.shortcuts import render

# Create your views.
from rest_framework.views import APIView
from app.serializers import *
from app.models import *
from rest_framework.response import Response

class ProductData(APIView):
    def get(self,request,Pid):

        #This is for Pid which is coming from url
        #PD=Product.objects.get(Pid=Pid)
        #JSD=ProductModelSerailizer(PD)

        PD=Product.objects.all()
        JSD=ProductModelSerailizer(PD,many=True)
        return Response(JSD.data)
    
    def post(self,request,Pid):
        CJSD=request.data
        PD=ProductModelSerailizer(data=CJSD)
        if PD.is_valid():
            PD.save()
            return Response({"massage":"Data Inserted Successfully"})
        else:
            return Response({"massage":"Failed to insert data"})
        

    def put(self,request,Pid):
        CJSD=request.data
        PD=Product.objects.get(Pid=CJSD['Pid'])
        POD=ProductModelSerailizer(PD,data=CJSD)
        if POD.is_valid():
            POD.save()
            return Response({"massage":" Data Updated Successfully"})
        else:
            return Response({"massage":"Validation Problem"})
        
    def patch(self,request,Pid):
        CJSD=request.data
        PD=Product.objects.get(Pid=CJSD['Pid'])
        POD=ProductModelSerailizer(PD,CJSD, partial=True)
        if POD.is_valid():
            POD.save()
            return Response({"massage":"Updated successfully"})
        else:
            return Response({"massage":"Validation Error"})
        
        

    def delete(self,request,Pid):
        PD=Product.objects.get(Pid=Pid)
        PD.delete()
        return Response({"massage":"Deleted successfully"})
    
    


    
    