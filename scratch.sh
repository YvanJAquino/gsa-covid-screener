gcloud functions deploy func-gsa-covid-screening-ps-to-bq \
    --runtime=python39 \
    --trigger-event=google.pubsub.topic.publish \ 
    --trigger-resource="projects/x-oxygen-322223/topics/screenings"