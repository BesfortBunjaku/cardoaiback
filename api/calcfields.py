
class CalcField:
    def __init__(self, cashflow_instance):
        self.cashflow_instance = cashflow_instance
       
    
    def invested_amount(self):
        pass

    def investment_date(self):
        pass

    def expected_interest_amount(self):
        pass

    def is_closed(self):
        pass

    def expected_irr(self):
        pass

    def realized_irr(self):
        pass


    def calculate_fields(self):
        return {
            "invested_amount": self.invested_amount(),
            "investment_date": self.investment_date(),
            "expected_interest_amount": self.expected_interest_amount(),
            "is_closed": self.is_closed(),
            "expected_irr": self.expected_irr(),
            "realized_irr": self.realized_irr(),
               }
