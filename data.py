from pymongo import MongoClient
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# MongoDB Connection URI
uri = 'mongodb://localhost:27017'
client = MongoClient(uri)

# Database Name
db_name = 'UserPrefsDB'
db = client[db_name]

# Data Generation Functions
def generate_feedback():
    return [{
        'feedback_id': i + 1,
        'user_id': random.randint(1, 354),
        'comment': fake.text(),
        'date': fake.date_time_this_decade()
    } for i in range(329)]

def generate_preference_categories():
    return [{
        'category_id': i + 1,
        'category_name': fake.bs()
    } for i in range(316)]

def generate_preferences():
    return [{
        'preference_id': i + 1,
        'category_id': random.randint(1, 316),
        'preference_type': fake.word(),
        'description': fake.sentence()
    } for i in range(344)]

def generate_products():
    return [{
        'product_id': i + 1,
        'product_name': fake.catch_phrase(),
        'category_id': random.randint(1, 316),
        'description': fake.text(),
        'price': round(random.uniform(10.0, 100.0), 2)
    } for i in range(348)]

def generate_user_preferences():
    return [{
        'user_preference_id': i + 1,
        'user_id': random.randint(1, 354),
        'preference_id': random.randint(1, 344),
        'value': fake.word()
    } for i in range(255)]

def generate_user_product_preferences():
    return [{
        'record_id': i + 1,
        'user_id': random.randint(1, 354),
        'product_id': random.randint(1, 348),
        'rating': random.randint(1, 5)
    } for i in range(126)]

def generate_users():
    return [{
        'user_id': i + 1,
        'username': fake.user_name(),
        'email': fake.email(),
        'registration_date': fake.date_between_dates(date_start=date(2000, 1, 1), date_end=date(2022, 1, 1)),
        'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=90),
        'country': fake.country()
    } for i in range(354)]

# Seeding Function
def seed_database():
    try:
        # Insert feedback data
        feedback_data = generate_feedback()
        db.feedback.insert_many(feedback_data)
        print('Feedback data inserted')

        # Insert preference categories data
        preference_categories_data = generate_preference_categories()
        db.preference_categories.insert_many(preference_categories_data)
        print('Preference Categories data inserted')

        # Insert preferences data
        preferences_data = generate_preferences()
        db.preferences.insert_many(preferences_data)
        print('Preferences data inserted')

        # Insert products data
        products_data = generate_products()
        db.products.insert_many(products_data)
        print('Products data inserted')

        # Insert user preferences data
        user_preferences_data = generate_user_preferences()
        db.user_preferences.insert_many(user_preferences_data)
        print('User Preferences data inserted')

        # Insert user product preferences data
        user_product_preferences_data = generate_user_product_preferences()
        db.user_product_preferences.insert_many(user_product_preferences_data)
        print('User Product Preferences data inserted')

        # Insert users data
        users_data = generate_users()
        db.users.insert_many(users_data)
        print('Users data inserted')

    except Exception as e:
        print('Error seeding data:', e)
    finally:
        client.close()
        print("Disconnected from database")

if __name__ == "__main__":
    print("Script is running...")
    seed_database()