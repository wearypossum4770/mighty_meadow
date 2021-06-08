import {readFileSync, writeFileSync} from 'fs'
let code = [
    {

        "code_value":"Z20.822",
        "coding_system":"icd_10",
        "has_category_code":"CM",
        "used_to_diagnose":"COVID-19 Exposure",
        "condition_description":"Contact with and (suspected) exposure to COVID-19"
          },
          {
            "code_value":"Z11.52",
            "coding_system":"icd_10",
            "has_category_code":"CM",
            "used_to_diagnose":"COVID-19 Exposure",
            "condition_description":"Encounter for screening for COVID-19"
             
          },
          {
            "code_value":"Z86.16",
            "coding_system":"icd_10",
            "has_category_code":"CM",
            "used_to_diagnose":"COVID-19 History",
            "condition_description":"Personal history of COVID-19"
             
          },
          {
            "code_value":"U07.1",
            "coding_system":"icd_10",
            "has_category_code":"CM",
            "used_to_diagnose":"COVID-19 Exposure",
            "condition_description":"",
            "related_condition":null
             
          },
          {
            "code_value":"Z20.828",
            "coding_system":"icd_10",
            "has_category_code":"CM",
            "used_to_diagnose":"COVID-19 Exposure",
            "condition_description":"Contact with and (suspected) exposure to other viral communicable diseases",
            "related_condition":"fever"
          },
]
let data = JSON.parse(readFileSync('./appointments/fixtures/appointmentinit.json'))

code.forEach((c, i) => {
    data.push(
        {
            "model": "appointments.medicalcondition",
            "pk": i+1,
            "fields": {
              "is_symptomatic": false,
              "code_value":c.code_value,
              "coding_system":c.coding_system,
              "has_category_code":c.has_category_code,
              "used_to_diagnose":c.used_to_diagnose,
              "condition_description":c.condition_description,
              "related_condition":c?.related_condition,
            }
          },
    )
})

writeFileSync('./appointments/fixtures/appointmentinit.json', JSON.stringify(data))