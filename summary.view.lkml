view: summary {
  sql_table_name: part_d_2017.summary ;;

  dimension: aggregate_cost_paid_for_part_d_claims {
    type: number
    sql: ${TABLE}."Aggregate Cost Paid for Part D Claims" ;;
  }
}
