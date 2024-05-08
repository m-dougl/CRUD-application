class RequestModel:
    def __init__(self, 
                 burguer_choice,
                 burguer_quantity,
                 soup_choice,
                 soup_quantity):
        self.burguer_choice = burguer_choice if burguer_choice !=0 else None
        self.burguer_quantity = burguer_quantity
        self.soup_choice = soup_choice if soup_choice !=0 else None
        self.soup_quantity = soup_quantity
        