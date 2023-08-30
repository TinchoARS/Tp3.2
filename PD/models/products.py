from ..database import DatabaseConnection


class products:
    def __init__(self, product_id,product_name,brand,category,model_year,list_price):
        self.product_id = product_id
        self.product_name = product_name
        self.brand = brand
        self.category = category
        self.model_year = model_year
        self.list_price = list_price

    @classmethod
    def get_all_products(cls):
            query = '''
            SELECT
                p.product_id,
                p.product_name,
                b.brand_id,
                b.brand_name,
                c.category_id,
                c.category_name,
                p.model_year,
                p.list_price
            FROM
                products p
                JOIN brands b ON p.brand_id = b.brand_id
                JOIN categories c ON p.category_id = c.category_id
            '''
            results = DatabaseConnection.fetch_all(query)
            products_list = []

            for result in results:
                products_list.append({
                    "product_id": result[0],
                    "product_name": result[1],
                    "brand": {"brand_id": result[2], "brand_name": result[3]},
                    "category": {"category_id": result[4], "category_name": result[5]},
                    "model_year": result[6],
                    "list_price": result[7]
                })

            return products_list
        
