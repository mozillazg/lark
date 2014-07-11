#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
import json

from django.http import HttpResponse


def json_view(func):
    """装饰 JSON view ::

        @json_view
        def view(request):
            return {'data': [1, 2]}

        @json_view
        def view(request):
            return {'msg': '403'}, 403
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        status = 200
        content_type = 'application/json'
        response = func(request, *args, **kwargs)
        if isinstance(response, HttpResponse):
            return response

        if isinstance(response, (tuple, list)):
            status = response[1]
            context = response[0]
        else:
            context = response

        content = json.dumps(context)
        return HttpResponse(content, status=status,
                            content_type=content_type)
    return wrapper
