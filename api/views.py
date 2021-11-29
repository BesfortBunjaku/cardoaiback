from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer
from rest_framework.parsers import MultiPartParser
from .permissions import InvestorAndAnalystPermissions
from .tasks import save_csv
from .statistics import Statistic
from django.utils.translation import gettext_lazy as _

class CashFlowAPIView(APIView):

    # permission_classes = [InvestorAndAnalystPermissions]
    serializer_class = CashFlowSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer]
    parser_classes = [MultiPartParser]

    def get(self, request):
        cash_flows = CashFlow.objects.all()
        serializer = CashFlowSerializer(cash_flows, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        string_csv = request.data['file_path'].read().decode('utf-8')
        save_csv.delay(string_csv)
        serializer = CashFlowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploded_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class CsvFileAPIView(APIView):
 
    # permission_classes = [InvestorAndAnalystPermissions]
    serializer_class = CsvFileSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer]
    parser_classes = [MultiPartParser]

    def post(self, request, format=None): 
        print(request.FILES['file_path'].name)
        # print(type(request.FILES['file_path'].name))
        string_csv = request.data['file_path'].read().decode('utf-8')
        save_csv.delay(string_csv=string_csv,file_name=request.FILES['file_path'].name)
        serializer = CsvFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #serializer.save(uploded_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class StatisticsAPIView(APIView):

    def get(self, request):
        """check first in cash"""
        statistic = Statistic(loan=Loan, cash_flow=CashFlow, user=request.user)
        return Response(statistic.get_statistics())
