from flask import jsonify, Blueprint,request
from http import  HTTPStatus
from marshmallow.exceptions import ValidationError
from app.schemas.schema import  ProductSchema
from app.models.model import  Product
from app.utils.helper import check_category_id, check_product_name_and_count


product = Blueprint("product", __name__)



@product.route("/", methods=["GET"])
def test():

    return jsonify({"result": True})



@product.route("/products", methods = ["GET"])
def get_products():

    product = Product.query.all()

    return ProductSchema().jsonify(product,many=True),HTTPStatus.OK


@product.route("/product/<uuid:id>", methods = ["GET"])
def get_product(id):

    product = Product.query.filter_by(id=id).first()

    if product:
        return ProductSchema().jsonify(product),HTTPStatus.OK

    return jsonify({"result":False})


@product.route("/product", methods = ["POST"])
def create_products():

    try:
        data = request.get_json()

        data_name = data.get("name")

        data_count = data.get("count")

        check = check_category_id(data.get("category_id"))

        if not check:
            return jsonify({"result":False, "message": "error happened"}), HTTPStatus.BAD_REQUEST

        elif check:
            return check_product_name_and_count(data.get("name"),data.get("count"))

        
    except ValidationError as err:

        return jsonify({"result":False}),HTTPStatus.NOT_FOUND



@product.route("/product/<uuid:id>", methods = ["POST"])
def create_product(id):

    product = Product.query.filter_by(id=id).first()
    data = request.get_json()

    if data == None:
        return jsonify({"result":False})

    else:

        product.count = data.get("count")
        product.save()

        return jsonify({"result":True})


@product.route("/product/<uuid:id>", methods = ["PUT"])
def update_product(id):

    data = request.get_json()

    product = Product.query.filter_by(id=id).first()

    if product:
        serializer = ProductSchema()
        product_up = serializer.dump(data)
        product_update = product.update(**product_up)

        return ProductSchema().jsonify(product), HTTPStatus.OK

    return jsonify({"result":False}), HTTPStatus.BAD_REQUEST 


@product.route("/product/<uuid:id>", methods = ["DELETE"])
def delete_product(id):

    product = Product.query.get(id)

    if Product:

        product.delete()

        return jsonify({"result":True}), HTTPStatus.OK

    return jsonify({"result":False, "message": "this product not found"}),HTTPStatus.BAD_REQUEST

