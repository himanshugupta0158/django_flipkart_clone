# FlipkartClone

FlipkartClone is a fully functional e-commerce web application built with Django. This project replicates the core features of the popular e-commerce platform, Flipkart, providing a seamless online shopping experience.

## Features

- **User Authentication**: Register, login, and manage user profiles.
- **Product Management**: Browse, search, and view product details.
- **Shopping Cart**: Add, update, and remove products from the cart.
- **Order Management**: Place orders and view order history.
- **Payment Integration**: Process payments using Stripe.
- **Admin Panel**: Manage products, categories, and orders.

## Technologies Used

- **Backend**: Django, Django Rest Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL
- **Payment Gateway**: Stripe
- **Deployment**: AWS EC2, Heroku

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/flipkartclone.git
    cd flipkartclone
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```sh
    python manage.py runserver
    ```

7. **Access the application**
    - Open your web browser and go to `http://127.0.0.1:8000/`
    - Admin panel: `http://127.0.0.1:8000/admin/`

## Configuration

Create a `.env` file in the project root and add the following configurations:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
DATABASE_URL=postgres://your_db_user:your_db_password@localhost:5432/your_db_name
STRIPE_SECRET_KEY=your_stripe_secret_key
