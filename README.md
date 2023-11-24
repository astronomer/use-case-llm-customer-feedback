Use Cohere and OpenSearch to analyze customer feedback in an MLOps pipeline
===========================================================================

This repository contains the DAG code used in the [Use Cohere and OpenSearch to analyze customer feedback in an MLOps pipeline use case](https://docs.astronomer.io/learn/use-case-llm-customer-feedback). 

The DAG in this repository uses the following packages:

- [Airflow Cohere provider](https://airflow.apache.org/docs/apache-airflow-providers-cohere/stable/index.html).
- [Airflow OpenSearch provider](https://airflow.apache.org/docs/apache-airflow-providers-opensearch/stable/index.html).
- [Cohere python client](https://docs.cohere.ai/quickstart).

# How to use this repository

This section explains how to run this repository with Airflow. Note that you will need to copy the contents of the `.env_example` file to a newly created `.env` file and provide your own value for `<your-cohere-api-key>`. You can find your Cohere API key in the [Cohere dashboard](https://dashboard.cohere.com/api-keys), a free account is sufficient to run this example.

Download the [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) to run Airflow locally in Docker. `astro` is the only package you will need to install locally.

1. Run `git clone https://github.com/astronomer/airflow-pgvector-tutorial.git` on your computer to create a local clone of this repository.
2. Install the Astro CLI by following the steps in the [Astro CLI documentation](https://docs.astronomer.io/astro/cli/install-cli). Docker Desktop/Docker Engine is a prerequisite, but you don't need in-depth Docker knowledge to run Airflow with the Astro CLI.
3. Run `astro dev start` in your cloned repository.
4. After your Astro project has started. View the Airflow UI at `localhost:8080`.

In this project `astro dev start` spins up 6 Docker containers:

- The Airflow webserver, which runs the Airflow UI and can be accessed at `https://localhost:8080/`.
- The Airflow scheduler, which is responsible for monitoring and triggering tasks.
- The Airflow triggerer, which is an Airflow component used to run deferrable operators.
- The Airflow metadata database, which is a Postgres database that runs on port 5432.
- A container running a mock API that simulates a customer feedback system, accessible at `http://localhost:5000/`.
- A local OpenSearch instance that runs on port 9200.

## Resources

- [Use Cohere and OpenSearch to analyze customer feedback in an MLOps pipeline use case](https://docs.astronomer.io/learn/use-case-llm-customer-feedback). 
- [Orchestrate OpenSearch operations with Apache Airflow](https://docs.astronomer.io/learn/airflow-opensearch).
- [Orchestrate Cohere LLMs with Apache Airflow](https://docs.astronomer.io/learn/airflow-cohere)
- [Airflow OpenSearch provider documentation](https://airflow.apache.org/docs/apache-airflow-providers-opensearch/stable/index.html).
- [Airflow Cohere provider documentation](https://airflow.apache.org/docs/apache-airflow-providers-cohere/stable/index.html).
- [Cohere documentation](https://docs.cohere.com/).
- [OpenSearch documentation](https://opensearch.org/docs/latest/).