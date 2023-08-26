from models import Item, Order, Customer, Review, History, Base
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
            {"name": "Spring Rolls", "category": "Appetizer", "description": "Crispy spring rolls served with sweet chili sauce", "spice_level": 3, "price": 5.95},
            {"name": "Chicken Satay", "category": "Appetizer", "description": "Grilled chicken breast in a satay sauce served with our own special peanut sauce. Served with a cucumber relish", "spice_level": 2, "price": 8.95},
            {"name": "Green Papaya Salad", "category": "Appetizer", "description": "Julienne crispy papaya, fresh vegetables, shrimp and peanuts served with a spicy lime dressing", "spice_level": 4, "price": 8.95},
            {"name": "Spicy Beef Salad", "category": "Appetizer", "description": "Grilled beef, cucumbers, red onions and cilantro mixed with a spicy lime dressing", "spice_level": 4, "price": 8.95},
            {"name": "Pad Thai", "category": "Entree", "description": "Famous Thai rice noodles, egg, scallions and bean sprouts topped with ground roasted peanuts. Prepared as a mild dish, appropriate for people who do not like spicy food.", "spice_level": 1, "price": 14.95},
            {"name": "Pad See Ew", "category": "Entree", "description": "Pan fried rice noodles, egg and broccoli in light soy sauce.", "spice_level": 2,"price": 14.95},
            {"name": "Drunken Noodles", "category": "Entree", "description": "Stir-fried flat rice noodles, egg, Chinese Broccoli leaf, cabbage, tomatoes, and broccoli in a flavorful spicy brown basil sauce garnished with fresh basil leaves.", "spice_level": 2, "price": 14.95},
            {"name": "Pad Kaprow", "category": "Entree", "description": "Sautéed chicken, string beans, carrots, sweet onions, and bell peppers in an authentic Thai basil sauce. Served with jasmine rice.", "spice_level": 2, "price": 14.95},
            {"name": "Red Curry", "category": "Entree", "description": "Homemade red curry cooked with coconut milk, carrots, string beans, bell peppers, bamboo shoots and fresh Thai basil leaves. Served with jasmine rice.", "spice_level": 3, "price": 14.95},
            {"name": "Green Curry", "category": "Entree", "description": "Homemade fresh green curry cooked with coconut milk, carrots, eggplant, bamboo shoots and string beans. Served with jasmine rice.", "spice_level": 3, "price": 14.95},
            {"name": "Mango with Sticky Rice", "category": "Dessert", "description": "Mango, sweet sticky rice, with a drizzle of coconut milk, and a sprinkle of roasted sesame seeds", "spice_level": 1, "price": 5.95},
            {"name": "Fried Ice Cream", "category": "Dessert", "description": "Deep fried vanilla ice cream combined with corn flakes and coconut flakes", "spice_level": 1, "price": 5.95},
            {"name": "Thai Iced Tea", "category": "Drinks", "description": "Homemade Thai tea", "spice_level": 1, "price": 3.95},
            {"name": "Thai Iced Coffee", "category": "Drinks", "description": "Homemade Thai coffee", "spice_level": 1, "price": 3.95}
        ]

        for item in menu_items_list:
            new_item = Item(name=item["name"], category=item["category"], description=item["description"], spice_level=item["spice_level"], price=item["price"])
            session.add(new_item)
            session.commit()
            
    menu_items()

    print("-" * 40)
    print("Welcome to Slice and Dice Thai Food!")
    print("-" * 40)
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
            current_category = None
            for item in items:
                if item.category != current_category:
                    current_category = item.category
                    print(f"\n{current_category}")
                    print("-" * 40)
                print(f"{item.id}: {item.name} - {item.price} \nIngredients: {item.ingredients} \nSpice level: {item.spice_level} \n")
        
        def place_order(items):
            show_menu(items)
            order_items = []
            order_price = 0

            while True:
                
                order_input = input("Enter the item number or enter 0 to finish your order: ")
                if order_input == "0":
                    break

                try:
                    item_number = int(order_input)
                    item = session.query(Item).filter_by(id=item_number).first()
                    if item:
                        order_items.append(item)
                        print(f"{item.name} has been added to your order.")
                except ValueError:
                    print("Not a valid item number. Enter again or enter 0.")

            for item in order_items:
                order_price += item.price

            if order_items is None:
                print("You ordered 0 items")
            else:
                print("\nYou ordered: ")
                for item in order_items:
                    print(item.name)

            print(f"\nYour total price is: {order_price}")

            order_item_names = ", ".join(item.name for item in order_items) 

            new_order = Order(items=order_item_names, total_price=order_price, customer_id=customer.id)
            session.add(new_order)
            session.commit()

            new_history = History(order_items=order_item_names, total=order_price, customer_id=customer.id)
            session.add(new_history)
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

            # new_restaurant_review = RestaurantR()

        # def see_restaurant_reviews():


        try:
            print("-" * 40)
            print("What would you like to do?")
            print("1. Place an order")
            print("2. Write a review")
            print("3. View order history")
            print("4. Quit") 
            print("-" * 40)
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
        print("-" * 40)
        print('\n')

        

    
        

            

