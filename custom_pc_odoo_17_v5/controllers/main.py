```python
from odoo import http
from odoo.http import request

class CustomPCController(http.Controller):

    @http.route('/shop', type='http', auth='public', website=True)
    def shop(self, **kwargs):
        components = request.env['product.template'].sudo().search([('type', '=', 'component')])
        systems = request.env['product.template'].sudo().search([('type', '=', 'system')])
        accessories = request.env['product.template'].sudo().search([('type', '=', 'accessory')])
        return request.render('custom_pc_odoo_17_v5.shop', {
            'components': components,
            'systems': systems,
            'accessories': accessories,
        })

    @http.route('/product/<model("product.template"):product>', type='http', auth='public', website=True)
    def product(self, product, **kwargs):
        return request.render('custom_pc_odoo_17_v5.product', {
            'product': product,
        })

    @http.route('/build', type='http', auth='public', website=True)
    def build(self, **kwargs):
        return request.render('custom_pc_odoo_17_v5.build')

    @http.route('/add_to_cart', type='json', auth='public', website=True)
    def add_to_cart(self, product_id, quantity):
        order = request.website.sale_get_order(force_create=1)
        product = request.env['product.template'].sudo().browse(int(product_id))
        order._cart_update(product_id=product.id, add_qty=quantity)
        return {'cart_quantity': order.cart_quantity}

    @http.route('/update_cart', type='json', auth='public', website=True)
    def update_cart(self):
        order = request.website.sale_get_order()
        return {'cart_quantity': order.cart_quantity if order else 0}
```