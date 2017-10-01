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
- Define a simple model
```python
class Config(models.Model):
    _name = 'ib.config'
    category = fields.Char(string='Category', required=True, translate=True)
    key = fields.Char(string='Key', required=True, translate=True)
    value = fields.Char(string='Value', required=True, translate=True)
    description = fields.Text(string='Description', required=False, translate=True)
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
- `views\config.xml`
```xml
<?xml version="1.0" encoding="utf-8" ?>
<openerp>
<data>
    <record id="ib_config_tree" model="ir.ui.view">
      <field name="name">ib.config.tree</field>
      <field name="model">ib.config</field>
      <field name="arch" type="xml">
          <tree string="Configuration" editable="top">
              <field name="category" />
              <field name="key" />
              <field name="value" />
              <field name="description" /> 
          </tree> 
        </field>
    </record>
    <record id="ib_config_form" model="ir.ui.view">
        <field name="name">ib.config.form</field>
        <field name="model">ib.config</field>
        <field name="arch" type="xml">
           <form string="Configuration">
               <sheet>
                  <group name="main">
                      <field name="category" />
                      <field name="key" />
                      <field name="value" />
                      <field name="description" /> 
                  </group> 
               </sheet>
           </form> 
        </field> 
    </record>
    
    <!-- actions -->
    <record id="ib_config_action" model="ir.actions.act_window" >
       <field name="name">Configuration</field>
       <field name="res_model">ib.config</field>
       <field name="view_mode">tree,form</field> 
    </record>
    <!-- menu items -->
    <menuitem id="ib_config_list_menu" parent="ib_crm_ccm_menu" action="ib_config_action" sequence="10" />   
</data>
</openerp>
```
- Add `views/menus.xml` and `views/config.xml` to the module manifest
- `__openerp__.py`
```python
# always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/config.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
```
# Multiple languages
- After app installation you can export transaltion file `crm-ccm.pot` for supporting different languages
- Go to `Settings/Transaltions/Import - Export/Export Translation`
- Select `CRM - CCM` in `Apps to Export`
```sh
# change `crm-ccm.pot` to `vi.po` or `de.po` upon languages you want to support
i18n\
     de.po
     vi.po
     ...
```
# Custom Module for all users
- By default a custom module is only visible for admin user
- To make the custom module accessible from different users you have to define a `security/ir.model.access.csv`
- Then declare `security/ir.model.access.csv` in the module manifest
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_crm_ccm_callrecord_manager,access_ib_callrecord,model_ib_callrecord,,1,1,1,1
access_crm_ccm_config_manager,access_ib_config,model_ib_config,,1,1,1,1
```
