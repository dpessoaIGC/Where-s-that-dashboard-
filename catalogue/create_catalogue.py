import looker_sdk #Note that the pip install required a hyphen but the import is an underscore.
import os #We import os here in order to manage environment variables for the tutorial. You don't need to do this on a local system or anywhere you can more conveniently set environment variables.
import json #This is a handy library for doing JSON work.
import pandas as pd
import pandas_gbq

def get_dashboard_catalog(looker_sdk_instance=None):
    """
    This function retrieves the dashboard catalog from the Looker instance and returns it as a dictionary.

    :param looker_sdk_instance :
    :return:
    """
    if looker_sdk_instance is None:
        looker_sdk_instance = looker_sdk.init40()  # This initializes the Looker SDK. Authentication is governed by the looker.ini file.

    responses = looker_sdk_instance.all_dashboards(fields="id, title, description")
    dashboard_catalog = {r.id: {"description": r.description, "title": r.title}
    for r in responses}
    return dashboard_catalog

def create_update_catalog(catalog):
    """Updates the dashboard catalog BigQuery table.

    :param catalog:
    :return:
    """
    dashboard_catalog = pd.DataFrame.from_dict(catalog, orient="index")
    dashboard_catalog = dashboard_catalog.rename_axis('dashboard_index').reset_index()
    pandas_gbq.to_gbq(dashboard_catalog, 'dashboard_query_results.dashboard_catalog2',
                      project_id='queryable-dashboard-catalog', if_exists='replace')

