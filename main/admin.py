from . import models
from django.contrib import admin


admin.site.register(models.Client)
admin.site.register(models.Contact)
admin.site.register(models.Service)
admin.site.register(models.Featured)
admin.site.register(models.Subscribe)
admin.site.register(models.Portfolio)
admin.site.register(models.PortfolioCategory)