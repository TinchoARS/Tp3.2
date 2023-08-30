from ..models.products import products
from flask import jsonify

class ProductController:
    @classmethod
    def get_products(self):
        products_list = products.get_all_products()

        response = []
        for product in products_list:
            product_data = {
                "brand": {
                    "brand_id": product.brand["brand_id"],
                    "brand_name": product.brand["brand_name"]
                },
                "category": {
                    "category_id": product.category["category_id"],
                    "category_name": product.category["category_name"]
                },
                "list_price": str(product.list_price),
                "model_year": product.model_year,
                "product_id": product.product_id,
                "product_name": product.product_name
            }
            response.append(product_data)

        return jsonify(response), 200
