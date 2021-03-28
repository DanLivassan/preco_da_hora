from core.requester import PHRequester
from models.models import Product, ProductBuilder, Store
from mail.email_sender import EmailSender
from icecream import ic


if __name__ == "__main__":
    requester = PHRequester()
    products = ProductBuilder.by_json_collection(requester.get_products("Maturada"))

    EmailSender.send_products([product.dict() for product in products])