from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    request_vendor_id = fields.Many2one(
        'res.partner',
        string='Request Vendor',
        domain=[('supplier_rank', '>', 0)],
        help='Vendor yang akan digunakan untuk purchase order'
    )
    
    no_kontrak = fields.Char(
        string='No Kontrak',
        help='Nomor kontrak terkait dengan sales order ini'
    )
    
    with_po = fields.Boolean(
        string='With PO',
        default=False,
        help='Centang jika sales order ini memerlukan purchase order'
    )
    
    purchase_order_ids = fields.One2many(
        'purchase.order',
        'sale_order_id',
        string='Purchase Orders',
        help='Purchase orders yang terkait dengan sales order ini'
    )
    
    purchase_order_count = fields.Integer(
        string='PO Count',
        compute='_compute_purchase_order_count',
        store=True
    )
    
    @api.depends('purchase_order_ids')
    def _compute_purchase_order_count(self):
        for order in self:
            order.purchase_order_count = len(order.purchase_order_ids)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    sale_order_id = fields.Many2one(
        'sale.order',
        string='Sales Order',
        help='Sales order yang terkait dengan purchase order ini'
    )