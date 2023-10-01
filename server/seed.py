from app import db
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Create sample restaurants
    restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
    restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')
    db.session.add_all([restaurant1, restaurant2])
    db.session.commit()

    # Create sample pizzas
    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
    db.session.add_all([pizza1, pizza2])
    db.session.commit()

    # Create sample restaurant pizzas
    restaurant_pizza1 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza1.id, price=10)
    restaurant_pizza2 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza2.id, price=12)
    restaurant_pizza3 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza2.id, price=8)
    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()

if __name__ == '__main__':
    seed_data()