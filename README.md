# Django Online Shop

A fully functional e-commerce website built with Django.

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

## Setup Instructions

### 1. Clone and Navigate
```bash
cd /path/to/onlineShop_django
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
```

### 5. Load Sample Data (Optional)
The project includes pre-populated categories and products. If you need to restore the working database:
```bash
cp db_backup_working_*.sqlite3 db.sqlite3
```

### 6. Run Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

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