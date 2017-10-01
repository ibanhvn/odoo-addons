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
- Define menu items, views and actions allowing user to create/update/delete `CallType`
- `views\menus.xml` 
```xml
<?xml version="1.0" encoding="utf-8"?>
<openerp>
<data>
    <!-- Settings/Techinical/CRM - CMM -->
    <menuitem id="ib_crm_ccm_menu" name="CRM - CCM" parent="base.menu_custom" sequence="1" />
</data>
</openerp>
```
- `views\calltype.xml`
```xml
<?xml version="1.0" encoding="utf-8" ?>
<openerp>
<data>
    <record id="ib_calltype_tree" model="ir.ui.view">
        <field name="name">ib.calltype.tree</field>
        <field name="model">ib.calltype</field>
        <field name="arch" type="xml">
            <tree string="Call Type" editable="top">
                <field name="name" />
                <field name="description" />
            </tree>
        </field>
    </record>
    <record id="ib_calltype_form" model="ir.ui.view">
        <field name="name">ib.calltype.form</field>
        <field name="model">ib.calltype</field>
        <field name="arch" type="xml">
           <form string="Call Type">
               <sheet>
                  <group name="main">
                      <field name="name" />
                      <field name="description" />
                  </group>
               </sheet>
           </form>
        </field>
    </record>

    <!-- actions -->
    <record id="ib_calltype_action" model="ir.actions.act_window" >
       <field name="name">Call Type</field>
       <field name="res_model">ib.calltype</field>
       <field name="view_mode">tree,form</field>
    </record>
    <!-- menu items -->
    <menuitem id="ib_calltype_list_menu" parent="ib_crm_ccm_menu" action="ib_calltype_action" sequence="10" />
</data>
</openerp>
```
- Add ``views/menus.xml` and `views/calltype.xml` to the module manifest
- `__openerp__.py`
```python
# always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menus.xml',
        'views/calltype.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
```
