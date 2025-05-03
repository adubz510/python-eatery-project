from app.models import db, Restaurant, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_restaurants():
    demo_restaurant = Restaurant(
        owner_id=1,
        name='Demo Diner',
        description='Classic American diner with all-day breakfast.',
        category='American',
        price_range='$$',
        address='123 Main St',
        city='Boston',
        state='MA',
        zip_code='02108',
        lat=42.3601,
        lng=-71.0589
    )

    marnie_restaurant = Restaurant(
        owner_id=2,
        name='Marnie\'s Mediterranean',
        description='Fresh Mediterranean food with vegan options.',
        category='Mediterranean',
        price_range='$$$',
        address='456 Sunset Blvd',
        city='Los Angeles',
        state='CA',
        zip_code='90026',
        lat=34.0900,
        lng=-118.3000
    )

    bobbie_restaurant = Restaurant(
        owner_id=3,
        name='Bobbie\'s BBQ',
        description='Smoked meats and southern-style sides.',
        category='BBQ',
        price_range='$$',
        address='789 Broadway',
        city='New York',
        state='NY',
        zip_code='10003',
        lat=40.7306,
        lng=-73.9352
    )
    
    tommy_restaurant = Restaurant(
        owner_id=4,
        name='Tommy\'s Zen',
        description='Quick and fast chinese food.',
        category='Chinese',
        price_range='$',
        address='123 Laurel Street',
        city='San Francisco',
        state='CA',
        zip_code='94107',
        lat=37.7749,
        lng=-122.4194
    )

    sammy_restaurant = Restaurant(
        owner_id=5,
        name='Sammy\'s Ramen',
        description='Authentic Japanese ramen made with care and tradition.',
        category='Japanese',
        price_range='$$',
        address='456 Roy Blvd',
        city='Las Vegas',
        state='NV',
        zip_code='89109',
        lat=36.1699,
        lng=-115.1398
    )

    db.session.add(demo_restaurant)
    db.session.add(marnie_restaurant)
    db.session.add(bobbie_restaurant)
    db.session.add(tommy_restaurant)
    db.session.add(sammy_restaurant)
    db.session.commit()


def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))

    db.session.commit()