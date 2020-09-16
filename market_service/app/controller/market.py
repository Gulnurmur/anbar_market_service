from flask import jsonify, Blueprint, request
from app.schemas.schema import ProductSchema,ProductSchema
import requests
from http import HTTPStatus

market = Blueprint("market", __name__)


@market.route("/", methods=["GET"])

def test():

    return jsonify({"result": True})




@market.route("/market", methods=["GET"])
def get_market():

    req = requests.get("http://127.0.0.1:5338/api/v1/categories")

    data = req.json()
    print(data)

    return jsonify(data), HTTPStatus.OK



@market.route("/sale/<uuid:id>", methods = ["POST"])
def post_sale(id):

    new_data = request.get_json()
    new_data_count = new_data.get("count") #daxil etdiyim

    req1 = requests.get("http://127.0.0.1:5338/api/v1/product/{}".format(id))

    count = req1.json().get("count") #evvelki

    new_count = int(count)-int(new_data_count)

    if new_count<0:     

        return jsonify ({"result":"yoxdur"})

    else:

        req=requests.post("http://127.0.0.1:5338/api/v1/product/{}".format(id),json={ "count" : str(new_count)})
        
        if req.status_code == 200:

            return req.json()

        else:

            return False
    


