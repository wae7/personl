from odoo import api, fields, models


class StockValuationLayerInherit(models.Model):
    _inherit = 'stock.valuation.layer'

    land = fields.Char(string='Landed Cost', compute='compute_stock_landed_cost_id')

    @api.depends('stock_landed_cost_id', 'stock_landed_cost_id.valuation_adjustment_lines')
    def compute_stock_landed_cost_id(self):
        for rec in self:
            rec.land = False
            if rec.stock_landed_cost_id:
                valuation_adjustment_lines = rec.stock_landed_cost_id.valuation_adjustment_lines.filtered(lambda line: line.additional_landed_cost == rec.value)
                if valuation_adjustment_lines:
                    rec.land = ', '.join(valuation_adjustment_lines.mapped('cost_line_id.name'))


class ProductTempletInherit(models.Model):
    _inherit = 'product.template'


    attributes1 = fields.Char(string='Attributes', compute='compute_attribute_line_ids')

    @api.depends('attribute_line_ids')
    def compute_attribute_line_ids(self):
        for rec in self:
            rec.attributes1 = False
            if rec.attribute_line_ids:
                attribute_names = [line.attribute_id.name for line in rec.attribute_line_ids]
                rec.attributes1 = ', '.join(attribute_names)

    valuo1 = fields.Char(string='Value', compute='compute_value_line_ids')

    @api.depends('attribute_line_ids')
    def compute_value_line_ids(self):
        for rec in self:
            rec.valuo1 = False
            if rec.attribute_line_ids:
                attribute_names = [line.value_ids.name for line in rec.attribute_line_ids]
                rec.valuo1 = ', '.join(attribute_names)



class ProductProductInherit(models.Model):
    _inherit = 'product.product'


    attributes2 = fields.Char(string='Attributes', compute='compute_attribute_line_ids')

    @api.depends('attribute_line_ids')
    def compute_attribute_line_ids(self):
        for rec in self:
            rec.attributes2 = False
            if rec.attribute_line_ids:
                attribute_names = [line.attribute_id.name for line in rec.attribute_line_ids]
                rec.attributes2 = ', '.join(attribute_names)

    valuo2 = fields.Char(string='Value', compute='compute_value_line_ids')

    @api.depends('attribute_line_ids')
    def compute_value_line_ids(self):
        for rec in self:
            rec.valuo2 = False
            if rec.attribute_line_ids:
                attribute_names = [line.value_ids.name for line in rec.attribute_line_ids]
                rec.valuo2 = ', '.join(attribute_names)




class StockQuantInherit(models.Model):
    _inherit = 'stock.quant'


    attributes3 = fields.Char(string='Attributes', related='product_tmpl_id.attributes1')

    valuo3 = fields.Char(string='Value', related='product_tmpl_id.valuo1')

























