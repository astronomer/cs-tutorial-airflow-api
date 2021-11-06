# Airflow Stable REST API Demo
The `main_dev.py` and `main_prod.py` scripts will demonstrate how to use the Airflow 2.0 Stable REST API via the python requests library. The Airflow Stable REST API documentation is located [here](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html).

## Pre-requisites
 - Astro CLI - see quickstart guide [here](https://www.astronomer.io/docs/enterprise/v0.16/develop/cli-quickstart)
 - Docker
 - Astronomer Airflow Instance (if you plan on running the `main_prod.py` script)

## Steps to use main_dev.py
*main_dev.py runs API requests against a locally running instance of Airflow (in Docker)*
 1. On your terminal navigate to a root directory where you want your project to be located
 2. Create a project directory `mkdir airlfow-api-demo && cd airflow-api-demo`
 3. Initialize an Airflow project using `astro dev init`
 4. Spin up the project in Docker using `astro dev start`
 5. Navigate to a root directory where you can clone this repository
 6. Clone this repository using `git clone git@github.com:astronomer/cs-tutorial-airflow-api.git`
 7. In the newly cloned repository, the `main_dev.py` script can now be run with docker running Airflow locally

After following these steps, you should be ready to run the methods in the `main_dev.py` script

___

## Steps to use main_prod.py
*main_prod.py runs API requests against a production instance of Airflow in an Astronomer deployment*
 1. On your terminal navigate to a root directory where you can clone this repository
 2. Clone this repository using `git clone git@github.com:astronomer/cs-tutorial-airflow-api.git`
 3. In the newly cloned repository, create a file named `secrets.py` (this file is excluded from the repository due to `.gitignore`)
 4. Add a the following variables:

    ```
    deployment_name = "<your_deployment_name>"
    release_name = "<your_release_name>"
    airflow_api_key = "<your_api_key>"
    ```
    
 After following these steps, you should be ready to run the methods in the `main_prod.py` script
