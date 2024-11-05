import sqlite3

# Initialize SQLite database and tables
def init_db():
    con = sqlite3.connect('Houseofchocloates.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        flavor_name TEXT NOT NULL,
                        season TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ingredient_name TEXT NOT NULL,
                        quantity INTEGER NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT,
                        flavor_suggestion TEXT,
                        allergy_concern TEXT
                    )''')
    con.commit()

    con.close()

def add_seasonal_flavor():
    flavor_name = input("Enter the flavor name: ")
    season = input("Enter the season (e.g., Spring, Summer, etc.): ")
    con = sqlite3.connect('Houseofchocloates.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO seasonal_flavors (flavor_name, season) VALUES (?, ?)", (flavor_name, season))
    con.commit()
    con.close()
    print(f"Seasonal flavor '{flavor_name}' for {season} season added.")

def view_seasonal_flavors():
    con = sqlite3.connect('Houseofchocloates.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    con.close()
    if flavors:
        print("\nSeasonal Flavors:")
        for flavor in flavors:
            print(f"ID: {flavor[0]}, Flavor: {flavor[1]}, Season: {flavor[2]}")
    else:
        print("No seasonal flavors found.")

def add_ingredient():
    ingredient_name = input("Enter ingredient name: ")
    quantity = int(input("Enter quantity: "))
    con = sqlite3.connect('Houseofchocloates.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", (ingredient_name, quantity))
    con.commit()
    con.close()
    print(f"Ingredient '{ingredient_name}' with quantity {quantity} added.")

def view_ingredients():
    con = sqlite3.connect('Houseofchocloates.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ingredient_inventory")
    ingredients = cursor.fetchall()
    con.close()
    if ingredients:
        print("\nIngredient Inventory:")
        for ingredient in ingredients:
            print(f"ID: {ingredient[0]}, Ingredient: {ingredient[1]}, Quantity: {ingredient[2]}")
    else:
        print("No ingredients found.")

def add_customer_feedback():
    customer_name = input("Enter customer's name: ")
    flavor_suggestion = input("Enter flavor suggestion: ")
    allergy_concern = input("Enter allergy concern (if any): ")
    con = sqlite3.connect('Houseofchocloates.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO customer_feedback (customer_name, flavor_suggestion, allergy_concern) VALUES (?, ?, ?)",
                   (customer_name, flavor_suggestion, allergy_concern))
    con.commit()
    con.close()
    print(f"Feedback from {customer_name} added.")

def view_customer_feedback():
    con = sqlite3.connect('Houseofchocloates.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM customer_feedback")
    feedbacks = cursor.fetchall()
    con.close()
    if feedbacks:
        print("\nCustomer Feedback:")
        for feedback in feedbacks:
            print(f"ID: {feedback[0]}, Customer: {feedback[1]}, Suggestion: {feedback[2]}, Allergy: {feedback[3]}")
    else:
        print("No customer feedback found.")

# Main menu
def main_menu():
    init_db()
    while True:
        print("\nChocolate House Management")
        print("1. Add Seasonal Flavor")
        print("2. View Seasonal Flavors")
        print("3. Add Ingredient")
        print("4. View Ingredients")
        print("5. Add Customer Feedback")
        print("6. View Customer Feedback")
        print("7. Exit")

        choice = input("Select an option (1-7): ")

        if choice == "1":
             add_seasonal_flavor()
        elif choice == "2":
             view_seasonal_flavors()
        elif choice == "3":
             add_ingredient()
        elif choice == "4":
             view_ingredients()
        elif choice == "5":
             add_customer_feedback()
        elif choice == "6":
             view_customer_feedback()
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the application
if __name__ == "__main__":
    main_menu()
