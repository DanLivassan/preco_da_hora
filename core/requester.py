
import requests
from lxml import html
from icecream import ic
import json


class PHRequester:
    BASE_URL = "https://precodahora.ba.gov.br/produtos/"

    def get_products(self, procuct_name):
        session = requests.Session()
        response = session.get(PHRequester.BASE_URL)
        tree = html.fromstring(response.content)
        csrf = tree.xpath('//input[@name="csrf_token"]/@value')
        session.headers.update({"X-CSRFToken": csrf[0]})
        data = {
            "termo": procuct_name,
            "horas": "72",
            "latitude": "-12.97111",
            "longitude": "-38.51083",
            "raio": "15",
            "pagina": "1",
            "ordenar": "preco.asc"
        }
        content = session.post(PHRequester.BASE_URL, data=data)

        return json.loads(content.text)


