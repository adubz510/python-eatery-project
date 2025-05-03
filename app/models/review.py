from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'reviews'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    restaurant = db.relationship("Restaurant", back_populates="reviews")
    user = db.relationship("User", back_populates="reviews")
    reviewImages = db.relationship("ReviewImage", back_populates="review", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'restaurantId': self.restaurant_id,
            'userId': self.user_id,
            'rating': self.rating,
            'comment': self.comment,
            'images': [image.url for image in self.reviewImages],
            'createdAt': self.created_at.isoformat()
        }