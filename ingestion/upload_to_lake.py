import os

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient
from dotenv import load_dotenv

from utils.utils import get_env

load_dotenv()


def ensure_directory(filesystem_client, directory_name: str):
    directory_client = filesystem_client.get_directory_client(directory_name)
    try:
        directory_client.create_directory()
        print(f"Diretório criado: {directory_name}")
    except Exception:
        print(f"Diretório já existe ou não precisou ser criado: {directory_name}")
    return directory_client


def upload_files():
    storage_account_name = get_env("AZURE_STORAGE_ACCOUNT_NAME")
    filesystem_name = get_env("AZURE_DATALAKE_FILESYSTEM")
    target_directory = get_env("TARGET_DIRECTORY")
    local_folder = '../' + get_env("SAMPLE_FOLDER")

    files = os.listdir(local_folder)
    if not files:
        raise FileNotFoundError(f"Arquivos locais não encontrados em {local_folder}")

    account_url = f"https://{storage_account_name}.dfs.core.windows.net"

    credential = DefaultAzureCredential()
    service_client = DataLakeServiceClient(account_url=account_url, credential=credential)
    filesystem_client = service_client.get_file_system_client(filesystem_name)
    ensure_directory(filesystem_client, target_directory)

    for file in os.listdir(local_folder):
        local_path = local_folder + file

        file_client = filesystem_client.get_file_client('bronze/' + file)
        with open(local_path, "rb") as f:
            data = f.read()

        file_client.upload_data(data, overwrite=True)

        print("Upload concluído com sucesso.")
        print(f"Arquivo local: {local_path}")
        print(
            f"Destino: abfss://{filesystem_name}@{storage_account_name}.dfs.core.windows.net/{target_directory}/{local_folder}")


if __name__ == "__main__":
    upload_files()
