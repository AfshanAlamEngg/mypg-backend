# My PG - A Paying Guest Management System - Django Backend

Welcome to the My PG Project! This project is designed to help manage paying guest accommodations efficiently. It allows landlords to manage their PG properties and tenants to find and book accommodations easily.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Registration and Authentication**
- **Landlord Dashboard for Property Management**
- **Tenant Dashboard for Booking Management**
- **Search and Filter PG Properties**
- **Online Booking and Payment Integration**
- **Room Availability Tracking**
- **Reviews and Ratings System**
- **Notifications and Email Alerts**

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python (version 3.13+)**
- **Django (version 5.0+)**
- **PostgreSQL (or any preferred database)**

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/AfshanAlamEngg/mypg-backend
    cd mypg-backend
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    # On Windows
    venv\Scripts\activate
    
    # On macOS/Linux
    source venv/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure the database settings in `my_pg/settings.py`.

6. Apply migrations:
    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

After setting up the project, you can access the application by navigating to `http://127.0.0.1:8000/` in your web browser. Use the superuser credentials to log in to the admin panel and start managing your PG properties.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch** (`git checkout -b feature/your-feature`).
3. **Commit your changes** (`git commit -m 'Add your feature'`).
4. **Push to the branch** (`git push origin feature/your-feature`).
5. **Create a new Pull Request.**

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

For any inquiries or support, please contact afshanalamengg@gmail.com

