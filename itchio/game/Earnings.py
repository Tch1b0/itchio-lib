class Earnings:
    def __init__(
        self,
        currency: str,
        amount_formatted: str,
        amount: int):

        self.currency = currency
        self.amount_formatted = amount_formatted
        self.amount = amount

    @staticmethod
    def parse_from_dict(data: dict):
        return Earnings(
            currency = data["currency"],
            amount_formatted = data["amount_formatted"],
            amount = data["amount"]
        )