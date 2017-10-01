# -*- coding: utf-8 -*-
from openerp import http

# class Crm-ccm(http.Controller):
#     @http.route('/crm-ccm/crm-ccm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm-ccm/crm-ccm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm-ccm.listing', {
#             'root': '/crm-ccm/crm-ccm',
#             'objects': http.request.env['crm-ccm.crm-ccm'].search([]),
#         })

#     @http.route('/crm-ccm/crm-ccm/objects/<model("crm-ccm.crm-ccm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm-ccm.object', {
#             'object': obj
#         })