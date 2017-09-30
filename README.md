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
```
git clone https://github.com/ibanhvn/odoo-addons.git
```
# Create a new Odoo module
[Reference: Building a Module](https://www.odoo.com/documentation/9.0/howtos/backend.html)
```sh
# create a new module, crm-ccm as module name
odoo.py scaffold crm-ccm odoo-addons
```


