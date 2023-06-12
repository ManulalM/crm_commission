from odoo import fields, models


class SalesTeam(models.Model):
    _inherit = 'crm.team'
    _description = "This model allows to add the sales team"

    plan_id = fields.Many2one('crm.commission', string="Sales Team Type")
