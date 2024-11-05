# Chocolate House Management Application

A Django application to manage a fictional chocolate house's:
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

## Getting Started

### Prerequisites
- Python 3.9+
- Docker (for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chocolate_house
   
2. Run the Program
      <br>   
     python manage.py migrate
     python manage.py runserver

3.Build Docker File
    docker build -t chocolate_house .

4. Run the Docker Container
    docker run -p 8000:8000 chocolate_house
