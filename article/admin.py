# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


class article(models.Model):
	author = models.Charfield(_("Author"), max_length = 60, null = True, blank =True)
	title = models.Charfield(_("Title"), max_length = 80, null = True, blank = True)
	time_stump = models.Datefield(_("published"),auto_now = True)
	content = models.Textfieds(_("Article"), blank = True, null = True)


	class Meta:
		verbose_name = 'ARTICLE'
		verbose_name_plural = 'ARTICLES'
		