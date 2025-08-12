class Medicine():
    def __init__(self, name,compound,brand,quantity, dosis, price, program):
        self.compound = compound
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.dosis = dosis
        self.price = price
        self. program = program

    def update_name(self, new_name):
        self.name = new_name

    def update_quantity(self,new_quantity):
        self.quantity = new_quantity
    
    def update_dosis(self, new_dosis):
        self.dosis = new_dosis
    
    def update_price(self, new_price):
        self.price = new_price

    def update_program(self, new_program):
        self.program = new_program
    