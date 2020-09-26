from django.contrib import admin

# Register your models here.

from .models import Donor
from .models import Ngo
from .models import Requirement
# from .models import Like


admin.site.register(Donor)
admin.site.register(Ngo)
admin.site.register(Requirement)
# admin.site.register(Like)