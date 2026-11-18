sites

site_id, site_name, country, target_enrollment

patients

patient_id, site_id, arm, enrollment_date, age, sex, baseline_sbp, status (active, completed, withdrawn)

visits

visit_id, patient_id, visit_name, scheduled_date, actual_date, sbp, attended (yes/no)

labs

lab_id, patient_id, visit_name, test_name, value, unit

adverse_events

ae_id, patient_id, ae_term, severity (mild, moderate, severe), start_date, serious (yes/no)

events (for survival analysis)

patient_id, event_occurred (yes/no), time_to_event_days