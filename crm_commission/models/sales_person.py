from odoo import models, fields


class SalesPerson(models.Model):
    _inherit = 'res.users'
    _description = "This model allows applying the commission in the sales"

    types = fields.Many2one('crm.commission', string='Type')
