class product(object):
    def __init__(self, price, itemName, weight, brand, cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'For Sale'
    def sell(self):
        self.status = 'Sold'
        return self
    def addTax(self, tax):
        return self.price * (1 + tax)
    def returnItem(self, reason):
        if reason == 'defective':
            self.price = 0
            self.status = 'defective'
        elif reason == 'in the box, like new':
            self.status = 'For Sale'
        elif reason == 'opened':
            self.status = 'Used'
            self.price = self.price * 0.8
        return self
    def displayInfo(self):
        print 'Name:', self.itemName
        print 'Price:', self.price
        print 'Weight:', self.weight
        print 'Brand:', self.brand
        print 'Cost:', self.cost
        print 'Status:', self.status
        return self

phone = product(1000, 'iPhone X', '.38lb', 'Apple', 800)
phone.displayInfo()
print phone.addTax(.1)
phone.sell()
phone.displayInfo()
phone.returnItem('opened')
phone.displayInfo()