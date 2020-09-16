from app.config.settings.extensions import ma
from app.models.model import Product,Category
from marshmallow import fields
from marshmallow.fields import String, Email, UUID,Nested,Integer
# from marshmallow import validates_schema



class CategorySchema(ma.SQLAlchemyAutoSchema):

    name = String(required=True)
    products = Nested("ProductSchema", many=True)

    class Meta:
        model = Category
        load_instance = True



class ProductSchema(ma.SQLAlchemyAutoSchema):

    name = String(required=True)
    count = Integer(required=True)
    



