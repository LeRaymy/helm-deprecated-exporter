# helm-deprecated-exporter : 

This project's goal is to provide a simple [Prometheus](https://prometheus.io/) exporter, which exposes metrics about outdated and deprecated [Helm](https://helm.sh/) charts. It uses [nova](https://github.com/FairwindsOps/nova), a tool that scans a given [Kubernetes](https://kubernetes.io/fr/) cluster for installed Helm charts. It searches on all known Helm repositories if any updated version is available or if the current version of the chart is deprected.  

Once a week - or according to the schedule of your Kubernetes `cronjob` -, a Kubernetes Job launches a scan with [nova](https://github.com/FairwindsOps/nova), then, it updates a ConfigMap on which upon the Prometheus exporter is based.

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
