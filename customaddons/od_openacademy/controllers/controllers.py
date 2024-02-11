# -*- coding: utf-8 -*-
# from odoo import http


# class OdOpenacademy(http.Controller):
#     @http.route('/od_openacademy/od_openacademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/od_openacademy/od_openacademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('od_openacademy.listing', {
#             'root': '/od_openacademy/od_openacademy',
#             'objects': http.request.env['od_openacademy.od_openacademy'].search([]),
#         })

#     @http.route('/od_openacademy/od_openacademy/objects/<model("od_openacademy.od_openacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('od_openacademy.object', {
#             'object': obj
#         })
