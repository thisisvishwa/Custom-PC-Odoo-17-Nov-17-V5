# Technical Documentation

## Module Name: custom_pc_odoo_17_v5

### Introduction

This document provides a technical overview of the `custom_pc_odoo_17_v5` module, an advanced eCommerce website theme for Odoo 17 CE, specializing in gaming-related products.

### Module Structure

The module follows the MVC (Model-View-Controller) architecture and is structured as follows:

- `models`: Contains the database models for the components, complete systems, and accessories.
- `controllers`: Contains the main controller for handling requests and responses.
- `views`: Contains the XML files for defining the structure of the website.
- `static/src`: Contains the JavaScript and CSS files for the website.
- `tests`: Contains the unit tests for the models and controllers.
- `data`: Contains the demo data for the module.
- `security`: Contains the CSV file defining the access rights for the module.

### Database Models

The module defines three models in the `models` directory:

- `component.py`: Represents the components like CPUs, GPUs, RAM, etc.
- `system.py`: Represents the complete systems like pre-built gaming PCs and gaming laptops.
- `accessory.py`: Represents the accessories like gaming consoles, monitors, keyboards, etc.

### Controllers

The `main.py` file in the `controllers` directory is the main controller for the module. It handles requests and responses, integrates with external services, and manages the data flow between the models and views.

### Views

The `views` directory contains two XML files:

- `product_template_views.xml`: Defines the structure of the product catalogue.
- `website_template.xml`: Defines the structure of the custom PC builder interface.

### Static Files

The `static/src` directory contains the JavaScript and CSS files for the website:

- `custom_pc_builder.js`: Contains the JavaScript code for the custom PC builder interface.
- `custom_pc_builder.css`: Contains the CSS code for the custom PC builder interface.

### Tests

The `tests` directory contains the unit tests for the models and controllers:

- `test_models.py`: Contains the unit tests for the models.
- `test_controllers.py`: Contains the unit tests for the controllers.

### Data

The `product_demo.xml` file in the `data` directory contains demo data for the module.

### Security

The `ir.model.access.csv` file in the `security` directory defines the access rights for the module.

### API Integrations

The `main.py` controller integrates with the Odoo Inventory Management and Sales and CRM modules for managing inventory and sales processes.

### Compliance

The module follows Odoo 17 CE standards for coding, UI design, and module integration.