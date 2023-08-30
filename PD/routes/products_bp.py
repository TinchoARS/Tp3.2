from flask import Blueprint
from ..controllers.products_controller import ProductController

product_bp=Blueprint('product_bp',__name__)
product_bp.route('/products' ,methods = ['GET'])(ProductController.get_products)