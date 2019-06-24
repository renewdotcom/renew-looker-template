view: summary {
  sql_table_name: part_d_2017.summary ;;

  dimension: pk1_aggregate_cost_paid_for_part_d_claims {
    type: number
    hidden: yes
    description: "This is a description"
    primary_key: yes
    sql: ${TABLE}."Aggregate Cost Paid for Part D Claims" ;;
  }
}
