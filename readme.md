docker system prune

Info:
https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

# Download docker-copmpose
$curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.1/docker-compose.yaml'

# Create volume folders
$mkdir -p ./dags ./logs ./plugins

# Create .env file
$echo -e "AIRFLOW_UID=$(id -u)" > .env

# Initialize the database
$docker-compose up airflow-init

# Cleaning-up the environment
Run in the directory you downloaded the docker-compose.yaml file:

$docker-compose down --volumes --remove-orphans command 

Remove the whole directory where you downloaded the docker-compose.yaml file rm -rf '<DIRECTORY>'
Re-download the docker-compose.yaml file
Re-start following the instructions from the very beginning in this guide

# Running Airflow
$docker-compose up


# Running the CLI commands
Download a optional wrapper scripts that will allow you to run commands with a simpler command.

$curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.1/airflow.sh'
$chmod +x airflow.sh

Now you can run commands easier.

./airflow.sh info
./airflow.sh bash
./airflow.sh python