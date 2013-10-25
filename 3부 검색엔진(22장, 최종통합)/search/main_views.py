# -*- coding: cp949 -*-
from django.http import HttpResponse

#for template
from django.template import Context, loader

def main_page(req):
    tpl = loader.get_template('main.html')
    ctx = Context({
    })
    html = tpl.render(ctx)
    return HttpResponse(html)
