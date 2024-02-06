# Copyright (C) Softhealer Technologies.
{
    "name": "Post Dated Cheque Management - Enterprise Edition",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Accounting",
    "license": "OPL-1",
    "summary": "Post Dated Cheque Management, Manage Post Dated Cheque App, View Vendor Invoice PDC , List Of Customer PDC Payment, Track Client PDC Process, Register Vendor Post Dated Cheque Module, Print VendorPDC Report, Print Client PDC Report Odoo.",
    "description": """In Invoice/Bill, a post-dated cheque is a cheque written by the customer/vendor (payer) for a date in the future. Whether a post-dated cheque may be cashed or deposited before the date written on it depends on the country. Currently, odoo does not provide any kind of feature to manage post-dated cheque. That why we make this module, it will help to manage a post-dated cheque with an accounting journal entries. This module provides a feature to Register PDC Cheque in an account. This module allows to manage postdated cheque for the customer as well vendors, you can easily track/move to a different state of cheque like new, registered, return, deposit, bounce, done. We have taken care of all states with accounting journal entries, You can easily list filter cheque with different states. We have also made simple pdf reports. Post Dated Cheque Management Odoo
 Manage Vendor Post Dated Cheque Module, Manage Client Post Dated Cheque View Client PDC In Invoice, Get Vendor PDC In Bill, See List Of PDC Bill Of Vendor, Track PDC Process Of Customer, Register Post Dated Cheque, Print Vendor PDC Report Odoo.
 Manage Post Dated Cheque App, View Vendor Invoice PDC , List Of Customer PDC Payment, Track Client PDC Process, Register Vendor Post Dated Cheque Module, Print VendorPDC Report, Print Client PDC Report Odoo.""",
    "version": "16.0.1",
    "depends": [
        "account_accountant","sh_pdc"
    ],
    "data": [
       
       'views/pdc_menu.xml'

    ],

    "application": True,
    "auto_install": False,
    "installable": True,
    "images": ['static/description/background.png', ],
    "price": 1,
    "currency": "EUR",
}
