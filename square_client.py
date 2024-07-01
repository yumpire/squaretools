from square.client import Client
from dotenv import load_dotenv
import os

def get_square_client():
    load_dotenv()
    return Client(
        access_token=os.getenv('SQUARE_ACCESS_TOKEN'),
        environment='production'
    )