provider "azurerm" {
  version = "=2.0.0"
  features {}
}

#backend
terraform {
  backend "azurerm" {
    resource_group_name  = "rgname"
    storage_account_name = "storageaccoutnisarg1"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
