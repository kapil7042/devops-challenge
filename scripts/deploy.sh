#!/bin/bash

set -e

kubectl apply -f k8s/secret.yaml

kubectl apply -f k8s/postgres.yaml

kubectl rollout status deployment/postgres --timeout=120s

kubectl apply -f k8s/deployment.yaml

kubectl apply -f k8s/service.yaml

kubectl rollout status deployment/my-app --timeout=120s

kubectl get deployments

kubectl get pods

kubectl get services