from ..models.products import products
from flask import request,jsonify
class ProductController:
    @classmethod
    def get_products(cls):
        products_list = products.get_all_products()

        response = []
        
        for product in products_list:
              brand = product.get("brand", {})
              category = product.get("category", {})
              product_data = {
                   "brand": {
                    "brand_id": brand.get("brand_id"),
                    "brand_name": brand.get("brand_name")
                },
                "category": {
                    "category_id": category.get("category_id"),
                    "category_name": category.get("category_name")
                },
                "list_price": str(product.get("list_price")),
                "model_year": product.get("model_year"),
                "product_id": product.get("product_id"),
                "product_name": product.get("product_name")
              }
              response.append(product_data)
        
        response.append({"total_products": len(products_list)})

        return jsonify(response), 200
    
    @classmethod
    def delete_product(cls, product_id):
        product = products.delete_product(product_id)
        return jsonify(product), 200
