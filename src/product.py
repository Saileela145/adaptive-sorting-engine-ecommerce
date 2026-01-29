
class Product:
    def __init__(self, product_id, name, price, rating, date_added):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.rating = rating
        self.date_added = date_added

    def __repr__(self):
        return (
            f"Product(id={self.product_id}, "
            f"name={self.name}, "
            f"price={self.price}, "
            f"rating={self.rating}, "
            f"date={self.date_added})"
        )
