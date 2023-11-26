"""
## Delete an OpenSearch Index

This DAG deletes an OpenSearch index using the OpenSearchHook.
It is meant for development purposes.
"""

from airflow.decorators import dag, task
from airflow.providers.opensearch.hooks.opensearch import OpenSearchHook
from pendulum import datetime

INDEX_TO_DELETE = "customer_feedback"
OPENSEARCH_CONN_ID = "opensearch_default"


@dag(
    start_date=datetime(2023, 10, 18),
    schedule=None,
    catchup=False,
)
def delete_opensearch_index():
    @task
    def delete_index(index_name: str, conn_id) -> None:
        client = OpenSearchHook(open_search_conn_id=conn_id, log_query=True).client
        client.indices.delete(index_name)

    delete_index(index_name=INDEX_TO_DELETE, conn_id=OPENSEARCH_CONN_ID)


delete_opensearch_index()
