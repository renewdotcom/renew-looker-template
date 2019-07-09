view: summary_sample {
  sql_table_name: part_d_2017.summary ;;

  dimension: pk1_sample_param {
    hidden: yes
    primary_key: yes
    type: string
    description: "Drug Name"
    sql: ${TABLE}.drug_name ;; # The name as it appears in the database
  }

  dimension: another_sample_param {
    type: number
    description: "Generic Name for Drug"
    sql: ${TABLE}.generic_name ;;
  }

  measure: count {
    type: count
    filters: {
      field: pk1_sample_param
      value: "-null"
    }
  }

}
