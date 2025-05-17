from .db import db, environment, SCHEMA, add_prefix_for_prod

class Cart(db.Model):
    __tablename__ = 'carts'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("users.id")),
        nullable=False,
        unique=True  # 1 cart per user
    )
    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("restaurants.id")),  # Use prefix here for consistency
        nullable=True
    )

    user = db.relationship("User", back_populates="cart")
    cart_items = db.relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")
    restaurant = db.relationship("Restaurant", back_populates="carts")  # 👈 Add back_populates

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'restaurantId': self.restaurant_id,
            'cartItems': [item.to_dict() for item in self.cart_items]
        }