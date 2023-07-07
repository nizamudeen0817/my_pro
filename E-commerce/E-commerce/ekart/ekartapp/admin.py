from django.contrib import admin
from . models import Ekartcard
from . models import Productcard
from . models import Booking
# Register your models here.
admin.site.register(Ekartcard)
admin.site.register(Productcard)
admin.site.register(Booking)