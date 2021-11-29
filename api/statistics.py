


class Statistic:

    def __init__(self,loan,cash_flow ,user) -> None:
        self.loan = loan
        self.cash_flow = cash_flow
        self.user = user

    def number_of_loans(self) -> int:
        """Number of Loans"""
        pass

    def total_invested_amount(self) -> float:
        """Total invested amount (all loans)"""
        pass

    def current_invested_amount(self) -> float:
        """ Current invested amount (only open loans)"""
        pass

    def total_repaid_amount(self) -> float:
        """Total repaid amount (all loans)"""
        pass

    def  average_realized_irr(self) -> float:
        """Average Realized IRR"""
        pass

    def get_statistics(self) -> dict:
        """"""
        return {
            'number_of_loans': self.number_of_loans(),
            'total_invested_amount': self.total_invested_amount(),
            'current_invested_amount': self.current_invested_amount(),
            'total_repaid_amount': self.total_repaid_amount(),
            'average_realized_irr': self.average_realized_irr()
               }