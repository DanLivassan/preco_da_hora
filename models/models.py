from pydantic import BaseModel
from datetime import datetime


class Store(BaseModel):
    name: str
    distance: float
    latitude: str
    longitude: str
    cep: str


class Product(BaseModel):
    description: str
    price: str
    found_date: datetime
    store: Store


class ProductBuilder:
    MAP_PRODUCT_JSON_FIELDS = {
        "product": "produto",
        "description": "descricao",
        "price": "precoLiquido",
        "found_date": "data"
    }
    MAP_STORE_JSON_FIELDS = {
        "store": "estabelecimento",
        "name": "nomeEstabelecimento",
        "distance": "distancia",
        "latitude": "latitude",
        "longitude": "longitude",
        "cep": "cep"
    }

    @staticmethod
    def by_json_raw(product_json_data, store_json_data) -> Product:
        store = Store(
            **{
                "name": store_json_data[ProductBuilder.MAP_STORE_JSON_FIELDS["name"]],
                "distance": store_json_data[ProductBuilder.MAP_STORE_JSON_FIELDS["distance"]],
                "latitude": store_json_data[ProductBuilder.MAP_STORE_JSON_FIELDS["latitude"]],
                "longitude": store_json_data[ProductBuilder.MAP_STORE_JSON_FIELDS["longitude"]],
                "cep": store_json_data[ProductBuilder.MAP_STORE_JSON_FIELDS["cep"]],
            }
        )
        product = Product(
            **{
                "description": product_json_data[ProductBuilder.MAP_PRODUCT_JSON_FIELDS["description"]],
                "price": product_json_data[ProductBuilder.MAP_PRODUCT_JSON_FIELDS["price"]],
                "found_date": product_json_data[ProductBuilder.MAP_PRODUCT_JSON_FIELDS["found_date"]],
                "store": store
            }
        )
        return product

    @staticmethod
    def by_json_collection(collection) -> [Product]:
        products = []
        for raw in collection["resultado"]:
            products.append(ProductBuilder.by_json_raw(
                raw[ProductBuilder.MAP_PRODUCT_JSON_FIELDS["product"]],
                raw[ProductBuilder.MAP_STORE_JSON_FIELDS["store"]],
            ))
        return products
