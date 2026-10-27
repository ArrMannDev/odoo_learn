from odoo import api,fields,models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_remark = fields.Char(string="Custom Remark")