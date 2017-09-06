# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from models import Article

class HomeView(ListView):
	model = Article
	template_name = "index.html"