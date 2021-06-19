from django.contrib import admin
from .models import One2one,Many2one,Many2Many
# Register your models here.
@admin.register(One2one)
class Onedata(admin.ModelAdmin):
    list_display=['page_title','page_cat','publish_date','user']

@admin.register(Many2one)
class Many21(admin.ModelAdmin):
    list_display=['song_name','song_duration','user']

@admin.register(Many2Many)
class Manymany(admin.ModelAdmin):
    list_display=['song_name','song_duration','written_by']