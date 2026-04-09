terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.35.0"
    }

    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 3.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
  required_version = ">= 1.12.2"
}

provider "azurerm" {
  features {}
  subscription_id = var.subscription_id
}

provider "azuread" {}

locals {
  project = "job"
}

resource "azurerm_resource_group" "this" {
  name     = "rg-${var.project_name}-${var.environment}"
  location = var.location
}

resource "azurerm_storage_account" "this" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.this.name
  location                 = azurerm_resource_group.this.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  is_hns_enabled = true // this enables ADLS Gen2

  tags = {
    project     = var.project_name
    environment = var.environment
  }
}

resource "azurerm_storage_data_lake_gen2_filesystem" "this" {
  name               = var.datalake_filesystem_name
  storage_account_id = azurerm_storage_account.this.id
}

resource "azurerm_storage_data_lake_gen2_path" "bronze" {
  path               = "bronze"
  filesystem_name    = azurerm_storage_data_lake_gen2_filesystem.this.name
  storage_account_id = azurerm_storage_account.this.id
  resource           = "directory"
}

resource "azurerm_storage_data_lake_gen2_path" "silver" {
  path               = "silver"
  filesystem_name    = azurerm_storage_data_lake_gen2_filesystem.this.name
  storage_account_id = azurerm_storage_account.this.id
  resource           = "directory"
}

resource "azurerm_storage_data_lake_gen2_path" "gold" {
  path               = "gold"
  filesystem_name    = azurerm_storage_data_lake_gen2_filesystem.this.name
  storage_account_id = azurerm_storage_account.this.id
  resource           = "directory"
}

resource "azurerm_role_assignment" "storage_blob_data_contributor" {
  scope                = azurerm_storage_account.this.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = var.current_user_object_id
}

data "azurerm_client_config" "current" {}

resource "azuread_application" "databricks_sp_app" {
  display_name = var.databricks_sp_display_name
}

resource "azuread_service_principal" "databricks_sp" {
  client_id = azuread_application.databricks_sp_app.client_id
}

resource "azuread_service_principal_password" "databricks_sp_password" {
  service_principal_id = azuread_service_principal.databricks_sp.id
  end_date             = timeadd(timestamp(), var.databricks_sp_secret_duration)
}

resource "azurerm_role_assignment" "databricks_sp_storage_blob_data_contributor" {
  scope                = azurerm_storage_account.this.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azuread_service_principal.databricks_sp.object_id
}

resource "azurerm_databricks_workspace" "this" {
  name                = "dbw-${var.project_name}-${var.environment}"
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  sku                 = var.databricks_sku

  tags = {
    project     = var.project_name
    environment = var.environment
  }
}