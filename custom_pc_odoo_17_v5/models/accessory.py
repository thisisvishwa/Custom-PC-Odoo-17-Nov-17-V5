```python
from odoo import models, fields

class Accessory(models.Model):
    _name = 'custom_pc_odoo_17_v5.accessory'
    _description = 'Accessory Model'

    name = fields.Char(string='Accessory Name', required=True)
    brand = fields.Char(string='Brand')
    price = fields.Float(string='Price', required=True)
    specifications = fields.Text(string='Specifications')
    image = fields.Binary(string='Image')
    rating = fields.Float(string='Rating')
    reviews = fields.One2many('custom_pc_odoo_17_v5.review', 'accessory_id', string='Reviews')

    # Define the relation with the inventory module
    inventory_id = fields.Many2one('custom_pc_odoo_17_v5.inventory', string='Inventory')

    # Define the relation with the sales module
    sales_id = fields.Many2one('custom_pc_odoo_17_v5.sales', string='Sales')
```