from odoo import api, fields, models

class ShopItem(models.Model):
    _name = 'shop.item' #shop.item will create a table in the database with the name shop_item
    _description = 'Shop Item'
    
    name = fields.Char('Name')
    number = fields.Integer(string='Item References')
    quantity = fields.Float('Stock Quantity')
    is_available = fields.Boolean('Is Available',compute='_compute_available')
    date = fields.Date('Date')
    received_datetime = fields.Datetime('Received DateTime')
    state = fields.Selection(selection=[('draft','Draft'),('available','Available'),('sold','Sold')],
                             string='State',
                             default='draft')
    currency_id = fields.Many2one('res.currency',string='Currency')
    tag_ids = fields.Many2many('shop.item.tag',string='Tags')
    item_line_ids = fields.One2many('shop.item.line',inverse_name='item_id',string='Lines')

    #compute function
    @api.depends('quantity')
    def _compute_available(self):
        for rec in self:

            if rec.quantity > 0:
                rec.is_available = True
            else:
                rec.is_available = False

    def action_confirm(self):
        self.state = 'available'
    def action_sold(self):
        self.state = 'sold'


class ShopItemTag(models.Model):
    _name = 'shop.item.tag'
    _description = 'Shop Item Tag'

    name = fields.Char('Tag Name',required=True)
    color =fields.Integer('Color')

class ShopItemLine(models.Model):
    _name = 'shop.item.line'
    _description = 'Shop Item Line'

    item_id = fields.Many2one('shop.item',string='Shop Item')
    product_id = fields.Many2one('product.product',string='Product')
    quantity = fields.Float('Quantity')
    unit_cost = fields.Float('Unit Cost')
    total_amount = fields.Float('Total Amount')

    @api.onchange('quantity','unit_cost')
    def _calculate_total_amount(self):
        # pdb is used for debugging
        # import pdb
        # pdb.set_trace()
        self.total_amount = self.quantity * self.unit_cost
