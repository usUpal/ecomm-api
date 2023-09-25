from tortoise import Model, fields as f
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = f.IntField(pk=True, index=True)
    username = f.CharField(max_length=20, null=False, unique=True)
    email = f.CharField(max_length=200, null=False, unique=True)
    password = f.CharField(max_length=100, null=False)
    is_verified = f.BooleanField(default=False)
    join_data = f.DatetimeField(default=datetime.utcnow)


class Business(Model):
    id = f.IntField(pk=True, index=True)
    business_name = f.CharField(max_length=200, null=False, unique=True)
    city = f.CharField(max_length=200, null=False, default="unspecified")
    region = f.CharField(max_length=200, null=False, default="unspecified")
    business_description = f.TextField(null=False)
    logo = f.CharField(max_length=200, null=False, default="default.jpg")
    owner = f.ForeignKeyField("models.User", related_name="business")


class Product(Model):
    id = f.IntField(pk=True, index=True)
    name = f.CharField(max_length=200, null=False, index=True)
    category = f.CharField(max_length=200, index=True)
    original_price = f.DecimalField(max_digits=12, decimal_places=2)
    new_price = f.DecimalField(max_digits=12, decimal_places=2)
    percentage_discount = f.IntField()
    offer_expiration_date = f.DatetimeField(default=datetime.utcnow)
    product_image = f.CharField(
        max_length=200, null=False, default="productDefault.jpg"
    )
    business = f.ForeignKeyField("models.Business", related_name="products")


# user
user_pydantic = pydantic_model_creator(User, name="User", exclude=("is_verified",))
user_pydanticIn = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
user_pydanticOut = pydantic_model_creator(User, name="UserOut", exclude=("password",))
# business
business_pydantic = pydantic_model_creator(Business, name="Business")
business_pydanticIn = pydantic_model_creator(
    Business, name="BusinessIn", exclude_readonly=True
)
# product
product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(
    Product, name="ProductIn", exclude=("percentage_discount", "id")
)
