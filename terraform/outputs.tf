output "resource_group_name" {
  value = azurerm_resource_group.this.name
}

output "storage_account_name" {
  value = azurerm_storage_account.this.name
}

output "datalake_filesystem_name" {
  value = azurerm_storage_data_lake_gen2_filesystem.this.name
}

output "bronze_path" {
  value = "abfss://${azurerm_storage_data_lake_gen2_filesystem.this.name}@${azurerm_storage_account.this.name}.dfs.core.windows.net/bronze"
}

output "silver_path" {
  value = "abfss://${azurerm_storage_data_lake_gen2_filesystem.this.name}@${azurerm_storage_account.this.name}.dfs.core.windows.net/silver"
}

output "gold_path" {
  value = "abfss://${azurerm_storage_data_lake_gen2_filesystem.this.name}@${azurerm_storage_account.this.name}.dfs.core.windows.net/gold"
}

output "databricks_workspace_name" {
  value = azurerm_databricks_workspace.this.name
}

output "databricks_workspace_url" {
  value = azurerm_databricks_workspace.this.workspace_url
}

output "tenant_id" {
  value = data.azurerm_client_config.current.tenant_id
}

output "databricks_sp_client_id" {
  value = azuread_application.databricks_sp_app.client_id
}

output "databricks_sp_object_id" {
  value = azuread_service_principal.databricks_sp.object_id
}

output "databricks_sp_client_secret" {
  value     = azuread_service_principal_password.databricks_sp_password.value
  sensitive = true
}