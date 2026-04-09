job_titles = [
    "Data Engineer", "Data Analyst", "Data Scientist",
    "Machine Learning Engineer", "Analytics Engineer",
    "BI Analyst", "Data Architect", "ML Engineer",
    "Backend Engineer", "Software Engineer"
]

companies = [
    "TechCorp", "DataInc", "Cloudify", "InsightLabs",
    "BigData Co", "AI Solutions", "NextGen Analytics",
    "BlueMetrics", "Lakehouse Labs", "CoreStack"
]

locations = [
    "São Paulo", "Rio de Janeiro", "Belo Horizonte",
    "Curitiba", "Porto Alegre", "Recife", "Remote"
]

skills_pool = [
    "Python", "Java", "Scala", "R", "JavaScript", "TypeScript",
    "Go", "C#", "C++", "Rust", "Kotlin",
    "SQL", "NoSQL", "Data Modeling", "ETL", "ELT",
    "Data Warehousing", "Data Lake", "Data Lakehouse",
    "Data Governance", "Data Quality", "Data Lineage",
    "Apache Spark", "PySpark", "Spark SQL", "Hadoop", "Hive",
    "Presto", "Trino", "Flink",
    "Azure", "AWS", "GCP",
    "Azure Data Factory", "Azure Databricks", "Azure Synapse",
    "Azure Data Lake", "ADLS Gen2", "Azure Functions",
    "S3", "Redshift", "Glue", "Lambda", "EMR", "Athena", "Kinesis",
    "BigQuery", "Dataflow", "Dataproc", "Pub/Sub", "Cloud Storage",
    "PostgreSQL", "MySQL", "SQL Server", "Oracle", "MariaDB",
    "MongoDB", "Cassandra", "DynamoDB", "Redis", "Cosmos DB",
    "Snowflake", "Databricks", "Delta Lake", "Apache Iceberg",
    "Apache Hudi",
    "Apache Airflow", "Prefect", "Dagster", "dbt",
    "Apache Kafka", "RabbitMQ", "Pulsar",
    "Power BI", "Tableau", "Looker", "Metabase", "Superset", "Excel",
    "Scikit-learn", "TensorFlow", "PyTorch", "MLflow", "NLP",
    "Docker", "Kubernetes", "Terraform", "Ansible", "CI/CD",
    "GitHub Actions", "GitLab CI", "Jenkins",
    "Git", "GitHub", "GitLab", "Bitbucket",
    "REST API", "GraphQL", "FastAPI", "Flask", "Django", "Spring Boot",
    "Prometheus", "Grafana", "ELK Stack", "Datadog", "Splunk",
    "IAM", "RBAC", "OAuth", "Data Security", "Encryption", "GDPR", "LGPD",
    "Linux", "Bash", "Shell Scripting", "Distributed Systems",
    "Microservices Architecture"
]

job_title_aliases = {
    "Data Engineer": ["data engineer", "Data Eng.", "Sr. Data Engineer", "jr data engineer", "  Data Engineer  "],
    "Data Analyst": ["data analyst", "Jr Data Analyst", "Senior Data Analyst", " BI / Data Analyst "],
    "Data Scientist": ["data scientist", "Senior Data Scientist", "sr data scientist"],
    "Machine Learning Engineer": ["ML Engineer", "machine learning engineer", "Sr. ML Engineer"],
    "Analytics Engineer": ["analytics engineer", "Analytics Eng."],
    "BI Analyst": ["bi analyst", "BI Specialist", "Power BI Analyst"],
    "Data Architect": ["data architect", "Senior Data Architect"],
    "Backend Engineer": ["backend engineer", "Software Backend Engineer"],
    "Software Engineer": ["software engineer", "Software Developer"]
}

location_aliases = {
    "São Paulo": ["São Paulo", "são paulo", "Sao Paulo", "SP - Sao Paulo", "São Paulo/SP", "  sao paulo "],
    "Rio de Janeiro": ["Rio de Janeiro", "rio de janeiro", "Rio de Janeiro - RJ", "RJ - Rio de Janeiro"],
    "Belo Horizonte": ["Belo Horizonte", "belo horizonte", "BH", "Belo Horizonte/MG"],
    "Curitiba": ["Curitiba", "curitiba", "Curitiba/PR"],
    "Porto Alegre": ["Porto Alegre", "porto alegre", "Porto Alegre/RS"],
    "Recife": ["Recife", "recife", "Recife/PE"],
    "Remote": ["Remote", "remote", "Remoto", "100% remoto", "Anywhere"]
}

skill_aliases = {
    "Python": ["Python", "python", " PYTHON "],
    "PySpark": ["PySpark", "pyspark", "PYSPARK"],
    "Apache Spark": ["Apache Spark", "Spark", "spark"],
    "PostgreSQL": ["PostgreSQL", "Postgres", "postgresql"],
    "SQL Server": ["SQL Server", "MS SQL Server", "sql server"],
    "Azure Databricks": ["Azure Databricks", "Databricks", "azure databricks"],
    "Apache Airflow": ["Apache Airflow", "Airflow", "airflow"],
    "Power BI": ["Power BI", "power bi", "POWER BI"],
    "CI/CD": ["CI/CD", "CICD", "ci cd"],
    "REST API": ["REST API", "REST APIs", "rest api"],
    "GraphQL": ["GraphQL", "graphql"],
    "Azure Data Factory": ["Azure Data Factory", "ADF", "azure data factory"],
    "BigQuery": ["BigQuery", "bigquery", "Google BigQuery"],
    "Apache Kafka": ["Apache Kafka", "Kafka", "kafka"],
    "dbt": ["dbt", "DBT"],
    "Terraform": ["Terraform", "terraform"],
    "Docker": ["Docker", "docker"],
    "Kubernetes": ["Kubernetes", "k8s", "K8S"]
}

extra_noise_skills = ["", " ", None, "N/A", "unknown", "misc", "Excel "]
