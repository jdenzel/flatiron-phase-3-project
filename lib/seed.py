from models import Item, Order, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    def menu_items():
        menu_items_list = [
            {"name": "Spring Rolls", "category": "Appetizer", "ingredients": "Rice paper, shrimp, lettuce, cucumber, vermicelli, mint leaves", "spice_level": 3, "price": 5.95},
            {"name": "Chicken Satay", "category": "Appetizer", "ingredients": "Chicken, peanut sauce", "spice_level": 2, "price": 8.95},
            {"name": "Green Papaya Salad", "category": "Appetizer", "ingredients": "Green papaya, carrots, peanuts, fish sauce, lime juice", "spice_level": 4, "price": 8.95},
            {"name": "Spicy Beef Salad", "category": "Appetizer", "ingredients": "Beef, cucumber, tomatoes, onions, fish sauce, lime juice", "spice_level": 4, "price": 8.95},
            {"name": "Pad Thai", "category": "Entree", "ingredients": "Rice noodles, shrimp, tofu, egg, bean sprouts, peanuts", "spice_level": 3, "price": 14.95},
            {"name": "Pad See Ew", "category": "Entree", "ingredients": "Rice noodles, chicken, egg, broccoli, carrots", "spice_level": 2,"price": 14.95},
            {"name": "Drunken Noodles", "category": "Entree", "ingredients": "Rice noodles, chicken, egg, bell peppers, onions, basil", "spice_level": 2, "price": 14.95},
            {"name": "Pad Kaprow", "category": "Entree", "ingredients": "Chicken, bell peppers, onions, basil", "spice_level": 2, "price": 14.95},
            {"name": "Red Curry", "category": "Entree", "ingredients": "Chicken, bamboo shoots, bell peppers, basil", "spice_level": 3, "price": 14.95},
            {"name": "Green Curry", "category": "Entree", "ingredients": "Chicken, bamboo shoots, bell peppers, basil", "spice_level": 3, "price": 14.95},
            {"name": "Mango with Sticky Rice", "category": "Dessert", "ingredients": "Mango, sticky rice, coconut milk", "spice_level": 1, "price": 5.95},
            {"name": "Fried Ice Cream", "category": "Dessert", "ingredients": "Ice cream, corn flakes, coconut flakes", "spice_level": 1, "price": 5.95},
            {"name": "Thai Iced Tea", "category": "Drinks", "ingredients": "Thai tea, milk, sugar", "spice_level": 1, "price": 3.95},
            {"name": "Thai Iced Coffee", "category": "Drinks", "ingredients": "Coffee, milk, sugar", "spice_level": 1, "price": 3.95}
        ]

        for item in menu_items_list:
            new_item = Item(name=item["name"], category=item["category"], ingredients=item["ingredients"], spice_level=item["spice_level"], price=item["price"])
            session.add(new_item)
            session.commit()
        
    menu_items()

    while True:
        print("Welcome to Slice and Dice Thai Food!")
        print("What would you like to do?")
        print("1. Place an order")
        print("3. Sign up for our rewards program")
        print("4. Write a review")
        print("5. Quit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                break
            if choice == 2:
                break
            if choice == 3:
                break
            if choice == 4:
                break
            if choice == 5:
                break
        except ValueError:
            print("Not a valid choice. Enter again.")

    
        

            

