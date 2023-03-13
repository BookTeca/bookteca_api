from django.contrib import admin
from .models import Copy, Loan

admin.site.register([Copy, Loan])
