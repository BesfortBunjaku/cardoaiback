# Create your tasks here
from celery import shared_task
import csv
from .models import CashFlow ,Loan

@shared_task
def save_csv(string_csv, file_name):
    test = csv.DictReader(string_csv.split(), delimiter=',')
    for item in list(test):
        if str(file_name) == 'cash_flows.csv':
            cash_flow = CashFlow(**item)
            cash_flow.save()
        if str(file_name)=='loans.csv':
            loan = Loan(**item)
            loan.save()

 
            

