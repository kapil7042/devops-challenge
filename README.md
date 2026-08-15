# DevOps 90-Minute Infrastructure Challenge

## Overview

This project demonstrates a production-style application deployment using Docker, Kubernetes and GitHub Actions.

The application includes a Flask backend and PostgreSQL database.

The infrastructure includes:

- Docker containerization
- Kubernetes deployments and services
- GitHub Actions CI/CD
- Readiness and liveness probes
- Resource requests and limits
- Kubernetes Secret
- Intentional failure simulation
- Live debugging and recovery

## Architecture

Developer pushes code to GitHub.

GitHub Actions builds the Docker image and pushes it to Docker Hub.

A self-hosted GitHub Actions runner deploys the updated image to Kubernetes.

The Kubernetes cluster runs:

- Two Flask application replicas
- PostgreSQL database
- Application service
- PostgreSQL service

## Prerequisites

- Docker
- Minikube
- kubectl
- GitHub repository
- Docker Hub account
- GitHub Actions self-hosted runner

## Start Kubernetes

```bash
minikube start --cpus=2 --memory=4096