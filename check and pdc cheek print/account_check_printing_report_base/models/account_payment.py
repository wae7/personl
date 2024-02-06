# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# (http://www.eficent.com)
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# Copyright 2018 iterativo.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.exceptions import UserError



class AccountRegisterPayments(models.TransientModel):
    _inherit = "account.payment.register"

    def action_create_payments(self):
        res = super().action_create_payments()
        if (
            self.journal_id.check_print_auto
            and self.payment_method_line_id.code == "check_printing"
        ):
            payment = self.env["account.payment"].search(
                [
                    ("journal_id", "=", self.journal_id.id),
                    (
                        "payment_method_line_id.name",
                        "like",
                        self.payment_method_line_id.name,
                    ),
                ],
                order="id desc",
                limit=1,
            )
            return payment.do_print_checks()
        return res


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def do_print_checks(self):
        for rec in self:
            if rec.journal_id.account_check_printing_layout:
                report_action = self.env.ref(
                    rec.journal_id.account_check_printing_layout, False
                )
                self.write({"is_move_sent": True})
                return report_action.report_action(self)
        return super().do_print_checks()

    def action_post(self):
        res = super().action_post()
        recs = self.filtered(
            lambda x: x.journal_id.check_print_auto
            and x.payment_method_line_id.code == "check_printing"
        )
        if recs:
            return recs.do_print_checks()
        return res





class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'

    custom_field = fields.Char('Name in Check')



class Partner_idww(models.Model):
    _inherit = 'account.payment'

    custom_field = fields.Char(related='partner_id.custom_field', string='Name in Check', readonly=True)


    def print_checks(self):
        """ Check that the recordset is valid, set the payments state to sent and call print_checks() """
        # Since this method can be called via a client_action_multi, we need to make sure the received records are what we expect
        if any(not payment.partner_id.custom_field for payment in self):
            raise UserError(_("Please enter a value for the 'Name in check' in the partner before printing checks."))
        self = self.filtered(lambda r: r.payment_method_line_id.code == 'check_printing' and r.state != 'reconciled')

        if len(self) == 0:
            raise UserError(_("Payments to print as a checks must have 'Check' selected as payment method and "
                              "not have already been reconciled"))
        if any(payment.journal_id != self[0].journal_id for payment in self):
            raise UserError(_("In order to print multiple checks at once, they must belong to the same bank journal."))

        if not self[0].journal_id.check_manual_sequencing:
            # The wizard asks for the number printed on the first pre-printed check
            # so payments are attributed the number of the check the'll be printed on.
            self.env.cr.execute("""
                  SELECT payment.id
                    FROM account_payment payment
                    JOIN account_move move ON movE.id = payment.move_id
                   WHERE journal_id = %(journal_id)s
                   AND payment.check_number IS NOT NULL
                ORDER BY payment.check_number::BIGINT DESC
                   LIMIT 1
            """, {
                'journal_id': self.journal_id.id,
            })
            last_printed_check = self.browse(self.env.cr.fetchone())
            number_len = len(last_printed_check.check_number or "")
            next_check_number = '%0{}d'.format(number_len) % (int(last_printed_check.check_number) + 1)

            return {
                'name': _('Print Pre-numbered Checks'),
                'type': 'ir.actions.act_window',
                'res_model': 'print.prenumbered.checks',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'payment_ids': self.ids,
                    'default_next_check_number': next_check_number,
                }
            }
        else:
            self.filtered(lambda r: r.state == 'draft').action_post()
            return self.do_print_checks()


