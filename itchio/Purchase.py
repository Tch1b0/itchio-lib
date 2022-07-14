from typing import Union


class Purchase:
    def __init__(
            self,
            donation: Union[bool, None],
            id: int,
            email: str,
            created_at: str,
            source: str,
            currency: str,
            price: str,
            sale_rate: int,
            game_id: int) -> None:

        self.donation = donation
        self.id = id
        self.email = email
        self.created_at = created_at
        self.source = source
        self.currency = currency
        self.price = price
        self.sale_rate = sale_rate
        self.game_id = game_id

    @classmethod
    def parse_from_dict(cls, data: dict):
        return cls(
            donation=data["donation"],
            id=data["id"],
            email=data["email"],
            created_at=data["created_at"],
            source=data["source"],
            currency=data["currency"],
            price=data["price"],
            sale_rate=data["sale_rate"],
            game_id=data["game_id"]
        )
