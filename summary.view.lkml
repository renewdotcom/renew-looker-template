view: summary {
  sql_table_name: part_d_2017.summary ;;

  dimension: pk1_sample_param {
    type: number
    hidden: yes
    description: "This is a description"
    primary_key: yes
    sql: ${TABLE}."Aggregate Cost Paid for Part D Claims" ;;
  }
}
