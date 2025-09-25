# Django Online Shop

A fully functional e-commerce website built with Django.

## About This Project

This project was completed in **2022** as the **final project for my Bachelor's degree** and was **awarded with full grade**. It demonstrates comprehensive Django development skills including e-commerce functionality, user authentication, database design, and modern web development practices.

## Features

- Product catalog with categories and subcategories
- Shopping cart functionality
- User authentication and accounts
- Order management
- Admin panel for managing products and orders

## Categories

- **Audio** (Headphones, Speakers, Gaming Headsets)
- **Cameras** (Digital Cameras, Action Cameras, DSLR)
- **Laptops**
  - Mac (MacBook Pro)
  - Windows (Gaming Laptops, Business Laptops)
- **Smartphones**
  - Android (Flagship, Budget phones)
  - iOS (iPhone Pro)
- **Wearables** (Smart Watches, Fitness Trackers, Smart Rings)

## Quick Start Guide

### Prerequisites
- Python 3.8+ installed on your system
- Git (optional, for cloning)

### Step-by-Step Setup

#### 1. Get the Project
```bash
# Option A: Clone from repository
git clone <repository-url>
cd onlineShop_django

# Option B: If you have the project folder
cd /path/to/onlineShop_django
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Database Setup
```bash
# Apply migrations
python manage.py migrate

# Load pre-populated data (recommended)
cp db_backup_working_*.sqlite3 db.sqlite3
```

#### 5. Run the Server
```bash
python manage.py runserver
```

#### 6. Access the Website
Open your browser and visit: **http://127.0.0.1:8000/**

### Alternative Database Setup
If you prefer to start with an empty database:
```bash
python manage.py migrate
python manage.py createsuperuser  # Create admin account
```

### Troubleshooting
- **Port already in use?** Try: `python manage.py runserver 8001`
- **Virtual environment issues?** Make sure it's activated (you should see `(.venv)` in your terminal)
- **Missing dependencies?** Run `pip install -r requirements.txt` again

## Project Structure

- `shop/` - Main shop application with products and categories
- `accounts/` - User authentication and profiles
- `cart/` - Shopping cart functionality
- `orders/` - Order processing and management
- `media/` - Product images organized by category
- `templates/` - HTML templates

## Database Backup

A working database backup is included: `db_backup_working_*.sqlite3`

This backup contains:
- 5 main categories with subcategories
- 15 products with proper images
- All category relationships configured

## Requirements

See `requirements.txt` for exact package versions that ensure compatibility.

## Notes

- All product images are stored in the `media/` folder
- Categories support hierarchical structure (parent/subcategories)
- Products can belong to multiple categories
- The project uses SQLite for development (easily portable)