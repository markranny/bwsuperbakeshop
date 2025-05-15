# ELJIN SUPERBAKESHOP

A complete web application for managing a bakery business with customer-facing site and admin dashboard, built with Django.

## Features

### Customer-Facing Website
- **Home Page**: Banner slideshow, featured products, and promotional sections
- **About Page**: Company story, team members, awards, and history timeline
- **Menu Page**: Product catalog with categories, filtering, and special offers
- **Franchise Page**: Franchise models, investment breakdown, testimonials, and application form
- **Career Page**: Job listings, application system, employee benefits, and testimonials
- **Location Page**: Store locator with map integration, location details, and search functionality
- **Contact Page**: Contact form with messaging system

### Admin Dashboard
- **Content Management**: Edit content for all pages with a user-friendly interface
- **Menu Management**: Manage product categories, items, prices, and special offers
- **Career Management**: Post job positions, manage applications, and update career content
- **Franchise Management**: Manage franchise models, investment details, and applications
- **Location Management**: Add/edit store locations, hours, and contact information
- **Message Center**: View and respond to customer messages, job applications, and franchise inquiries
- **Site Settings**: Manage global settings, contact info, social media links, and branding

## Technical Overview

### Built With
- Django 4.2
- MySQL Database
- CKEditor for rich text editing
- Bootstrap 5 for the dashboard UI
- Custom CSS/JS for the frontend website

### Project Structure
- `bakeshop`: Main app for the customer-facing website
- `dashboard`: Admin interface for content management
- `eljin_bakeshop`: Project settings and configuration

## Setup Instructions

### Prerequisites
- Python 3.8+
- MySQL Server
- pip and virtualenv

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd eljin_bakeshop
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure the database in `eljin_bakeshop/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eljin_bakeshop',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Create the database
```bash
mysql -u root -p
CREATE DATABASE eljin_bakeshop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'eljin_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON eljin_bakeshop.* TO 'eljin_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

6. Run migrations
```bash
python manage.py migrate
```

7. Create a superuser
```bash
python manage.py createsuperuser
```

8. Collect static files
```bash
python manage.py collectstatic
```

9. Run the development server
```bash
python manage.py runserver
```

10. Access the site at `http://127.0.0.1:8000` and the dashboard at `http://127.0.0.1:8000/dashboard/`

## Deployment

### Production Settings
For production deployment, make sure to:
1. Set `DEBUG = False` in settings.py
2. Configure a proper `SECRET_KEY`
3. Update `ALLOWED_HOSTS` with your domain
4. Set up proper database credentials
5. Configure a production-ready web server (Nginx/Apache)
6. Set up HTTPS with SSL certificate

## Project Structure

```
eljin_bakeshop/                  # Main project directory
│
├── eljin_bakeshop/              # Project configuration directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── bakeshop/                    # Main app directory 
│   ├── __init__.py
│   ├── admin.py                 # Admin configurations
│   ├── apps.py
│   ├── forms.py                 # Forms for various content management
│   ├── models.py                # Database models
│   ├── urls.py                  # URL patterns for the app
│   ├── views.py                 # View logic
│   ├── context_processors.py    # For global context variables
│   ├── templatetags/            # Custom template tags
│   │   ├── __init__.py
│   │   └── bakeshop_tags.py
│   │
│   ├── migrations/              # Database migrations
│   ├── static/                  # Static files - CSS, JS, images
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── templates/               # HTML templates
│       ├── bakeshop/
│       │   ├── base.html        # Base template with common elements
│       │   ├── index.html       # Homepage
│       │   ├── about.html       # About us page
│       │   ├── career.html      # Career opportunities
│       │   ├── franchise.html   # Franchise information
│       │   ├── location.html    # Store locations
│       │   ├── menu.html        # Menu items
│       │   └── includes/        # Reusable template components
│       │
│       └── admin/               # Custom admin templates
│           └── bakeshop/        # Admin dashboard customizations
│
├── dashboard/                   # Custom dashboard app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py                  # Dashboard URLs
│   ├── views.py                 # Dashboard views
│   └── templates/
│       └── dashboard/
│           ├── base.html        # Dashboard base template
│           ├── index.html       # Dashboard home
│           ├── about.html       # About page management
│           ├── career.html      # Career page management
│           ├── franchise.html   # Franchise page management
│           ├── location.html    # Locations management
│           └── menu.html        # Menu management
│
├── media/                       # User-uploaded content
│
├── manage.py                    # Django management script
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## License
This project is proprietary software. All rights reserved.

## Contact
For support or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).