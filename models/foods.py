class RequestModel:
    def __init__(
        self,
        first_name,
        last_name,
        address,
        date,
        burguer_choice,
        burguer_quantity,
        soup_choice,
        soup_quantity,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.date = date

        self.burguer_choice = burguer_choice if burguer_choice != 0 else None
        self.burguer_quantity = burguer_quantity
        self.soup_choice = soup_choice if soup_choice != 0 else None
        self.soup_quantity = soup_quantity
        self.requests = f"""
            {self.burguer_quantity} x {self.burguer_choice}
            {self.soup_choice} x {self.soup_choice}
        """
