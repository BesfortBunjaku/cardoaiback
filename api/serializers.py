from .models import CashFlow,CsvFile,Loan
from rest_framework import serializers

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'
        

class CashFlowSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashFlow
        fields = '__all__'
        


class CsvFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CsvFile
        fields = '__all__'