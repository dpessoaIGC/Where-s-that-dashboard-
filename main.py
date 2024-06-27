from catalogue import get_dashboard_catalog, create_update_catalog

if __name__ == "__main__":
    catalog = get_dashboard_catalog()
    create_update_catalog(catalog)