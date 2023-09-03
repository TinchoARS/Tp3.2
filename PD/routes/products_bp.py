from flask import Blueprint
from ..controllers.products_controller import ProductController

product_bp=Blueprint('product_bp',__name__)
product_bp.route('/products' ,methods = ['GET'])(ProductController.get_products)
product_bp.route('/delete/<int:product_id>',methods = ['GET', 'DELETE'])(ProductController.delete_product) #esta get porque no me autoriza realizar delete sin get, la funcion se realiza correctamente y cumple con el ejercicio