# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
	author = models.CharField(("Author"), max_length = 60, null = True, blank =True)
	title = models.CharField(("Title"), max_length = 80, null = True, blank = True)
	date = models.DateField(("published"),auto_now = True)
	time = models.TimeField()
	content = models.TextField(("Article"), blank = True, null = True)


	class Meta:
		verbose_name = 'ARTICLE'
		verbose_name_plural = 'ARTICLES'

	def __unicode__(self):
		return self.title