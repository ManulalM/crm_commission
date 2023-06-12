from odoo import fields, models


class CrmCommission(models.Model):
    _name = "crm.commission"
    _inherit = ["mail.thread"]
    _description = "welcome to commission management system"

    name_id = fields.Many2one('res.partner', string="Name", help="contact")
    name = fields.Char(string="Name", help="contact")
    active = fields.Boolean('Is Active')
    from_date = fields.Datetime(string=" From Date", help="contact")
    to_date = fields.Datetime(string="To Date", help="contact")
    type = fields.Selection([('pw', 'Product Wise'), ('rw', 'Revenue Wise')])
    order_line_ids = fields.One2many('product.wise', 'connect_id', string="Order lines")
    strong = fields.Char(string="strong")
    types = fields.Selection([('straight', 'Straight'), ('graduated', 'Graduated')], string="Revenue Types")
    connect_line_ids = fields.One2many('revenue.wise', 'connects_id')
