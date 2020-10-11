# -*- coding: utf-8 -*-
from odoo import http


# class Alnaggarnet(http.Controller):
#     @http.route('/alnaggarnet/alnaggarnet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alnaggarnet/alnaggarnet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alnaggarnet.listing', {
#             'root': '/alnaggarnet/alnaggarnet',
#             'objects': http.request.env['alnaggarnet.alnaggarnet'].search([]),
#         })

#     @http.route('/alnaggarnet/alnaggarnet/objects/<model("alnaggarnet.alnaggarnet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alnaggarnet.object', {
#             'object': obj
#         })
