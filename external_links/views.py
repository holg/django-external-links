# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from external_links.models import LinkClick

def external_link(request, use_ga_js = True):
    """
    Redirects links and keeps track of them
    """
    try:
        link = request.GET['link']
        link_click = LinkClick(link=link)
        link_click.store(request)
    except KeyError:
        # Someone got here without the link param
        # Redirect to Home as default
        link = '/'
    if use_ga_js:
        return render_to_response('external_links/ga_redirect.html', {'link': link})
    else:
        return HttpResponseRedirect(link)
