# -*- coding: utf-8 -*-
# from odoo import http


# class OmOdooInheritence(http.Controller):
#     @http.route('/om_odoo_print_saleorder/om_odoo_print_saleorder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_odoo_print_saleorder/om_odoo_print_saleorder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_odoo_print_saleorder.listing', {
#             'root': '/om_odoo_print_saleorder/om_odoo_print_saleorder',
#             'objects': http.request.env['om_odoo_print_saleorder.om_odoo_print_saleorder'].search([]),
#         })

#     @http.route('/om_odoo_print_saleorder/om_odoo_print_saleorder/objects/<model("om_odoo_print_saleorder.om_odoo_print_saleorder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_odoo_print_saleorder.object', {
#             'object': obj
#         })
