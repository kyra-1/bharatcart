# generator/generate_data.py

from faker import Faker
import pandas as pd
import random
from tqdm import tqdm
import uuid
from datetime import timedelta
import os

fake = Faker('en_IN')
random.seed(42)

NUM_USERS = 10000
NUM_PRODUCTS = 1000
NUM_SELLERS = 500
NUM_EVENTS = 500000  # increase to 5M later


# ---------------------- USERS ----------------------
def generate_users():
    users = []
    for _ in range(NUM_USERS):
        users.append({
            'user_id': str(uuid.uuid4()),
            'age': random.randint(18, 60),
            'gender': random.choice(['F', 'M']),
            'signup_source': random.choice(['organic', 'referral', 'ad']),
            'city': fake.city()
        })
    return pd.DataFrame(users)


# ---------------------- SELLERS ----------------------
def generate_sellers():
    sellers = []
    for _ in range(NUM_SELLERS):
        sellers.append({
            'seller_id': str(uuid.uuid4()),
            'city': fake.city(),
            'fulfillment_type': random.choice(['Meesho F', 'Self', '3P Fulfillment']),
            'onboard_date': fake.date_between(start_date='-2y', end_date='-6m')
        })
    return pd.DataFrame(sellers)


# ---------------------- PRODUCTS ----------------------
def generate_products(sellers_df):
    categories = ['Apparel', 'Home', 'Kitchen', 'Beauty', 'Electronics']
    products = []
    for _ in range(NUM_PRODUCTS):
        products.append({
            'product_id': str(uuid.uuid4()),
            'category': random.choice(categories),
            'price': random.randint(100, 2000),
            'rating': round(random.uniform(2.0, 5.0), 1),
            'seller_id': random.choice(sellers_df['seller_id'].tolist())
        })
    return pd.DataFrame(products)


# ---------------------- EVENTS ----------------------
def generate_events(users_df, products_df):
    events = []
    event_types = ['view', 'cart', 'buy', 'return']

    for _ in tqdm(range(NUM_EVENTS)):
        user = users_df.sample().iloc[0]
        product = products_df.sample().iloc[0]
        base_time = fake.date_time_between(start_date='-60d', end_date='now')

        stage = random.choices(['view', 'cart', 'buy', 'return'], weights=[50, 25, 20, 5])[0]

        # simulate funnel timestamps (optional)
        events.append({
            'event_id': str(uuid.uuid4()),
            'user_id': user['user_id'],
            'product_id': product['product_id'],
            'seller_id': product['seller_id'],
            'category': product['category'],
            'event_type': stage,
            'timestamp': base_time + timedelta(minutes=random.randint(0, 60)),
            'city': user['city']
        })
    return pd.DataFrame(events)


# ---------------------- MAIN ----------------------
def main():
    print("Generating data...")

    users_df = generate_users()
    sellers_df = generate_sellers()
    products_df = generate_products(sellers_df)
    events_df = generate_events(users_df, products_df)

    os.makedirs("data", exist_ok=True)
    users_df.to_csv("data/users.csv", index=False)
    sellers_df.to_csv("data/sellers.csv", index=False)
    products_df.to_csv("data/products.csv", index=False)
    events_df.to_csv("data/events.csv", index=False)

    print("✅ Done! Data saved in /data folder.")


if __name__ == "__main__":
    main()
