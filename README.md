# o11y-pipeline-router

Google Cloud Function for routing data from the observability pipeline

## Deployment

```sh
$ gcloud beta functions deploy pipeline-router \
    --env-vars-file env.yaml \
    --update-labels obs-pipeline= \
    --runtime python37 \
    --entry-point handle_message \
    --trigger-resource pipeline \
    --trigger-event google.pubsub.topic.publish \
    --retry
```

