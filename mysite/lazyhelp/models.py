from django.db import models

# Create your models here.
class User(models.Model):
	uid = models.AutoField(primary_key = True)
	uname = models.CharField(max_length = 20)
	account = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	point = models.DecimalField(max_digits = 10, decimal_places = 0)
	mail = models.EmailField(max_length = 254)


        def __unicode__(self):
            return self.uname

class Order(models.Model):
	oid = models.AutoField(primary_key = True)
	title = models.CharField(max_length = 20)
	location = models.CharField(max_length = 40)
	buyer = models.ForeignKey(User, related_name="custom_user_profile_b")
	saler = models.ForeignKey(User, related_name="custom_user_profile_s")
	price = models.DecimalField(max_digits = 10, decimal_places = 0)
	pic1 = models.ImageField(height_field = 500,width_field =500)
	pic2 = models.ImageField(height_field = 500,width_field =500)
	pic3 = models.ImageField(height_field = 500,width_field =500)
	pic4 = models.ImageField(height_field = 500,width_field =500)
	deadline = models.DateField()
	point_to_b = models.IntegerField()
	point_to_s = models.IntegerField()
	status = models.SmallIntegerField()

        def __unicode__(self):
            return self.title