from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.exceptions import AccessError



class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    name = fields.Char('Work Center', related='resource_id.name', store=True, readonly=False, translate=True)
    code = fields.Char('Code', copy=False, translate=True)


class product_category(models.Model):
    _inherit = "product.category"

    name = fields.Char('Name', index='trigram', required=True, translate=True)
    display_name = fields.Char('Display Name', compute='_compute_display_name', translate=True)

    @api.depends('name', 'parent_id')
    def _compute_display_name(self):
        for category in self:
            if category.parent_id:
                category.display_name = "%s / %s" % (category.parent_id.display_name, category.name)
            else:
                category.display_name = category.name



class Location(models.Model):
    _inherit = "stock.location"

    name = fields.Char('Location Name', required=True, translate=True)
    complete_name = fields.Char("Full Location Name", compute='_compute_complete_name', recursive=True, store=True,
                                translate=True)

    @api.depends('name', 'location_id.complete_name', 'usage')
    def _compute_complete_name(self):
        for location in self:
            if location.location_id and location.usage != 'view':
                location.complete_name = '%s/%s' % (location.location_id.complete_name, location.name)
            else:
                location.complete_name = location.name

