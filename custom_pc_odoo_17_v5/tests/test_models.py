```python
from odoo.tests import common

class TestModels(common.TransactionCase):

    def setUp(self):
        super(TestModels, self).setUp()
        self.Component = self.env['custom_pc_odoo_17_v5.component']
        self.System = self.env['custom_pc_odoo_17_v5.system']
        self.Accessory = self.env['custom_pc_odoo_17_v5.accessory']

    def test_create_component(self):
        """Test the creation of a Component."""
        component = self.Component.create({
            'name': 'Test Component',
            'price': 100.0,
            'specifications': 'Test Specifications',
        })
        self.assertEqual(component.name, 'Test Component')

    def test_create_system(self):
        """Test the creation of a System."""
        system = self.System.create({
            'name': 'Test System',
            'price': 1000.0,
            'specifications': 'Test Specifications',
        })
        self.assertEqual(system.name, 'Test System')

    def test_create_accessory(self):
        """Test the creation of an Accessory."""
        accessory = self.Accessory.create({
            'name': 'Test Accessory',
            'price': 50.0,
            'specifications': 'Test Specifications',
        })
        self.assertEqual(accessory.name, 'Test Accessory')
```