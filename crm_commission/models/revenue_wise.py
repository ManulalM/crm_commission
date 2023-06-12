from odoo import fields, models


class RevenueWise(models.Model):
    _name = "revenue.wise"
    _inherit = ["mail.thread"]
    _description = "welcome to Revenue wise  management system"

    sequence = fields.Char(string="Sequence")
    from_amount = fields.Monetary(string="From Amount", currency_field='company_currency_id', help="contact")
    to_amount = fields.Monetary(string="To Amount", currency_field='company_currency_id', help="contact")
    company_id = fields.Many2one('res.company', string='Company', required=True, index=True,
                                 default=lambda self: self.env.company,
                                 help="Company related to this journal", )
    company_currency_id = fields.Many2one(string='company currency', related='company_id.currency_id', help="contact")
    rate = fields.Float(string="Rate")
    connects_id = fields.Many2one('crm.commission', string='connect')