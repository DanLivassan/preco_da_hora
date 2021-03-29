from core.requester import PHRequester
from models.models import ProductBuilder
from mail.email_sender import EmailSender
import sys

if __name__ == "__main__":
    search = sys.argv[1]
    requester = PHRequester()
    products = ProductBuilder.by_json_collection(requester.get_products(search))
    EmailSender.send_products(search, [product.dict() for product in products], "daniloxc@msn.com")