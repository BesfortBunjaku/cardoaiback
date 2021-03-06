from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from .calcfields import CalcField
from django.db.models import Q


class Loan(models.Model):

    identifier = models.CharField(max_length=255,primary_key=True)
    issue_date = models.DateField()
    total_amount = models.FloatField(default=0) 
    rating = models.IntegerField(default=1) # validators=[MinValueValidator(1), MaxValueValidator(9)]
    maturity_date = models.DateField()
    total_expected_interest_amount = models.FloatField()


class LoanCalc(models.Model):

    loan = models.OneToOneField(Loan, on_delete=models.CASCADE, primary_key=True)
    invested_amount = models.FloatField()
    investment_date = models.DateField()
    expected_interest_amount = models.FloatField() 
    is_closed = models.BooleanField(default=False)
    expected_irr = models.FloatField()
    realized_irr = models.FloatField()


def after_loan_save(sender, instance, **kwargs):
    calc_field  = CalcField(model=sender,instance=instance)
    calculated_dict = calc_field.calculate_fields()
    loan_calc = LoanCalc(**calculated_dict)
    loan_calc.save()


post_save.connect(after_loan_save, sender=Loan)


  
class CashFlow(models.Model):

    loan_identifier = models.ForeignKey(Loan, on_delete=models.CASCADE,db_constraint=False, related_name='cash')
    reference_date = models.DateField()
    type = models.CharField(max_length=20)
    amount = models.FloatField()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class CsvFile(models.Model):
    file_path = models.FileField(upload_to='media')
    # cash_flow = models.FileField(upload_to='media')
    # uploded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

