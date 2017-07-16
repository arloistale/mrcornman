# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic

from django.shortcuts import render

class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'

