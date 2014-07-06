#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

# from .forms import CreateForm
# from .models import Poll


# def index(request, template_name='music/index.html',
#           extra_context=None):
#     context = {
#         'foo': 'bar',
#     }
#     if extra_context:
#         context.update(extra_context)
#     return render_to_response(template_name, context,
#                               context_instance=RequestContext(request))
