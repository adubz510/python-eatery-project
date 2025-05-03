from app.models import db, ReviewImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_review_images():
    image1 = ReviewImage(review_id=1, url="https://example.com/review1_img1.jpg")
    image2 = ReviewImage(review_id=2, url="https://example.com/review2_img1.jpg")
    image3 = ReviewImage(review_id=3, url="https://example.com/review3_img1.jpg")

    image4 = ReviewImage(review_id=4, url="https://example.com/review4_img1.jpg")
    image5 = ReviewImage(review_id=5, url="https://example.com/review5_img1.jpg")
    image6 = ReviewImage(review_id=6, url="https://example.com/review6_img1.jpg")

    image7 = ReviewImage(review_id=7, url="https://example.com/review7_img1.jpg")
    image8 = ReviewImage(review_id=8, url="https://example.com/review8_img1.jpg")
    image9 = ReviewImage(review_id=9, url="https://example.com/review9_img1.jpg")

    image10 = ReviewImage(review_id=10, url="https://example.com/review10_img1.jpg")
    image11 = ReviewImage(review_id=11, url="https://example.com/review11_img1.jpg")
    image12 = ReviewImage(review_id=12, url="https://example.com/review12_img1.jpg")

    image13 = ReviewImage(review_id=13, url="https://example.com/review13_img1.jpg")
    image14 = ReviewImage(review_id=14, url="https://example.com/review14_img1.jpg")
    image15 = ReviewImage(review_id=15, url="https://example.com/review15_img1.jpg")

    db.session.add_all([
        image1, image2, image3,
        image4, image5, image6,
        image7, image8, image9,
        image10, image11, image12,
        image13, image14, image15
    ])
    db.session.commit()


def undo_review_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.review_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM review_images"))

    db.session.commit()