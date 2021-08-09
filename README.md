# gsa-covid-screener

See cloudbuild.yaml for instructions

gcloud builds submit --substitutions _DATASET=gsa,_TABLE_ID=covid_screenings

Requirements:
  Create a new project.
  Enable the appropriate APIs: Compute Engine, App Engine, Pub/Sub, BigQuery, Cloud Functions, Cloud Build, App Engine Admin API
  YOU MUST ENABLE THE APP ENGINE ADMIN API!
  Configure the Cloud Build Service Account:
    Console -> Cloud Build -> Settings: ENABLE Cloud Functions, App Engine, Compute Engine
    IAM & Admin -> IAM: Add BigQueryAdmin, Pub/Sub Admin to Cloud Build Service Account (###...@cloudbuild.gserviceaccount.com)

Instructions: 
  Get a copy of this source via github and review the cloudbuild.yaml file closely.
  run the gcloud builds submit command as above (gcloud builds submit --substitutions _DATASET=gsa,_TABLE_ID=covid_screenings)
  test..!

Troubleshooting:
  Sometimes the Cloud Build - Service Account Enablement doesn't work well.  You may need to manually add 
  
