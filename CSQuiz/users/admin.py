from django.contrib import admin
from .models import User,EmailConfirmCodeHelperModel
# Register your models here.
admin.site.register(User)
admin.site.register(EmailConfirmCodeHelperModel)