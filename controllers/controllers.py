# -*- coding: utf-8 -*-
# from odoo import http


# class DemoFirenor(http.Controller):
#     @http.route('/demo_firenor/demo_firenor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_firenor/demo_firenor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_firenor.listing', {
#             'root': '/demo_firenor/demo_firenor',
#             'objects': http.request.env['demo_firenor.demo_firenor'].search([]),
#         })

#     @http.route('/demo_firenor/demo_firenor/objects/<model("demo_firenor.demo_firenor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_firenor.object', {
#             'object': obj
#         })

