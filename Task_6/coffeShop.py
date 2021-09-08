import abc


class Location:
    def __init__(self, name, tzone):
        self.name = name
        self.tzone = tzone

    @property
    def get_name(self):
        return self.name


class CaffeShop:
    def __init__(self, name, location, c_type):
        self.name = name
        self.location = location
        self.type = c_type

    @property
    def get_name(self):
        return self.name

    @property
    def get_location(self):
        return self.location.get_name

    @property
    def get_c_type(self):
        return self.type


class Invoice:
    def __init__(self, coffeshop, number):
        self.coffeshop = coffeshop
        self.number = number

    def generate_invoice(self):
        if self.coffeshop.get_location == "Bolivia":
            print(InvoiceType1(self).display_invoice())
        else:
            print(InvoiceType2(self).display_invoice())

    @property
    def get_number(self):
        return self.number


class InvoiceType(metaclass=abc.ABCMeta):

    def display_invoice(self):
        pass


class InvoiceType1(InvoiceType):
    def __init__(self, invoice_wrapped):
        self.invoice_wrapped = invoice_wrapped

    def display_invoice(self):
        return \
            f"----------Invoice info Type 1 -----------\n" \
            f"CoffeShop: {self.invoice_wrapped.coffeshop.get_name}\n" \
            f"Type: {self.invoice_wrapped.coffeshop.get_c_type}\n" \
            f"Location: {self.invoice_wrapped.coffeshop.get_location}\n" \
            f"Invoice Number: {self.invoice_wrapped.get_number}\n"


class InvoiceType2(InvoiceType):
    def __init__(self, invoice_wrapped):
        self.invoice_wrapped = invoice_wrapped

    def display_invoice(self):
        return \
            f"----------Invoice info Type 2 -----------\n" \
            f"CoffeShop: {self.invoice_wrapped.coffeshop.get_name}\n" \
            f"Type: {self.invoice_wrapped.coffeshop.get_c_type}\n" \
            f"Location: {self.invoice_wrapped.coffeshop.get_location}\n" \
            f"Additional info here: \n" \
            f"Invoice Number: {self.invoice_wrapped.get_number}\n"


def main():
    location1 = Location("Bolivia", "GMT-4")
    shop = CaffeShop("Coffeina", location1, "Main Shop")
    invoice = Invoice(shop, "001")
    invoice.generate_invoice()


if __name__ == '__main__':
    main()
