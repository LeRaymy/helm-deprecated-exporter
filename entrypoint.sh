#!/bin/sh

export KUBECONFIG='/root/.kube/config'

# Run nova 
/nova -a --output-file /tmp/nova-output.json find

# Create configmap from nova output
kubectl --kubeconfig='/root/.kube/config' create configmap nova-output --dry-run=client -o yaml --from-file=/tmp/nova-output.json | kubectl apply -f -
