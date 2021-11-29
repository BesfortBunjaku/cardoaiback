from django.db.models import Q
class CalcField:
    def __init__(self, model,instance):
        self.model = model
        self.instance = instance
       
    def loan_id(self):
        return self.instance

    def invested_amount(self):
        query = Q(type="Funding") & Q(loan_identifier_id=self.instance.identifier)
        data = self.instance.cash.filter(query).values('amount').first().get('amount','')
        return data

    def investment_date(self):
        query = Q(type="Funding") & Q(loan_identifier_id=self.instance.identifier)
        data = self.instance.cash.filter(query).values('reference_date').first().get('reference_date','')
        return data

    def expected_interest_amount(self):
        data = float(self.instance.total_expected_interest_amount) * (self.invested_amount()/float(self.instance.total_amount))
        return data

    def is_closed(self):
        return False

    def expected_irr(self):
        return 5.5

    def realized_irr(self):
        return 6.5


    def calculate_fields(self):
        return {
            'loan': self.loan_id(),
            "invested_amount": self.invested_amount(),
            "investment_date": self.investment_date(),
            "expected_interest_amount": self.expected_interest_amount(),
            "is_closed": self.is_closed(),
            "expected_irr": self.expected_irr(),
            "realized_irr": self.realized_irr(),
               }
