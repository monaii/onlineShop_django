import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A.settings')
django.setup()

from shop.models import Product

# Update all image paths from .svg to .jpeg
for product in Product.objects.all():
    if '.svg' in str(product.image):
        product.image = str(product.image).replace('.svg', '.jpeg')
        product.save()
        print(f"Updated {product.name}: {product.image}")

print("All image extensions updated to .jpeg")