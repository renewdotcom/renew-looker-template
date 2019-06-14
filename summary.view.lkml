view: summary {
  sql_table_name: part_d_2017.summary ;;

  dimension: aggregate_cost_paid_for_part_d_claims {
    type: number
    sql: ${TABLE}."Aggregate Cost Paid for Part D Claims" ;;
  }

  dimension: aggregate_cost_paid_for_part_d_claims_for_beneficiaries_65 {
    type: number
    sql: ${TABLE}."Aggregate Cost Paid for Part D Claims for Beneficiaries 65+" ;;
  }

  dimension: aggregate_cost_share_for_beneficiaries_with_low_income_subsidy {
    type: number
    sql: ${TABLE}."Aggregate Cost Share for Beneficiaries with Low Income Subsidy" ;;
  }

  dimension: aggregate_cost_share_for_beneficiaries_with_no_low_income_subsi {
    type: number
    sql: ${TABLE}."Aggregate Cost Share for Beneficiaries with No Low Income Subsi" ;;
  }

  dimension: antibiotic_drug_flag {
    type: string
    sql: ${TABLE}."Antibiotic Drug Flag" ;;
  }

  dimension: antipsychotic_drug_flag {
    type: string
    sql: ${TABLE}."Antipsychotic Drug Flag" ;;
  }

  dimension: beneficiary_65_suppression_flag {
    type: string
    sql: ${TABLE}."Beneficiary 65+ Suppression Flag" ;;
  }

  dimension: drug_name {
    type: string
    sql: ${TABLE}."Drug Name" ;;
  }

  dimension: ge65_suppression_flag {
    type: string
    sql: ${TABLE}."GE65 Suppression Flag" ;;
  }

  dimension: generic_name {
    type: string
    sql: ${TABLE}."Generic Name" ;;
  }

  dimension: longacting_opioid_drug_flag {
    type: string
    sql: ${TABLE}."Long-Acting Opioid Drug Flag" ;;
  }

  dimension: number_of_medicare_beneficiaries {
    type: number
    sql: ${TABLE}."Number of Medicare Beneficiaries" ;;
  }

  dimension: number_of_medicare_beneficiaries_65 {
    type: number
    sql: ${TABLE}."Number of Medicare Beneficiaries 65+" ;;
  }

  dimension: number_of_medicare_part_d_claims {
    type: number
    sql: ${TABLE}."Number of Medicare Part D Claims" ;;
  }

  dimension: number_of_medicare_part_d_claims_for_beneficiaries_65 {
    type: number
    sql: ${TABLE}."Number of Medicare Part D Claims for Beneficiaries 65+" ;;
  }

  dimension: number_of_prescribers {
    type: number
    sql: ${TABLE}."Number of Prescribers" ;;
  }

  dimension: number_of_standardized_30day_part_d_fills {
    type: number
    sql: ${TABLE}."Number of Standardized 30-Day Part D Fills" ;;
  }

  dimension: number_of_standardized_30day_part_d_fills_for_beneficiaries_6 {
    type: number
    sql: ${TABLE}."Number of Standardized 30-Day Part D Fills for Beneficiaries 6" ;;
  }

  dimension: opioid_drug_flag {
    type: string
    sql: ${TABLE}."Opioid Drug Flag" ;;
  }

  measure: count {
    type: count
    drill_fields: [drug_name, generic_name]
  }
}
