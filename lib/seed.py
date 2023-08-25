from models import Item, Order, Customer, Review, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Item).delete()
    session.commit()

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

    print("Welcome to Slice and Dice Thai Food!")
    customer_name = input("Please enter your name: ")
    customer_phone_number = input("Please enter your phone number: ")
    existing_customer = session.query(Customer).filter_by(name=customer_name, phone_number=customer_phone_number).first()

    if existing_customer:
        print(f"Welcome back {existing_customer.name}!")
        customer = existing_customer
    else:
        print("It looks like you are a new customer. Welcome!")
        customer = Customer(name=customer_name, phone_number=customer_phone_number)
        session.add(customer)
        session.commit()

    while True:
        def show_menu(items):
            for item in items:
                print(f"{item.id}: {item.name} - {item.price}")
        
        def place_order(items):
            show_menu(items)

            order_items = []
            order_price = 0

            while True:
                
                order_input = input("Enter the item number: . Enter 0 to finish your order: ")
                if order_input == "0":
                    break

                try:
                    item_number = int(order_input)
                    item = session.query(Item).filter_by(id=item_number).first()
                    if item:
                        order_items.append(item)
                        print(f"{item} has been added to your order.")
                except ValueError:
                    print("Not a valid item number. Enter again or enter 0.")

            for item in order_items:
                order_price += item.price

            print("Your ordered:")
            for item in order_items:
                print(item.name)
            print("Your total price is:")
            print(order_price)

            order_item_names = ", ".join(item.name for item in order_items) 

            new_order = Order(items=order_item_names, total_price=order_price, customer_id=customer.id)
            session.add(new_order)
            session.commit()

        def write_review():
            print("Give us a Review!")

            rating = int(input("Rate our restaurant from 1 to 5:"))
            comment = input("Tell us what you thought:")

            print(f"Thank you for your review {customer_name}!")

            new_review = Review(rating=rating, comment=comment, customer_id=customer.id)
            session.add(new_review)
            session.commit()
        
        def view_history():
            if customer.history:
                print("Order history:")
                for orders in customer.history:
                    print(f"Order ID: {orders.id}")
                    print(f"Items ordered: {orders.order_items}")
                    print(f"Order total:  {orders.total}")
                else:
                    print("It seems like you haven't ordered from us yet")
            

        try:
            print("Menu")
            print("-" * 30)
            print("What would you like to do?")
            print("1. Place an order")
            print("2. Write a review")
            print("3. View order history")
            print("4. Quit") 
            choice = int(input("Please choose from one of the following choices: "))
            
            if choice == 1:
                items = session.query(Item).all()
                place_order(items)
            elif choice == 2:
                write_review()
            elif choice == 3:
                view_history()
            elif choice == 4:
                print("Thank you for stopping by Slice and Dice Thai Food!")
                break
        except ValueError:
            print("Not a valid choice. Enter again.")

        

    
        

            

