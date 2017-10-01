# Install development environment

```sh
apt-get update
apt-get install git
apt-get install vim
```
## Install git inside docker container

```sh
# login to docker as root user
docker exec -it --user root odoo bash
```
## Clone the repository

```sh
git clone https://github.com/ibanhvn/odoo-addons.git
```
# Create a new Odoo module

[Reference: Building a Module](https://www.odoo.com/documentation/9.0/howtos/backend.html)
```sh
# create a new module, crm-ccm as module name
# odoo-addons: module location
odoo.py scaffold crm-ccm odoo-addons
```
## Define module icon

```sh
mkdir -p static/description
# copy icon.png (200x200) to static/description
# static/description/icon.png is applied as the module icon
```
# Creat a new model
- Define a simple model having name and description as the properties
```python
# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CallType(models.Model):
    _name = 'ib.calltype'
    name = fields.Char()
    description = fields.Text()
```
- Define menu items and actions allowing user to create/update/delete `CallType`
```xml
<?xml version="1.0" encoding="utf-8"?>
<openerp>
<data>
    <!-- Settings/Techinical/CRM - CMM -->
    <menuitem id="ib_crm_ccm_menu" name="CRM - CCM" parent="base.menu_custom" sequence="1" />
</data>
</openerp>
```
