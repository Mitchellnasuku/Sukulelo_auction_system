from django.contrib import admin
from auction.models import *

admin.site.register(Person)
admin.site.register(Item)
admin.site.register(Bid)