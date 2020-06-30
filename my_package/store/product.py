class Product(object):
    def __init__(self, price):
        self.price = price

    def discount(self, percent):
        try:
            float(percent)
        except ValueError:
            raise TypeError('Percent must be number.')
        return (100-percent) * self.price / 100


if __name__ == '__main__':
    Product(400).discount(33)
