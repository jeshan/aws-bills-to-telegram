#!/usr/bin/env bash
set -e

BRANCH=`git rev-parse --abbrev-ref HEAD`
echo "On branch $BRANCH"

aws s3 sync --delete --exclude "*" --include "config/*" --exclude "config/config.yaml" --exclude "config/app/dev/*" --exclude "config/app/deployment/*" . s3://${PRIVATE_BUCKET}/github.com/jeshan/${PROJECT_NAME}/$BRANCH/
