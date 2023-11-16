```python
from odoo.tests import HttpCase

class TestMainController(HttpCase):

    def setUp(self):
        super(TestMainController, self).setUp()
        self.Component = self.env['custom_pc_odoo_17_v5.component']
        self.System = self.env['custom_pc_odoo_17_v5.system']
        self.Accessory = self.env['custom_pc_odoo_17_v5.accessory']

    def test_01_homepage(self):
        response = self.url_open('/shop')
        self.assertEqual(response.status_code, 200)

    def test_02_product_catalogue(self):
        response = self.url_open('/shop/category/components')
        self.assertEqual(response.status_code, 200)

    def test_03_custom_pc_builder(self):
        response = self.url_open('/shop/custom_pc_builder')
        self.assertEqual(response.status_code, 200)

    def test_04_product_detail(self):
        component = self.Component.create({'name': 'Test CPU', 'price': 100.0})
        response = self.url_open('/shop/product/%s' % component.id)
        self.assertEqual(response.status_code, 200)

    def test_05_add_to_cart(self):
        component = self.Component.create({'name': 'Test GPU', 'price': 200.0})
        self.authenticate('admin', 'admin')
        self.url_open('/shop/cart/update/%s' % component.id)
        cart = self.env['sale.order'].search([('state', '=', 'draft')])
        self.assertEqual(len(cart.order_line), 1)
        self.assertEqual(cart.order_line.product_id.id, component.id)

    def test_06_checkout(self):
        self.authenticate('admin', 'admin')
        self.url_open('/shop/checkout')
        order = self.env['sale.order'].search([('state', '=', 'sent')])
        self.assertEqual(len(order), 1)
```
