# The name of this view in Looker is "Dashboard Catalog"
view: dashboard_catalog {
  # The sql_table_name parameter indicates the underlying database table
  # to be used for all fields in this view.
  sql_table_name: `queryable-dashboard-catalog.dashboard_query_results.dashboard_catalog` ;;

  # No primary key is defined for this view. In order to join this view in an Explore,
  # define primary_key: yes on a dimension that has no repeated values.

    # Here's what a typical dimension looks like in LookML.
    # A dimension is a groupable field that can be used to filter query results.
    # This dimension will be called "Dashboard Index" in Explore.

  dimension: dashboard_index {
    type: string
    sql: ${TABLE}.dashboard_index ;;
  }

  dimension: description {
    type: string
    sql: ${TABLE}.description ;;
  }

  dimension: title {
    type: string
    sql: ${TABLE}.title ;;
  }
  measure: count {
    type: count
  }
}
