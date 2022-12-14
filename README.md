# helm-deprecated-exporter : is there an update for my Helm chart ?  

This project's goal is to provide a simple [Prometheus](https://prometheus.io/) exporter, which exposes metrics about outdated and deprecated [Helm](https://helm.sh/) charts. It uses [nova](https://github.com/FairwindsOps/nova), a tool that scans a given [Kubernetes](https://kubernetes.io/) cluster for installed Helm charts. It searches on all known Helm repositories if any updated version is available or if the current version of the chart is deprected.  

Once a week - or according to the schedule of your Kubernetes `cronjob` -, a Kubernetes Job launches a scan with [nova](https://github.com/FairwindsOps/nova), then, it updates a ConfigMap on which upon the Prometheus exporter is based.

# Requirements
- A kubernetes cluster
- [Helm](https://helm.sh/) v3 or higher
- A [prometheus](https://prometheus.io/docs/prometheus/latest/installation/) cluster

# Helm chart repository

1. Add a new Helm repository

```
helm repo add helm-deprecated-exporter https://leraymy.github.io/helm-deprecated-exporter/
```

2. Refresh the repository information

```
helm repo update
```

3. Search for all available charts in this repository

```
helm search repo helm-deprecated-exporter --versions
```
Or list the latest development/unstable versions
```
helm search repo helm-deprecated-exporter --versions
```

# Configuration
The configuration is done via `values.yaml` and for complete details, you should refer to the [repository](https://github.com/LeRaymy/helm-deprecated-exporter/blob/gh-pages/helm/values.yaml).

# Installation
To install the helm-deprecated-exporter chart:
```
helm upgrade --install --namespace helm-deprecated --create-namespace helm-deprecated helm-deprecated-exporter/helm-deprecated-exporter -f values.yaml
```
To uninstall the chart:
```
helm uninstall --namespace helm-deprecated helm-deprecated
```
# Metrics exposed by the exporter  

## Helm outdated

This gauge lets you know if the installed version of your helm chart is outdated (` = 1.0 `) or not (` = 0.0 `).

```
helm_outdated{chart_name="argo-cd",installed_version="4.5.4",latest_version="5.14.3",namespace="argocd",release="argo-cd"} 1.0
```

## Helm deprecated

This gauge lets you know if the installed version of your helm chart is deprecated (` = 1.0 `) or not (` = 0.0 `).

```
helm_deprecated{chart_name="kube-prometheus-stack",installed_version="42.0.0",latest_version="42.1.0",namespace="monitoring-system",release="prometheus"} 0.0
```
