import pandas as pd
from faker import Faker
from datetime import datetime
import random
import csv
import io

fake = Faker()

def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + (end - start) * random.random()

def gen_json_list_single_order():

    order = {
        "order_id": fake.random_int(min=1000, max=9999),
        "store_id": fake.random_int(min=1, max=20),
        "order_date": random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)).strftime('%Y-%m-%dT%H:%M:%S'),
        "customer": {
            "customer_id": fake.random_int(min=100, max=999),
            "name": fake.name(),
            "email": fake.email()
        },
        "items": []
    }

    for _ in range(fake.random_int(min=1, max=5)):
        item = {
            "product_id": fake.random_int(min=1, max=25),
            "product_name": fake.word(),
            "quantity": fake.random_int(min=1, max=10),
            "price": round(random.uniform(5.0, 50.0), 2)
        }
        order["items"].append(item)

    return order


def gen_json_list_multiple_orders(p_num_orders):
    l_data = ""
    for c in range(p_num_orders):
        l_data = l_data + gen_json_list_single_order()
    
    return l_data


def gen_csv_list_single_order():

    order = {
        "order_id": fake.random_int(min=1000, max=9999),
        "store_id": fake.random_int(min=1, max=20),
        "order_date": random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)).strftime('%Y-%m-%dT%H:%M:%S'),
        "customer_id": fake.random_int(min=100, max=999),
        "name": fake.name(),
        "email": fake.email(),
        "product_id": fake.random_int(min=1, max=25),
        "quantity": fake.random_int(min=1, max=10)
        }

    return order


def gen_csv_list_multiple_orders(p_num_orders):
    l_data = []
    for c in range(p_num_orders):
        l_data.append(gen_csv_list_single_order())
    
    return l_data

