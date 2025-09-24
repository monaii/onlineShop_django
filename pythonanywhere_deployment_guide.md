# Deploying onlineShop_django to PythonAnywhere

This guide will walk you through deploying your Django online shop to PythonAnywhere's free tier.

## Step 1: Create a PythonAnywhere Account

1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com/) and sign up for a free account
2. Verify your email address

## Step 2: Upload Your Project

### Option 1: Using Git (Recommended)

1. Log in to PythonAnywhere
2. Open a Bash console from the Dashboard
3. Clone your repository:
   ```bash
   git clone https://github.com/monaii/onlineShop_django.git
   ```

### Option 2: Manual Upload

If you prefer to upload manually:
1. Create a zip file of your project
2. Upload it via the PythonAnywhere Files tab
3. Unzip it in your PythonAnywhere home directory

## Step 3: Set Up a Virtual Environment

1. In the PythonAnywhere Bash console:
   ```bash
   cd ~/onlineShop_django
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Step 4: Configure Your Web App

1. Go to the Web tab in PythonAnywhere
2. Click "Add a new web app"
3. Choose "Manual configuration" (not the Django option)
4. Select Python 3.8 (or the version compatible with your project)

## Step 5: Configure WSGI File

1. In the Web tab, click on the WSGI configuration file link
2. Replace the contents with the code from your `wsgi_pythonanywhere.py` file
3. Update the path to match your PythonAnywhere username:
   ```python
   path = '/home/YOUR_USERNAME/onlineShop_django'
   ```

## Step 6: Update Settings

1. Create a file called `local_settings.py` in the same directory as your settings.py:
   ```python
   # Add to A/local_settings.py
   DEBUG = False
   ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']
   
   # Database settings (using SQLite)
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': '/home/YOUR_USERNAME/onlineShop_django/sqlite3',
       }
   }
   
   # Static files
   STATIC_ROOT = '/home/YOUR_USERNAME/onlineShop_django/static'
   MEDIA_ROOT = '/home/YOUR_USERNAME/onlineShop_django/media'
   ```

2. Update your main settings.py to import local settings:
   ```python
   # Add at the end of A/settings.py
   try:
       from .local_settings import *
   except ImportError:
       pass
   ```

## Step 7: Configure Static Files

1. In the Web tab, add these static file mappings:
   - URL: `/static/` Directory: `/home/YOUR_USERNAME/onlineShop_django/static`
   - URL: `/media/` Directory: `/home/YOUR_USERNAME/onlineShop_django/media`

2. Run collectstatic:
   ```bash
   python manage.py collectstatic
   ```

## Step 8: Set Up the Database

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

## Step 9: Reload Your Web App

1. Go to the Web tab
2. Click the "Reload" button for your web app

## Step 10: Visit Your Site

Your site should now be live at:
```
https://YOUR_USERNAME.pythonanywhere.com
```

## Troubleshooting

If you encounter issues:

1. Check the error logs in the Web tab
2. Ensure all required packages are installed
3. Verify your WSGI file path is correct
4. Make sure your ALLOWED_HOSTS includes your PythonAnywhere domain

## Updating Your Site

When you make changes to your code:

1. Pull the latest changes from GitHub
2. Apply any migrations
3. Collect static files if needed
4. Reload your web app

## Free Tier Limitations

- Your site will be available at YOUR_USERNAME.pythonanywhere.com
- CPU usage is limited
- Database size is limited to 512MB
- Always-on (no sleep like Heroku)