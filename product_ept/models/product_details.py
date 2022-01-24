from odoo import models, fields


class ProductDetails(models.Model):
    _name = "product.demo.ept"
    _description = "Product Demo"

    name = fields.Char(string="Product", help="Name of the product")
    sku = fields.Char(string="SKU", help="Stock Keeping Unit of the Product", compute="_compute_sku", readonly=True)
    barcode = fields.Char(string="Barcode", help="Barcode of the product")
    on_sale = fields.Boolean(string="Can Sold", help="Can this product be sold")
    product_type = fields.Selection(string="Product Type", help="Type of the product", selection=[('Storable', 'Storable'), ('Consumable', 'Consumable'), ('Service', 'Service')])
    sale_price = fields.Float(string="Sale Price", help="Sale price of the product", digits=(6, 2))
    cost_price = fields.Float(string="Cost Price", help="Cost price of the product", digits=(6, 2))
    active = fields.Boolean(string="Active", help="Whether this product is available or not")
    warehouse = fields.Char(string="Warehouse", help="Name of the warehouse where product is stored")
    product_image = fields.Image(string="Product Image", help="Image of the Product")
    website_description = fields.Html(string="Website Description", help="Description of the product")
    internal_note = fields.Text(string="Internal Note", help="Note about the product")

    def _compute_sku(self):
        for record in self:
            record.sku = "PRD" + str(record.id)