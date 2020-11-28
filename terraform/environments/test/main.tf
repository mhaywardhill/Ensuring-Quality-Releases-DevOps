provider "azurerm" {
  features {}
}

terraform {
  backend "azurerm" {
    storage_account_name = ""
    container_name       = ""
    key                  = ""
  }
}

module "resource_group" {
  source               = "../../modules/resource_group"
  resource_group       = "${var.resource_group}"
  location             = "${var.location}"
}
