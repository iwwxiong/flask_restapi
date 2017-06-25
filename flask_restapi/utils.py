#! /usr/bin/env python
# -*- coding: utf-8 -*-


def register_api(bp, view, endpoint, pk='id', pk_type='int'):
    """
    register api url
    """
    view_func = view.as_view(endpoint)
    bp.add_url_rule('', view_func=view_func, methods=['GET', ])
    bp.add_url_rule('', view_func=view_func, methods=['POST', ])
    bp.add_url_rule('/<%s:%s>' % (pk_type, pk), view_func=view_func, methods=['GET', ])
    bp.add_url_rule('/<%s:%s>' % (pk_type, pk), view_func=view_func, methods=['PUT', 'DELETE', ])

    return bp


def set_dict(_dict, _key, _value):
    """
    >>> _dict = {}
    >>> _key = 'a.b.c' or ['a', 'b', 'c']
    >>> _value = 1
    {
        'a': {
            'b': {
                    'c': 1
                }
            }
        }
    }
    """
    if not isinstance(_key, list):
        _key = _key.split('.')
    length = len(_key)
    if length <= 0:
        return _dict
    if length == 1:
        _dict[_key[0]] = _value
        return _dict
    i = 0
    temp_dict = _dict
    while i <= length - 1:
        if _key[i] not in temp_dict:
            if length - i > 1:
                temp_dict[_key[i]] = {}
            else:
                temp_dict[_key[i]] = _value
        temp_dict = temp_dict[_key[i]]
        i += 1

    return _dict
