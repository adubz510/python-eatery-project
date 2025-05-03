from app.models import db, Image, environment, SCHEMA
from sqlalchemy.sql import text

def seed_images():
    # Demo Diner Images
    demo_img1 = Image(
        url='https://example.com/demo1.jpg',
        restaurant_id=1,
        user_id=1
    )
    demo_img2 = Image(
        url='https://example.com/demo2.jpg',
        restaurant_id=1,
        user_id=1
    )
    demo_img3 = Image(
        url='https://example.com/demo3.jpg',
        restaurant_id=1,
        user_id=1
    )

    # Marnie's Mediterranean Images
    marnie_img1 = Image(
        url='https://example.com/med1.jpg',
        restaurant_id=2,
        user_id=2
    )
    marnie_img2 = Image(
        url='https://example.com/med2.jpg',
        restaurant_id=2,
        user_id=2
    )
    marnie_img3 = Image(
        url='https://example.com/med3.jpg',
        restaurant_id=2,
        user_id=2
    )

    # Bobbie's BBQ Images
    bobbie_img1 = Image(
        url='https://example.com/bbq1.jpg',
        restaurant_id=3,
        user_id=3
    )
    bobbie_img2 = Image(
        url='https://example.com/bbq2.jpg',
        restaurant_id=3,
        user_id=3
    )
    bobbie_img3 = Image(
        url='https://example.com/bbq3.jpg',
        restaurant_id=3,
        user_id=3
    )

    # Tommy's Zen Images
    tommy_img1 = Image(
        url='https://example.com/zen1.jpg',
        restaurant_id=4,
        user_id=4
    )
    tommy_img2 = Image(
        url='https://example.com/zen2.jpg',
        restaurant_id=4,
        user_id=4
    )
    tommy_img3 = Image(
        url='https://example.com/zen3.jpg',
        restaurant_id=4,
        user_id=4
    )

    # Sammy's Ramen Images
    sammy_img1 = Image(
        url='https://example.com/ramen1.jpg',
        restaurant_id=5,
        user_id=5
    )
    sammy_img2 = Image(
        url='https://example.com/ramen2.jpg',
        restaurant_id=5,
        user_id=5
    )
    sammy_img3 = Image(
        url='https://example.com/ramen3.jpg',
        restaurant_id=5,
        user_id=5
    )

    db.session.add_all([
        demo_img1, demo_img2, demo_img3,
        marnie_img1, marnie_img2, marnie_img3,
        bobbie_img1, bobbie_img2, bobbie_img3,
        tommy_img1, tommy_img2, tommy_img3,
        sammy_img1, sammy_img2, sammy_img3
    ])
    db.session.commit()


def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()
