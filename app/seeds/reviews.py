from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_reviews():
    review_1 = Review(
        restaurant_id=1,
        user_id=2,
        rating=5,
        comment='Absolutely loved the pancakes here! Classic diner vibes.',
        created_at=datetime.now()
    )

    review_2 = Review(
        restaurant_id=1,
        user_id=3,
        rating=4,
        comment='Great food and fast service.',
        created_at=datetime.now()
    )

    review_3 = Review(
        restaurant_id=1,
        user_id=4,
        rating=3,
        comment='Decent breakfast, but a bit crowded.',
        created_at=datetime.now()
    )

    review_4 = Review(
        restaurant_id=2,
        user_id=1,
        rating=5,
        comment='Amazing falafel and hummus!',
        created_at=datetime.now()
    )

    review_5 = Review(
        restaurant_id=2,
        user_id=3,
        rating=4,
        comment='Fresh ingredients and big portions.',
        created_at=datetime.now()
    )

    review_6 = Review(
        restaurant_id=2,
        user_id=5,
        rating=4,
        comment='One of the best Mediterranean spots in LA.',
        created_at=datetime.now()
    )

    review_7 = Review(
        restaurant_id=3,
        user_id=1,
        rating=4,
        comment='Brisket was tender and flavorful.',
        created_at=datetime.now()
    )

    review_8 = Review(
        restaurant_id=3,
        user_id=2,
        rating=3,
        comment='Sides were a little underwhelming.',
        created_at=datetime.now()
    )

    review_9 = Review(
        restaurant_id=3,
        user_id=5,
        rating=5,
        comment='BBQ sauce is out of this world!',
        created_at=datetime.now()
    )

    review_10 = Review(
        restaurant_id=4,
        user_id=1,
        rating=2,
        comment='Below average fast chinese food take-out. Not a fan.',
        created_at=datetime.now()
    )

    review_11 = Review(
        restaurant_id=4,
        user_id=2,
        rating=3,
        comment='Good prices, decent portions.',
        created_at=datetime.now()
    )

    review_12 = Review(
        restaurant_id=4,
        user_id=3,
        rating=4,
        comment='Love the lo mein! Always hot and fresh.',
        created_at=datetime.now()
    )

    review_13 = Review(
        restaurant_id=5,
        user_id=1,
        rating=5,
        comment='Rich broth and chewy noodles, excellent ramen!',
        created_at=datetime.now()
    )

    review_14 = Review(
        restaurant_id=5,
        user_id=2,
        rating=4,
        comment='Perfect after a long day in Vegas.',
        created_at=datetime.now()
    )

    review_15 = Review(
        restaurant_id=5,
        user_id=3,
        rating=4,
        comment='Authentic flavors, friendly staff.',
        created_at=datetime.now()
    )

    db.session.add_all([
        review_1, review_2, review_3,
        review_4, review_5, review_6,
        review_7, review_8, review_9,
        review_10, review_11, review_12,
        review_13, review_14, review_15
    ])
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
    db.session.commit()