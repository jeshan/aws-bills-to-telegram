#!/usr/bin/env bash
set -e

aws s3 cp templates/template.yaml s3://${PUBLIC_BUCKET}/${PROJECT_NAME}-template.yaml
aws s3 cp templates/deployment-pipeline.yaml s3://${PUBLIC_BUCKET}/${PROJECT_NAME}-deployment-pipeline-template.yaml
