from django.contrib import admin
from .models import User,magazine_Upload,magazine_details,magazine_category#,categoryRegistration
# Register your models here.
admin.site.register(User)
admin.site.register(magazine_details)
admin.site.register(magazine_Upload)
admin.site.register(magazine_category)
#try
