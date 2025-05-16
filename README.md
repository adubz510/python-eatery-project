# UBEREATS

# Live Site


## Summary

This is a full-stack clone of UberEats, a food delivery and restaurant ordering platform. The project allows users to browse restaurants, view detailed menus, add items to a shopping cart, and place orders. Core features include user authentication, restaurant and menu item CRUD functionality, real-time cart management, and a responsive search system. Users can also leave reviews for restaurants, view past orders, and quickly reorder from previous purchases. 


## 🔧 Features
### User Authentication
- Signup, login, and logout functionality
- Demo user login for quick access
- Protected routes based on user session

### 🍽️ Restaurants
- Full CRUD (Create, Read, Update, Delete) for restaurant listings
- Each restaurant includes name, description, category, address, and price range

### 📋 Menus
- Restaurants have associated menu items
- Full CRUD for menu items (e.g., dish name, description, price, image)
- Menu items displayed on individual restaurant pages

### ⭐ Reviews
- Logged-in users can leave, edit, and delete reviews for restaurants
- Reviews include star rating and written feedback
- Average star ratings displayed per restaurant


### 🔍 Search
- Search bar with keyword matching for restaurant names and categories
- Results displayed in a clean, responsive layout

### 📱 Modals
- ustom modals for login, signup, and adding/editing content
- Seamless user experience without full-page reloads

### 🌐 Responsive Design
- Styled with a modern, clean layout using CSS and component-based design


## 📂 API Routes

### Auth
- `GET /api/auth/` — restore session
- `POST /api/auth/login` — login
- `POST /api/auth/signup` — signup
- `POST /api/auth/logout` — logout

### 👤 User Routes
- `GET /api/users/` — get all users (login required)
- `GET /api/users/<id>` — get a specific user by ID (login required)

### 🍽️ Restaurant Routes
- `GET /api/restaurants/` — get all restaurants
- `GET /api/restaurants/<restaurant_id> `— get a single restaurant by ID
- `GET /api/restaurants/my-restaurants` — get all restaurants owned by the current user (login required)
- `POST /api/restaurants/` — create a new restaurant (login required)
- `PUT /api/restaurants/<restaurant_id>` — update an existing restaurant (login required & must be owner)
- `DELETE /api/restaurants/<restaurant_id>` — delete a restaurant (login required & must be owner)

### 🍽️ Menu Item Routes
- `GET /api/menu_items/restaurant/<restaurant_id>` — get all menu items for a specific restaurant
- `POST /api/menu_items/restaurant/<restaurant_id>` — create a new menu item for a specific restaurant
- `PATCH /api/menu_items/<menu_item_id>` — update a specific menu item
- `DELETE /api/menu_items/<menu_item_id>` — delete a specific menu item

### 📝 Review Routes
- `GET /api/reviews/restaurant/<restaurant_id>` — get all reviews for a restaurant
- `POST /api/reviews/restaurant/<restaurant_id> `— create a new review for a restaurant (login required)
- `PATCH /api/reviews/<review_id>` — update a review (login required & must be the review author)
- `DELETE /api/reviews/<review_id>` — delete a review (login required & must be the review author)

### 🗃 Database Schema
- User: id, username, email, hashed_password
- Restaurant: id, owner_id, name, description, category, price_range, address, city, state, zip_code, lat, lng
- Image: id, url, restaurant_id, user_id
- MenuItem: id, restaurant_id, name, description, price, image_url
- Review: id, restaurant_id, user_id, rating, comment, created_at, updated_at


