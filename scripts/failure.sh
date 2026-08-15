#!/bin/bash

set -e

kubectl set env deployment/my-app DB_HOST=wrong-host

kubectl rollout status deployment/my-app --timeout=60s || true

kubectl get pods

kubectl get deployment my-app

kubectl get endpoints my-app-service

kubectl logs -l app=my-app --tail=50