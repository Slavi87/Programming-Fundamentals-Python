class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [el for el in self.products if el[0] == first_letter]

    def __repr__(self):
        # return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted(self.products))
        string_for_output = f"Items in the {self.name} catalogue:\n"
        string_for_output += '\n'.join(sorted(self.products))
        return string_for_output


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
