# Copyright (C) Softhealer Technologies.

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    pdc_customer = fields.Many2one(
        'account.account', string="PDC Account for customer")

    pdc_vendor = fields.Many2one(
        'account.account', string="PDC Account for Vendor")

    pdc_bounce = fields.Many2one('account.account', string="PDC Account for Bounce")

    auto_fill_open_invoice = fields.Boolean(string = "Auto Fill open Invoice in PDC on Customer Selection ")

    pdc_operation_type = fields.Selection([('cancel', 'Cancel Only'), ('cancel_draft', 'Cancel and Reset to Draft'), ('cancel_delete', 'Cancel and Delete')],
                                              default='cancel', string="Opration Type")

    #=============
    # Customer
    #=============
    
    is_cust_due_notify = fields.Boolean('Customer Due Notification')
    
    is_notify_to_customer = fields.Boolean('Notify to Customer')
    
    is_notify_to_user = fields.Boolean('Notify to Internal User ')
    
    sh_user_ids = fields.Many2many('res.users',relation='sh_user_ids_customer_company_rel',string='Responsible User')
    
    notify_on_1 = fields.Char(string='Notify On 1')
    
    notify_on_2 = fields.Char(string='Notify On 2')
    
    notify_on_3 = fields.Char(string='Notify On 3')
    
    notify_on_4 = fields.Char(string='Notify On 4')
    
    notify_on_5 = fields.Char(string='Notify On 5')
    
    #=============
    # Vendor
    #=============

    is_vendor_due_notify = fields.Boolean('Vendor Due Notification')
    
    is_notify_to_vendor = fields.Boolean('Notify to Vendor')
    
    is_notify_to_user_vendor = fields.Boolean('Notify to internal User')
     
    sh_user_ids_vendor = fields.Many2many('res.users',relation='sh_user_ids_vendor_company_rel',string='Responsible User ')
    
    notify_on_1_vendor = fields.Char(string='Notify on 1')
    
    notify_on_2_vendor = fields.Char(string='Notify on 2')
    
    notify_on_3_vendor = fields.Char(string='Notify on 3')
    
    notify_on_4_vendor = fields.Char(string='Notify on 4')
    
    notify_on_5_vendor = fields.Char(string='Notify on 5')

    # =============
    # Bounce
    # =============

    is_bounce_due_notify = fields.Boolean('Bounce Due Notification')

    is_notify_to_bounce = fields.Boolean('Notify to Bounce')

    is_notify_to_user_bounce = fields.Boolean('Notify to internal User')

    sh_user_ids_bounce = fields.Many2many('res.users', relation='sh_user_ids_bounce_company_rel',
                                          string='Responsible User ')

    notify_on_1_bounce = fields.Char(string='Notify on 1')

    notify_on_2_bounce = fields.Char(string='Notify on 2')

    notify_on_3_bounce = fields.Char(string='Notify on 3')

    notify_on_4_bounce = fields.Char(string='Notify on 4')

    notify_on_5_bounce = fields.Char(string='Notify on 5')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pdc_customer = fields.Many2one('account.account', string="PDC Account for customer",
                                   related='company_id.pdc_customer', readonly=False)

    pdc_vendor = fields.Many2one('account.account', string="PDC Account for Vendor",
                                 related='company_id.pdc_vendor', readonly=False)
    pdc_bounce = fields.Many2one('account.account', string="PDC Account for bounce",
                                 related='company_id.pdc_bounce', readonly=False)

    auto_fill_open_invoice = fields.Boolean(string = "Auto Fill open Invoice in PDC on Customer Selection",
                                            related = "company_id.auto_fill_open_invoice",readonly=False)
    
    pdc_operation_type = fields.Selection(related="company_id.pdc_operation_type", readonly=False)
    
    #=============
    # Customer
    #=============
    
    is_cust_due_notify = fields.Boolean('Customer Due Notification',
                                        related='company_id.is_cust_due_notify',readonly=False)
    
    is_notify_to_customer = fields.Boolean('Notify to Customer',
                                        related='company_id.is_notify_to_customer',readonly=False)
    
    is_notify_to_user = fields.Boolean('Notify to Internal User',
                                        related='company_id.is_notify_to_user',readonly=False)
    
    sh_user_ids = fields.Many2many('res.users',string='Responsible User',
                                        related='company_id.sh_user_ids',readonly=False)
    
    notify_on_1 = fields.Char('Notify On 1',
                              related='company_id.notify_on_1',readonly=False)
    
    notify_on_2 = fields.Char('Notify On 2',
                              related='company_id.notify_on_2',readonly=False)
    
    notify_on_3 = fields.Char('Notify On 3',
                              related='company_id.notify_on_3',readonly=False)
    
    notify_on_4 = fields.Char('Notify On 4',
                              related='company_id.notify_on_4',readonly=False)
    
    notify_on_5 = fields.Char('Notify On 5',
                              related='company_id.notify_on_5',readonly=False)
    
    #=============
    # Vendor
    #=============
    is_vendor_due_notify = fields.Boolean('Vendor Due Notification',
                                        related='company_id.is_vendor_due_notify',readonly=False)
    
    is_notify_to_vendor = fields.Boolean('Notify to Vendor',
                                        related='company_id.is_notify_to_vendor',readonly=False)
    
    is_notify_to_user_vendor = fields.Boolean('Notify to Internal User ',
                                              related='company_id.is_notify_to_user_vendor',readonly=False)
    
    sh_user_ids_vendor = fields.Many2many('res.users',string='Responsible User ',
                                        related='company_id.sh_user_ids_vendor',readonly=False)
    
    notify_on_1_vendor = fields.Char('Notify on 1',
                              related='company_id.notify_on_1_vendor',readonly=False)
    
    notify_on_2_vendor = fields.Char('Notify on 2',
                              related='company_id.notify_on_2_vendor',readonly=False)
    
    notify_on_3_vendor = fields.Char('Notify on 3',
                              related='company_id.notify_on_3_vendor',readonly=False)
    
    notify_on_4_vendor = fields.Char('Notify on 4',
                              related='company_id.notify_on_4_vendor',readonly=False)
    
    notify_on_5_vendor = fields.Char('Notify on 5',
                              related='company_id.notify_on_5_vendor',readonly=False)



    # =============
    # Bounce
    # =============
    is_bounce_due_notify = fields.Boolean('Bounce Due Notification',
                                          related='company_id.is_bounce_due_notify', readonly=False)

    is_notify_to_bounce = fields.Boolean('Notify to Bounce',
                                         related='company_id.is_notify_to_bounce', readonly=False)

    is_notify_to_user_bounce = fields.Boolean('Notify to Internal User ',
                                              related='company_id.is_notify_to_user_bounce', readonly=False)

    sh_user_ids_bounce = fields.Many2many('res.users', string='Responsible User ',
                                          related='company_id.sh_user_ids_bounce', readonly=False)

    notify_on_1_bounce = fields.Char('Notify on 1',
                                     related='company_id.notify_on_1_bounce', readonly=False)

    notify_on_2_bounce = fields.Char('Notify on 2',
                                     related='company_id.notify_on_2_bounce', readonly=False)

    notify_on_3_bounce = fields.Char('Notify on 3',
                                     related='company_id.notify_on_3_bounce', readonly=False)

    notify_on_4_bounce = fields.Char('Notify on 4',
                                     related='company_id.notify_on_4_bounce', readonly=False)

    notify_on_5_bounce = fields.Char('Notify on 5',
                                     related='company_id.notify_on_5_bounce', readonly=False)
