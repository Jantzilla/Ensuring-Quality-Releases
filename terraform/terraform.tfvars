# Azure subscription vars
subscription_id = "${var.subscription_id}"
client_id = "${var.client_id}"
client_secret = "${var.client_secret}"
tenant_id = "${var.tenant_id}"

# Resource Group/Location
location = "eastus"
resource_group = "my_resource_group"
application_type = "webApp"

# Network
virtual_network_name = ""
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"
