
view: dashboard_catalog {
  derived_table: {
   sql: select *
      from `queryable-dashboard-catalog.dashboard_query_results.dashboard_catalog`;;
  }

  # measure: count {
  #   type: count
  #   drill_fields: [detail*]
  # }

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


  parameter: request {
    type: string
    label: "Request"
    default_value: "Where can I find the top sales?"
  }

}
