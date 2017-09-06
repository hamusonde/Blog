# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.contrib import admin
from models import Article

# Register your models here.

class articleAdmin(admin.ModelAdmin):
	list_display = ['author', 'content', 'time', 'date', 'title']
	search_filters = ['article', 'author', 'title']

	class meta:
		model = Article

admin.site.register(Article,articleAdmin)
