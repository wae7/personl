from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import AccessError
from odoo.exceptions import ValidationError


class MrpBomInherit(models.Model):
    _inherit = "mrp.bom"

    private_id = fields.Many2one('custom.pom.line', string='Private')
    custom_ids = fields.One2many('custom.pom.line', 'bom_id', string='Custom Records')
    name = fields.Char(string='Name')
    percentage_field = fields.Float(string='Percentage', widget='percentage')
    amount_field = fields.Float(string='Amount')

    @api.model
    def default_get(self, fields):
        defaults = super(MrpBomInherit, self).default_get(fields)

        # Create and save the default records
        default_values = []
        names = ['Operation Cost', 'Management Cost', 'Hidden Profit', 'Risk Cost', 'Profit Margin']

        for name in names:
            record_values = {'name': name}
            default_record = self.env['custom.pom.line'].create(record_values)
            default_values.append((4, default_record.id, 0))

        defaults['custom_ids'] = default_values

        return defaults




class CustomPom(models.Model):
    _name = "custom.pom.line"

    bom_id = fields.Many2one('mrp.bom', string='Bill Of Materil')
    bom_ids = fields.One2many('mrp.bom', 'private_id', string='Bill Of Materil')
    cost_hose = fields.Float(related='bom_id.product_tmpl_id.standard_price')
    name = fields.Char(string='Name')
    percentage_field = fields.Float(string='Percentage', widget='percentage')
    amount_field = fields.Float(
        string='Amount',
        compute='_compute_amount',
        digits=(16, 5),
        store=True
    )

    @api.depends('cost_hose', 'percentage_field')
    def _compute_amount(self):
        for record in self:
            record.amount_field = round(record.cost_hose * record.percentage_field, 5)





class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'


    def button_sale_order_eco(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("mrp_plm.mrp_eco_action_main")
        context = {
            'default_sale_order_id': self.id,
            'default_partner_id': self.partner_id.id,
        }
        previous_orders = self._get_previous_orders()
        action['domain'] = [('bom_id', 'in', list(previous_orders.keys()))]

        action['context'] = context

        return action

    def _get_previous_orders(self):
        """ Return a dictionary with the keys to be all the previous orders' id and
        the value to be a set of ids in self of which the key is their previous orders.
        """
        previous_orders = dict((order.id, {order.id}) for order in self)
        for order in self:
            previous_orders_data = self.with_context(active_test=False).search_read(
                [('partner_id', '=', order.partner_id.id)],
                fields=['id'],
                order='id desc'
            )

            for previous_order_data in previous_orders_data:
                previous_order_id = previous_order_data['id']
                previous_orders[previous_order_id] = previous_orders.get(order.id, set()) | previous_orders.get(
                    previous_order_id, set())

        return previous_orders


class InheritedMrpEco(models.Model):
    _inherit = 'mrp.eco'

    sale_order_id = fields.Many2one('sale.order', string="Sales Order", readonly=True,)
    production_id = fields.Many2one('mrp.production', string='Manufacturing Order', readonly=True)

    def button_mrp1_eco(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("mrp.mrp_production_action")
        context = {
            'default_eco_id': self.id,
            'default_product_tmpl_id': self.product_tmpl_id.id,
        }
        previous_orders = self._get_previous_orders()
        action['domain'] = [('bom_id', 'in', self.bom_id.ids)]
        action['context'] = context

        if self.production_id:
            self.production_id.write({'bom_id': self.bom_id.id})

        return action

    def _get_previous_orders(self):
        previous_orders = {}
        for order in self:
            previous_orders_data = self.with_context(active_test=False).search_read(
                [('product_tmpl_id', '=', order.product_tmpl_id.id)],
                fields=['id'],
                order='id desc'
            )

            for previous_order_data in previous_orders_data:
                previous_order_id = previous_order_data['id']
                previous_orders[previous_order_id] = previous_orders.get(order.id, set()) | previous_orders.get(
                    previous_order_id, set())

        return previous_orders

    def approve(self):
        self._create_or_update_approval(status='approved')

        activity_to_check = self.env['mail.activity'].search([
            ('res_id', '=', self.id),
            ('res_model', '=', 'mrp.eco'),
            ('activity_type_id.name', '=', 'R&D-Document-Check'),
        ], limit=1)

        if activity_to_check:
            activity_to_check.action_done()

        eco_approval_activity = self.env['mail.activity'].search([
            ('res_id', '=', self.id),
            ('res_model', '=', 'mrp.eco'),
            ('activity_type_id.name', '=', 'ECO Approval'),
        ], limit=1)

        if eco_approval_activity:
            eco_approval_activity.action_done()

        ed_document_check_activity = self.env['mail.activity'].search([
            ('res_id', '=', self.id),
            ('res_model', '=', 'mrp.eco'),
            ('activity_type_id.name', '=', 'ED-Document-Check'),
        ], limit=1)

        if ed_document_check_activity:
            ed_document_check_activity.action_done()


    type_id = fields.Many2one(
        'mrp.eco.type', 'Type', required=True,
        widget="radio", default=lambda self: self.env['mrp.eco.type'].search([], limit=1))

    effectivity = fields.Selection(
        default='date',  # Set the default value to 'date'
    )

    type = fields.Selection(
        default='product',  # Set the default value to 'product'
    )
    sale_order_line_id = fields.Many2one('sale.order.line', readonly=True)

    @api.onchange('effectivity')
    def _onchange_effectivity(self):
        if self.effectivity == 'date':
            self.effectivity_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d %H:%M:%S')

    @api.onchange('effectivity_date')
    def _onchange_effectivity_date(self):
        if self.effectivity_date and self.effectivity == 'date':
            min_date = datetime.now() + timedelta(days=14)
            if self.effectivity_date < min_date:
                self.effectivity_date = min_date.strftime('%Y-%m-%d %H:%M:%S')



class MrpProductionInherited(models.Model):
    _inherit = 'mrp.production'

    eco_id = fields.Many2one('mrp.eco', 'ECO', readonly=True)
    roo_id = fields.Many2one(related='eco_id.bom_id', string='wee')

    @api.onchange('roo_id')
    def _onchange_roo_id(self):
        if self.roo_id:
            self.bom_id = self.roo_id



class ProductAttributeInherited(models.Model):
    _inherit = 'product.attribute.value'

    cod = fields.Char(string='cood', unique=True)

    # _sql_constraints = [
    #     ('cod_unique', 'UNIQUE(cod)', 'The cod must be unique!'),
    # ]
    #
    # @api.constrains('cod')
    # def _check_unique_cod(self):
    #     for record in self:
    #         if record.cod:
    #             if self.search_count([('cod', '=', record.cod)]) > 1:
    #                 raise ValidationError("The cod must be unique!")


class ProductTTemplateInherited(models.Model):
    _inherit = 'product.template.attribute.value'

    cooding = fields.Char(related='product_attribute_value_id.cod', string='Cooding')


class ProductProductInherited(models.Model):
    _inherit = 'product.product'

    cood = fields.Char(string='Code', compute='_compute_cood_values')

    @api.depends('product_template_variant_value_ids.cooding')
    def _compute_cood_values(self):
        for product in self:
            cood_values = [str(value.cooding) for value in product.product_template_variant_value_ids if value.cooding]
            product.cood = ''.join(cood_values)
            product.default_code = product.cood











