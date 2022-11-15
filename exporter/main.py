import json
import os
from time import sleep

from loguru import logger
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server


# Exporter parameters
EXPORTER_PORT = os.getenv("PORT", 8000)
CLUSTER_NAME = os.getenv("CLUSTER_NAME", "default")
TIME_PROMETHEUS = os.getenv("TIME_PROMETHEUS", 10)
NOVA_OUTPUT_PATH = os.getenv("NOVA_OUTPUT_PATH", "nova-output.json")

class NovaCollector(object):

    def __init__(self, nova_output, cluster_name):
        self.nova_output = nova_output
        self.cluster_name = cluster_name
        self.gauges = {}
    def collect(self):
        apps = json.loads(open(self.nova_output, 'r').read())
        # Recreate gauges to prevent multiple occurences of metrics
        self.gauges = {
            'helm_outdated': GaugeMetricFamily(
                'helm_outdated', 
                "Helm chart is outdated or not", 
                labels=['release', 'chart_name', 'namespace', 'installed_version', 'latest_version']
            ),
            'helm_deprecated': GaugeMetricFamily(
                'helm_deprecated', 
                "Helm chart is deprecated or not", 
                labels=['release', 'chart_name', 'namespace', 'installed_version', 'latest_version']
            )
        }
        for app in apps['helm']:
            label_values = [app['release'], app['chartName'], app['namespace'], app['Installed']['version'], app['Latest']['version']]
            deprecated = int(app['deprecated'])
            outdated = int(app['outdated'])
            self.gauges['helm_outdated'].add_metric(label_values, outdated)
            self.gauges['helm_deprecated'].add_metric(label_values, deprecated)

        yield self.gauges['helm_outdated']
        yield self.gauges['helm_deprecated']

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(EXPORTER_PORT)
    REGISTRY.register(NovaCollector(NOVA_OUTPUT_PATH, CLUSTER_NAME))
    while True:
        sleep(TIME_PROMETHEUS)