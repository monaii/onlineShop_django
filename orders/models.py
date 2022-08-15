from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	discount = models.IntegerField(blank=True, null=True, default=None)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return f'{self.user} - {str(self.id)}'

	def get_total_price(self):
		total = sum(item.get_cost() for item in self.items.all())
		final_price=total
		if self.discount:
			discount_price = (self.discount / 100) * total
			final_price=int( total - discount_price )
			return total ,final_price 
		return total , final_price

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
	price = models.IntegerField()
	quantity = models.PositiveSmallIntegerField(default=1)

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		return self.price * self.quantity

class Coupon(models.Model):
	code = models.CharField(max_length=30, unique=True)
	valid_from = models.DateTimeField()
	valid_to = models.DateTimeField()
	discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.code