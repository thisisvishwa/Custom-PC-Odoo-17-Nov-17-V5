```python
from odoo import models, fields

class System(models.Model):
    _name = 'custom_pc_odoo_17_v5.system'
    _description = 'Complete Systems'

    name = fields.Char(string='System Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    image = fields.Binary(string='Image')
    cpu_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='CPU', domain=[('component_type', '=', 'CPU')])
    gpu_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='GPU', domain=[('component_type', '=', 'GPU')])
    ram_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='RAM', domain=[('component_type', '=', 'RAM')])
    motherboard_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='Motherboard', domain=[('component_type', '=', 'Motherboard')])
    storage_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='Storage', domain=[('component_type', '=', 'Storage')])
    power_supply_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='Power Supply', domain=[('component_type', '=', 'Power Supply')])
    cooling_system_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='Cooling System', domain=[('component_type', '=', 'Cooling System')])
    case_id = fields.Many2one('custom_pc_odoo_17_v5.component', string='Case', domain=[('component_type', '=', 'Case')])
    rating = fields.Float(string='Rating')
    review_count = fields.Integer(string='Review Count')
    is_available = fields.Boolean(string='Available', default=True)
```