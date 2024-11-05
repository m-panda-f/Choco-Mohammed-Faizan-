# 🍫 Chocolate House Management Application
<h2> Built by Mohammed Faizan </h2>>
This is a Django-powered application designed to help manage the operations of a fictional chocolate house, handling tasks such as:

-   **Seasonal Flavor Offerings:** Add, view, and manage seasonal flavors.
-   **Ingredient Inventory:** Track ingredients and manage stock levels.
-   **Customer Feedback:** Collect customer flavor suggestions and allergy concerns.
Explore the code and projects by visiting my GitHub and portfolio.

# 📋 Features
Add, View, and Delete Seasonal Flavors: Keep track of special offerings for each season.
Manage Ingredient Inventory: Record and monitor the quantity of ingredients on hand.
Collect Customer Feedback: Allow customers to suggest flavors and share allergy concerns.

# 🚀 Getting Started

   Prerequisites
      - Python 3.9+
      - Docker (optional, for containerized deployment)

<h3> Installation and Setup</h3>
**1. Clone the Repository**
First, clone this repository to your local machine and navigate into the project directory:

            git clone <repository-url>
            cd chocohouse
**2. Install and Run the Application**
Set up the Django environment and start the application by running the following commands:

      
         # Run migrations to set up the database
         python manage.py migrate

         # Start the Django development server
         python manage.py runserver
         The application should now be running at http://127.0.0.1:8000/.


# 🐳 Docker Setup
For a containerized setup, follow these steps to build and run the application using Docker.

**3. Build the Docker Image**
In the project root directory, build the Docker image:

         docker build -t chocohouse .
**4. Run the Docker Container**
Now, run the Docker container, mapping port 8000:

      
      docker run -p 8000:8000 chocohouse
Access the application in your browser at http://localhost:8000/.

# 🛠 Usage
The application is designed to be intuitive and user-friendly. Here’s a quick overview of each feature:

**Manage Seasonal Flavors:**

Navigate to the Seasonal Flavors page to add, view, and delete flavors based on the season.
Manage Ingredient Inventory:

On the Ingredient Inventory page, you can add ingredients along with their quantities, and delete ingredients when stock runs out.
Customer Feedback:

The Feedback page allows customers to suggest new flavors and report any allergy concerns, which you can review.


# 🧪 Testing the Application
To validate the functionality of this application, follow these test steps:

-   Add a Seasonal Flavor: Go to the flavors page, add a new flavor, and ensure it appears in the list.
-   Delete a Seasonal Flavor: Delete any flavor entry and confirm it’s removed.
-   Add an Ingredient: On the ingredients page, add an ingredient with a specified quantity.
-   Delete an Ingredient: Remove an ingredient and verify it no longer appears in the list.
-   Submit Feedback: Use the feedback form to submit a suggestion or allergy concern and check that it’s displayed on the page.


# 🧩 Edge Cases and Validations
-   Empty Fields: The application handles cases where required fields are left empty and prompts the user to enter valid data.
-   Invalid Quantities: For inventory management, the app checks that quantities are positive integers.
-   Duplicate Entries: The app ensures that identical entries do not cause unexpected behavior in the system.
  
# 💼 About the Developer
I'm Mohammed Faizan, a passionate software developer with expertise in Python, Django, and web development. Explore more of my projects and connect with me through the links below:

   - Portfolio: m-panda-f.github.io/Portfolio
   - GitHub: github.com/m-panda-f
   - linkedin: https://www.linkedin.com/in/mohammed-faizan-b3305b299/
