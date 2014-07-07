#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
import json

from django.http import HttpResponse


def json_view(**response_kwargs):
    """装饰 JSON view ::

        @json_view()
        def view(request):
            return {'data': [1, 2]}

        @json_view(content_type='application/vnd.github+json')
        def view(request):
            return {'data': [1, 2]}

        @json_view()
        def view(request):
            return {'msg': '403'}, 403
    """
    response_kwargs.setdefault('content_type', 'application/json')
    response_kwargs.setdefault('status', 200)

    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            if isinstance(response, HttpResponse):
                return response

            if isinstance(response, (tuple, list)):
                response_kwargs['status'] = response[1]
                context = response[0]
            else:
                context = response

            content = json.dumps(context)
            return HttpResponse(content, **response_kwargs)
        return wrapper
    return decorator
