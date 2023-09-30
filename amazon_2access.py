import requests
from bs4 import BeautifulSoup
from machine_mail import alert_system
import json

print("bonjour Chafi du 68")
URLS = [
    "https://www.amazon.fr/Logitech-Conf%C3%A9renceCam-Visioconf%C3%A9rence-Haut-Parleur-Personnalisables/dp/B071KBDVV5/ref=d_pb_allspark_purchase_sims_desktop_sccl_2_2/259-7387529-4215619?pd_rd_w=TGBIl&content-id=amzn1.sym.3c605f9b-1861-4c59-a786-b1b2901fc33b&pf_rd_p=3c605f9b-1861-4c59-a786-b1b2901fc33b&pf_rd_r=SHV3E9B1QD4VSETWC2W5&pd_rd_wg=d9q1i&pd_rd_r=1c45ad6e-969d-4742-bcb7-4a1e8c5b3ede&pd_rd_i=B071KBDVV5&psc=1",
    "https://www.amazon.fr/Sony-TV-Bravia-XR-65A80L-Playstation/dp/B0BYGXGX6Y/ref=sr_1_2_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=318I4CKFA4985&keywords=television&qid=1695159687&sprefix=television%2Caps%2C194&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
]
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "close"
}

set_price = 29800
prctsaisie = 100

# Charger le dictionnaire previous_prices à partir d'un fichier JSON s'il existe
try:
    with open('previous_prices.json', 'r') as file:
        previous_prices = json.load(file)
except FileNotFoundError:
    previous_prices = {}

def save_previous_prices():
    # Sauvegarder le dictionnaire previous_prices dans un fichier JSON
    with open('previous_prices.json', 'w') as file:
        json.dump(previous_prices, file)

def check_price():
    for URL in URLS:
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id='productTitle').get_text()
        price_element = soup.find(class_="a-offscreen")

        if price_element:
            price_text = price_element.get_text()
            product_price = float(''.join(filter(str.isdigit, price_text))) / 100.0  # Convertit le prix en float
            product_price = round(product_price, 2)
            print(f"Product: {title.strip()}")
            print(f"Current Price: ${product_price:.2f}")

            message1 = ""
            message2 = ""
            if product_price < set_price:
                message1 = f"[Le prix du produit est passé sous votre valeur seuil: {set_price}euros]"
            if title.strip() in previous_prices:
                base_price = previous_prices[title.strip()]
                prctvoulu = (1 - (prctsaisie * 0.01))
                prixmax = prctvoulu * base_price
                if product_price < prixmax:
                    message2 = f"Le prix du produit a diminué de {round((1 - product_price / base_price) * 100, 2)}%, plus que votre valeur seuil de {prctsaisie}%"
            if message1 or message2:
                alert_message = "\n".join([message for message in [message1, message2] if message])  # Combinez les messages non vides
                print(f"Envoi d'un e-mail avec le message : {alert_message}")
                alert_system(title.strip(), URL, product_price, alert_message)
                if title.strip() not in previous_prices:
                    # Si le produit n'est pas dans le dictionnaire, enregistrez le prix de base.
                    previous_prices[title.strip()] = product_price

# Exécutez la fonction check_price()
check_price()

# Sauvegardez le dictionnaire previous_prices après chaque exécution
save_previous_prices()
