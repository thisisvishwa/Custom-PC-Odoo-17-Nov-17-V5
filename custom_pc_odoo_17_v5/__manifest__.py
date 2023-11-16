{
    'name': 'Custom PC Builder',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Advanced eCommerce Website Theme for Custom PC Building',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'website_sale', 'stock', 'sale_management', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/product_demo.xml',
        'views/product_template_views.xml',
        'views/website_template.xml',
        'views/component.xml',
        'views/system.xml',
        'views/accessory.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
    This module provides an advanced eCommerce website theme for Odoo 17 CE, specializing in gaming-related products. 
    It covers all aspects from UI/UX design to backend functionality, ensuring a comprehensive solution for custom PC building and sales of gaming products.
    """
}