from odoo import fields, models


class ProductWise(models.Model):
    _name = "product.wise"
    _description = "This model contains the product wise detail"

    product_category_id = fields.Many2one('product.category', string='Category')
    product_id = fields.Many2one('product.template', string='Product',
                                 domain="[('categ_id', '=', product_category_id)]")
    rate = fields.Float(string="Rate (%)", help="contact")
    max_commission = fields.Integer(string="Max commission", help="contact")
    connect_id = fields.Many2one('crm.commission', string="connect")
