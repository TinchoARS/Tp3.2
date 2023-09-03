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
            total_products = 0

            for result in results:
                    products_list.append({
                        "product_id": result[0],
                        "product_name": result[1],
                        "brand": {"brand_id": result[2], "brand_name": result[2]},
                        "category": {"category_id": result[3], "category_name": result[3]},
                        "model_year": result[4],
                        "list_price": result[5]        
                    })
                    total_products + 1
            
            products_list.append({"total_products": total_products})   
            return products_list
    
    @classmethod
    def delete_product(cls, product_id):
        query = '''
        DELETE FROM products WHERE product_id = %s
        '''
        params=(product_id,)
        DatabaseConnection.execute_query(query, params)
        return{"msg": "Product deleted successfully"}, 204
