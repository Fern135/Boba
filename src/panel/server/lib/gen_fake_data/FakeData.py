from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
import requests
import random

from ...Login.models import Product, ProductImage
from ..util.util import error, success, warning

from faker.providers import internet
from faker import Faker

fake = Faker()
Faker.seed(random.randint(1, 1000000))
fake.add_provider(internet)

FAKE_DATA = {
    "name"       : fake.name(),
    "address"    : fake.address(),
    "emai"       : fake.email(),
    "phone_num"  : fake.phone_number(),
    "job"        : fake.job(),
    "credit_card": fake.credit_card_number(),
    "text"       : fake.text(),
    "text"       : fake.sentence(),
    "ipv4"       : fake.ipv4_private(),
}

pic_width, pic_height = 900, 900

#region individual functions for the dict above
def gen_name():
    return fake.name()

def gen_address():
    return fake.address()

def gen_email():
    return fake.email()

def gen_phone_num():
    return fake.phone_number()

def gen_job():
    return fake.job()   

def gen_credit_card_num():
    return fake.credit_card_number()

def gen_text():
    return fake.text()

def gen_sentence():
    return fake.sentence()

def gen_ipv4_private():
    return fake.ipv4_private()

#endregion

def gen_image(image_nums:int) -> None:
    try:
        for _ in range(image_nums + 1):
            url = f"https://picsum.photos/{pic_width}/{pic_height}"  # Replace with the URL of the website you want to scrape

            response    = requests.get(url)
            soup        = BeautifulSoup(response.text, "html.parser")

            images = soup.find_all("img")  # Find all <img> tags on the page

            for image in images:
                image_url = image["src"]  # Get the URL of the image
                image_response = requests.get(image_url)  # Send a request to download the image

                filename = image_url.split("/")[-1]  # Extract the filename from the URL

                # Save the image to ProductImage model
                product_image = ProductImage()

                # product_image.product_id = <your_product_id>  # Replace <your_product_id> with the actual product ID
                product_image.image.save(filename, ContentFile(image_response.content), save=True) # seems to save

                # Save the image to Product model
                # product = Product.objects.get(pk=<your_product_id>)  # Replace <your_product_id> with the actual product ID
                # product_image = ProductImage(product=product)
                product_image.image.save(filename, ContentFile(image_response.content), save=True)

                print(f"Image '{filename}' saved to Product and ProductImage models.")

    except Exception as Error:
        print(f"{error} * error occured at gen_image: {str(Error)}")