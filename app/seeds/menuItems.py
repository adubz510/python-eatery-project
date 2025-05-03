from app.models import db, MenuItem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_menu_items():
    # Demo Diner Menu Items
    pancake_stack = MenuItem(
        restaurant_id=1,
        name='Pancake Stack',
        description='Fluffy pancakes served with maple syrup.',
        price=8.99
    )
    classic_burger = MenuItem(
        restaurant_id=1,
        name='Classic Burger',
        description='Beef patty with lettuce, tomato, and house sauce.',
        price=10.99
    )
    grilled_cheese = MenuItem(
        restaurant_id=1,
        name='Grilled Cheese',
        description='Cheddar cheese melted between sourdough.',
        price=6.50
    )
    milkshake = MenuItem(
        restaurant_id=1,
        name='Milkshake',
        description='Creamy vanilla milkshake with whipped cream.',
        price=4.99
    )
    chicken_tenders = MenuItem(
        restaurant_id=1,
        name='Chicken Tenders',
        description='Golden-fried chicken tenders with fries.',
        price=9.25
    )

    # Marnie’s Mediterranean Menu Items
    falafel_wrap = MenuItem(
        restaurant_id=2,
        name='Falafel Wrap',
        description='Chickpea patties wrapped with tahini sauce.',
        price=9.99
    )
    hummus_plate = MenuItem(
        restaurant_id=2,
        name='Hummus Plate',
        description='House-made hummus served with pita.',
        price=7.50
    )
    lamb_gyro = MenuItem(
        restaurant_id=2,
        name='Lamb Gyro',
        description='Spiced lamb in a warm pita with tzatziki.',
        price=11.25
    )
    greek_salad = MenuItem(
        restaurant_id=2,
        name='Greek Salad',
        description='Cucumber, tomato, feta, and olives.',
        price=8.25
    )
    baklava = MenuItem(
        restaurant_id=2,
        name='Baklava',
        description='Sweet pastry layered with nuts and honey.',
        price=5.50
    )

    # Bobbie’s BBQ Menu Items
    pulled_pork = MenuItem(
        restaurant_id=3,
        name='Pulled Pork Sandwich',
        description='Slow-cooked pork with BBQ sauce.',
        price=10.75
    )
    brisket_plate = MenuItem(
        restaurant_id=3,
        name='Brisket Plate',
        description='Tender smoked brisket with two sides.',
        price=14.99
    )
    bbq_ribs = MenuItem(
        restaurant_id=3,
        name='BBQ Ribs',
        description='Half rack of ribs with tangy sauce.',
        price=16.50
    )
    mac_cheese = MenuItem(
        restaurant_id=3,
        name='Mac & Cheese',
        description='Southern-style creamy mac and cheese.',
        price=6.99
    )
    coleslaw = MenuItem(
        restaurant_id=3,
        name='Coleslaw',
        description='Crunchy coleslaw with vinegar dressing.',
        price=3.25
    )

    # Tommy’s Zen Menu Items
    orange_chicken = MenuItem(
        restaurant_id=4,
        name='Orange Chicken',
        description='Crispy chicken tossed in orange sauce.',
        price=9.99
    )
    beef_lo_mein = MenuItem(
        restaurant_id=4,
        name='Beef Lo Mein',
        description='Stir-fried noodles with beef and veggies.',
        price=11.50
    )
    general_tsos = MenuItem(
        restaurant_id=4,
        name='General Tso\'s Chicken',
        description='Spicy-sweet glazed chicken.',
        price=10.75
    )
    spring_rolls = MenuItem(
        restaurant_id=4,
        name='Vegetable Spring Rolls',
        description='Crispy rolls filled with fresh veggies.',
        price=4.99
    )
    fried_rice = MenuItem(
        restaurant_id=4,
        name='Fried Rice',
        description='Classic egg fried rice with scallions.',
        price=6.50
    )

    # Sammy’s Ramen Menu Items
    tonkotsu_ramen = MenuItem(
        restaurant_id=5,
        name='Tonkotsu Ramen',
        description='Pork bone broth with chashu and egg.',
        price=13.50
    )
    shoyu_ramen = MenuItem(
        restaurant_id=5,
        name='Shoyu Ramen',
        description='Soy-based broth with bamboo shoots.',
        price=12.75
    )
    spicy_miso_ramen = MenuItem(
        restaurant_id=5,
        name='Spicy Miso Ramen',
        description='Rich miso broth with chili oil.',
        price=13.99
    )
    gyoza = MenuItem(
        restaurant_id=5,
        name='Gyoza',
        description='Pan-fried dumplings with pork filling.',
        price=6.25
    )
    seaweed_salad = MenuItem(
        restaurant_id=5,
        name='Seaweed Salad',
        description='Chilled seaweed with sesame oil.',
        price=4.95
    )

    db.session.add_all([
        pancake_stack, classic_burger, grilled_cheese, milkshake, chicken_tenders,
        falafel_wrap, hummus_plate, lamb_gyro, greek_salad, baklava,
        pulled_pork, brisket_plate, bbq_ribs, mac_cheese, coleslaw,
        orange_chicken, beef_lo_mein, general_tsos, spring_rolls, fried_rice,
        tonkotsu_ramen, shoyu_ramen, spicy_miso_ramen, gyoza, seaweed_salad
    ])
    db.session.commit()


def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))

    db.session.commit()