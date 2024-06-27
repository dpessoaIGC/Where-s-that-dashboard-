from catalogue.create_catalogue import get_dashboard_catalog, create_update_catalog
from catalogue.search import get_dashboards

if __name__ == "__main__":
    catalog = get_dashboard_catalog()
    create_update_catalog(catalog)
    get_dashboards("where can I find the top sales?", catalog)