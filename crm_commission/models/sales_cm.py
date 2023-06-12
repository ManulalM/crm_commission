from odoo import api, fields, models


class SalesPerson(models.Model):
    _inherit = 'sale.order'
    _description = "This model allows to apply the commission in the sales"

    plan_type_id = fields.Many2one('crm.commission', string="Plan type")
    commission_rate = fields.Float(string="Commission rate", store=True)
    commission_amount = fields.Monetary(
        string="Commission Amount",
        compute='_compute_amount',
        store=True, precompute=True)
    revenue_type = fields.Char(string="Type")
    from_amount = fields.Char(string="FA", help="contact")
    to_amount = fields.Char(string="TA", help="contact")
    comms_type = fields.Char(string="Commission type", help="contact")

    @api.onchange('user_id')
    def _onchangeuser(self):
        if self.user_id:
            plan_type = self.user_id.types.name
            self.plan_type_id = self.env['crm.commission'].search([('name', '=', plan_type)]).id

            commission_record = self.env['revenue.wise'].search([('connects_id.name', '=', plan_type)], limit=1)
            if commission_record:
                self.commission_rate = commission_record.rate
            else:
                self.commission_rate = 0.0

            types = self.env['crm.commission'].search([('name', '=', plan_type)]).types
            self.revenue_type = types

            fa = self.env['revenue.wise'].search([('connects_id.name', '=', plan_type)])
            if fa:
                self.from_amount = fa.from_amount
            else:
                self.from_amount = 0

            ta = self.env['revenue.wise'].search([('connects_id.name', '=', plan_type)])
            if ta:
                self.to_amount = ta.to_amount
            else:
                self.to_amount = 0

            ca = self.env['crm.commission'].search([('name', '=', plan_type)]).type
            self.comms_type = ca

    def _compute_amount(self):
        for order in self:
            if order.comms_type == 'rw':
                if order.revenue_type == 'straight':
                    totals = sum(order.order_line.mapped('price_total'))
                    total_amount = totals * order.commission_rate
                    order.commission_amount = total_amount
                else:
                    for i in self:
                        tam = float(i.to_amount)
                        totals = sum(order.order_line.mapped('price_total'))
                        if totals < tam:
                            order.commission_amount = totals * 0.05
                        elif totals > tam:
                            p_total = totals - tam
                            order.commission_amount = p_total * 0.06
                        else:
                            order.commission_amount = 0

            else:
                for k in self.plan_type_id.order_line_ids:
                    for m in self.order_line:
                        if k.product_id.id == m.product_template_id.id:
                            rates = k.rate
                            subst = rates * m.price_subtotal
                            self.commission_amount = self.commission_amount + subst
