variable "resource_group_name" {
  type = string
}

variable "service_plan_name" {
  type = string
}

variable "webapp_name" {
  type = string
}

resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = "West Europe"
}

resource "azurerm_app_service_plan" "example" {
  name                = var.service_plan_name
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  kind = "Linux"
  reserved = true

  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "example" {
  name                = var.webapp_name
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    ##linux_fx_version = "DOTNETCORE|3.1"
    #dotnet_framework_version = "v4.0"
    linux_fx_version = "PYTHON|3.6"
    #python_version = 3.4
    #app_command_line = "dotnet MySampleWebApp.dll"
  }
}
