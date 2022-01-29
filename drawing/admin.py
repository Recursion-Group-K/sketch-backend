from django.contrib import admin
from .models import Drawing


# Register your models here.
@admin.register(Drawing)
class Drawing(admin.ModelAdmin):
  pass