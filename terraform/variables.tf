variable "subscription_id" {
  description = "Azure subscription ID"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "Brazil South"
}

variable "project_name" {
  description = "Project base name"
  type        = string
  default     = "jobmarket"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "storage_account_name" {
  description = "Globally unique storage account name"
  type        = string
}

variable "datalake_filesystem_name" {
  description = "ADLS Gen2 filesystem name"
  type        = string
  default     = "job-data"
}

variable "current_user_object_id" {
  description = "Object ID of the current Azure user for RBAC"
  type        = string
}

variable "databricks_sku" {
  description = "Databricks SKU"
  type        = string
  default     = "standard"
}

variable "databricks_sp_display_name" {
  description = "Display name for the Service Principal used by Databricks to access ADLS"
  type        = string
  default     = "sp-jobmarket-databricks-dev"
}

variable "databricks_sp_secret_duration" {
  description = "Secret lifetime for the Databricks Service Principal password"
  type        = string
  default     = "8760h"
}