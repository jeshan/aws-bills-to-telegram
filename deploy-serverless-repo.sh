#!/usr/bin/env bash

BUCKET=`aws ssm get-parameter --name default-sam-bucket --query Parameter.Value --output text`

aws cloudformation package --template-file templates/template.yaml --s3-bucket ${BUCKET} --s3-prefix serverlessrepo --output-template-file templates/packaged-template.yaml

sam publish --template templates/packaged-template.yaml --region us-east-1
