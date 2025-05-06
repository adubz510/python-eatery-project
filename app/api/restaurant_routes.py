from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Restaurant

restaurant_routes = Blueprint('restaurants', __name__, url_prefix='/api/restaurants')

# GET all restaurants
@restaurant_routes.route('/', methods=['GET'])
def get_all_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants]), 200


# POST create a new restaurant
@restaurant_routes.route('/', methods=['POST'])
@login_required
def create_restaurant():
    data = request.get_json()

    new_restaurant = Restaurant(
        owner_id=current_user.id,
        name=data['name'],
        description=data['description'],
        category=data['category'],
        price_range=data.get('priceRange'),
        address=data['address'],
        city=data['city'],
        state=data['state'],
        zip_code=data['zipCode'],
        lat=data.get('lat'),
        lng=data.get('lng')
    )

    db.session.add(new_restaurant)
    db.session.commit()

    return new_restaurant.to_dict(), 201


# PUT update an existing restaurant
@restaurant_routes.route('/<int:restaurant_id>', methods=['PUT'])
@login_required
def update_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if restaurant.owner_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()

    restaurant.name = data.get('name', restaurant.name)
    restaurant.description = data.get('description', restaurant.description)
    restaurant.category = data.get('category', restaurant.category)
    restaurant.price_range = data.get('priceRange', restaurant.price_range)
    restaurant.address = data.get('address', restaurant.address)
    restaurant.city = data.get('city', restaurant.city)
    restaurant.state = data.get('state', restaurant.state)
    restaurant.zip_code = data.get('zipCode', restaurant.zip_code)
    restaurant.lat = data.get('lat', restaurant.lat)
    restaurant.lng = data.get('lng', restaurant.lng)

    db.session.commit()

    return restaurant.to_dict(), 200


# DELETE a restaurant
@restaurant_routes.route('/<int:restaurant_id>', methods=['DELETE'])
@login_required
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if restaurant.owner_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(restaurant)
    db.session.commit()

    return jsonify({'message': 'Restaurant deleted'}), 200