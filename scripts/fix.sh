#!/bin/bash

set -e

kubectl set env deployment/my-app DB_HOST=postgres-service

kubectl rollout status deployment/my-app --timeout=120s

kubectl get pods

kubectl get endpoints my-app-service