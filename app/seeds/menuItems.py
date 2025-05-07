from app.models import db, MenuItem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_menu_items():
    # Joël Robuchon Menu Items (French cuisine)
    foie_gras = MenuItem(
        restaurant_id=1,
        name='Foie Gras',
        description='Delicately seared foie gras with fig jam and toast.',
        price=24.99
    )
    tasting_menu = MenuItem(
        restaurant_id=1,
        name='Tasting Menu',
        description='A multi-course tasting experience showcasing French culinary artistry.',
        price=99.99
    )
    lobster_ravioli = MenuItem(
        restaurant_id=1,
        name='Lobster Ravioli',
        description='Handmade ravioli filled with lobster, served in a rich cream sauce.',
        price=32.99
    )
    truffle_frites = MenuItem(
        restaurant_id=1,
        name='Truffle Frites',
        description='Crispy fries tossed in truffle oil and parmesan.',
        price=8.50
    )

    # Lotus of Siam Menu Items (Thai cuisine)
    pad_thai = MenuItem(
        restaurant_id=2,
        name='Pad Thai',
        description='Classic stir-fried rice noodles with shrimp, peanuts, and tamarind sauce.',
        price=13.50
    )
    green_curry = MenuItem(
        restaurant_id=2,
        name='Green Curry',
        description='Spicy coconut-based curry with chicken and vegetables.',
        price=14.75
    )
    thai_spring_rolls = MenuItem(
        restaurant_id=2,
        name='Thai Spring Rolls',
        description='Crispy spring rolls filled with vegetables and served with sweet chili sauce.',
        price=6.99
    )
    mango_sticky_rice = MenuItem(
        restaurant_id=2,
        name='Mango Sticky Rice',
        description='Sweet sticky rice paired with ripe mango and coconut milk.',
        price=7.25
    )

    # The Buffet at Wynn Menu Items (Buffet)
    seafood_platter = MenuItem(
        restaurant_id=3,
        name='Seafood Platter',
        description='A selection of shrimp, oysters, and crab legs.',
        price=29.99
    )
    prime_rib = MenuItem(
        restaurant_id=3,
        name='Prime Rib',
        description='Slow-roasted prime rib with au jus and horseradish.',
        price=22.50
    )
    sushi_rolls = MenuItem(
        restaurant_id=3,
        name='Sushi Rolls',
        description='A variety of sushi rolls including tuna, salmon, and crab.',
        price=18.99
    )
    mashed_potatoes = MenuItem(
        restaurant_id=3,
        name='Mashed Potatoes',
        description='Creamy mashed potatoes with garlic and chives.',
        price=5.99
    )

    # Carson Kitchen Menu Items (New American)
    fried_chicken = MenuItem(
        restaurant_id=4,
        name='Fried Chicken',
        description='Crispy fried chicken served with honey and hot sauce.',
        price=15.99
    )
    roasted_vegetables = MenuItem(
        restaurant_id=4,
        name='Roasted Vegetables',
        description='Seasonal vegetables roasted with herbs and olive oil.',
        price=8.50
    )
    short_ribs = MenuItem(
        restaurant_id=4,
        name='Short Ribs',
        description='Slow-braised short ribs with a rich red wine sauce.',
        price=22.50
    )
    sweet_potato_fries = MenuItem(
        restaurant_id=4,
        name='Sweet Potato Fries',
        description='Crispy sweet potato fries served with garlic aioli.',
        price=6.99
    )

    # Momofuku Menu Items (Asian Fusion)
    pork_belly_bao = MenuItem(
        restaurant_id=5,
        name='Pork Belly Bao',
        description='Soft steamed buns with tender pork belly, hoisin sauce, and cucumber.',
        price=9.75
    )
    ramen = MenuItem(
        restaurant_id=5,
        name='Ramen',
        description='Rich and flavorful ramen broth with noodles, egg, and pork belly.',
        price=12.50
    )
    spicy_tofu = MenuItem(
        restaurant_id=5,
        name='Spicy Tofu',
        description='Crispy tofu served in a spicy sauce with cilantro.',
        price=10.99
    )
    kimchi = MenuItem(
        restaurant_id=5,
        name='Kimchi',
        description='Fermented vegetables, mainly cabbage and radishes, with chili paste.',
        price=4.50
    )

    # In-N-Out Burger Menu Items (Fast Food)
    double_double = MenuItem(
        restaurant_id=6,
        name='Double-Double Burger',
        description='Two beef patties with American cheese, lettuce, tomato, and In-N-Out sauce.',
        price=7.50
    )
    animal_fries = MenuItem(
        restaurant_id=6,
        name='Animal Fries',
        description='Fries topped with melted cheese, grilled onions, and secret sauce.',
        price=4.95
    )
    milkshake_vanilla = MenuItem(
        restaurant_id=6,
        name='Vanilla Milkshake',
        description='Rich and creamy vanilla milkshake made with real ice cream.',
        price=5.00
    )
    cheeseburger = MenuItem(
        restaurant_id=6,
        name='Cheeseburger',
        description='Single beef patty with cheese, lettuce, tomato, and special sauce.',
        price=5.25
    )

    # Eataly Menu Items (Italian Marketplace)
    margherita_pizza = MenuItem(
        restaurant_id=7,
        name='Margherita Pizza',
        description='Classic pizza with tomato, mozzarella, and fresh basil.',
        price=12.99
    )
    tagliatelle_bolognese = MenuItem(
        restaurant_id=7,
        name='Tagliatelle Bolognese',
        description='Homemade pasta with rich meat sauce.',
        price=15.50
    )
    tiramisu = MenuItem(
        restaurant_id=7,
        name='Tiramisu',
        description='Classic Italian dessert with layers of coffee-soaked sponge and mascarpone.',
        price=7.99
    )
    bruschetta = MenuItem(
        restaurant_id=7,
        name='Bruschetta',
        description='Toasted bread topped with tomatoes, basil, and olive oil.',
        price=6.50
    )

    # Add all items to the session
    db.session.add_all([
        foie_gras, tasting_menu, lobster_ravioli, truffle_frites,
        pad_thai, green_curry, thai_spring_rolls, mango_sticky_rice,
        seafood_platter, prime_rib, sushi_rolls, mashed_potatoes,
        fried_chicken, roasted_vegetables, short_ribs, sweet_potato_fries,
        pork_belly_bao, ramen, spicy_tofu, kimchi,
        double_double, animal_fries, milkshake_vanilla, cheeseburger,
        margherita_pizza, tagliatelle_bolognese, tiramisu, bruschetta
    ])
    db.session.commit()

def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))

    db.session.commit()