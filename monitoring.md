## 📈 Monitoring & Observability

This section explains how monitoring and observability are implemented for the Flask application deployed on Kubernetes.

---

### 🔹 Basic Metrics

To monitor application-level metrics like request count, response time, and error rate:

#### ✅ Flask + Prometheus Exporter

* Integrate [`prometheus_flask_exporter`](https://github.com/rycus86/prometheus_flask_exporter) in the Flask application.
* It exposes metrics at `/metrics` that Prometheus can scrape.

Example setup in Flask:

```python
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)
```

* Common metrics collected include:

  * HTTP request count
  * Request duration (latency)
  * Exception count

#### ✅ Optional: Grafana for Visualization

* Connect Prometheus as a data source to Grafana.
* Create dashboards to track throughput, latency, and errors.

---

### 🔹 Health Check Monitoring

Kubernetes provides basic health checks, but production-grade monitoring goes further:

#### ✅ Kubernetes Probes

Defined in your `deployment.yaml`:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 5
```

#### ✅ External Health Checks

* Use tools like **UptimeRobot**, **Pingdom**, or **StatusCake** to monitor the external LoadBalancer endpoint.
* Useful for real-world availability checks.

#### ✅ Prometheus Alerts (Optional)

* Set up Prometheus Alertmanager to trigger alerts:

  * When pods crash
  * When `/health` returns failure
  * When latency increases

Example alert rule:

```yaml
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
  for: 2m
  labels:
    severity: warning
  annotations:
    summary: "High 5xx error rate"
```

---

### 🔹 Logging

Effective logging makes troubleshooting easier.

#### ✅ Pod-Level Logging

* Flask logs to `stdout`, which is automatically captured by Kubernetes.
* View logs via:

```sh
kubectl logs -l app=flask-app
```

#### ✅ Optional: Centralized Logging

For production-grade observability, integrate:

| Component       | Purpose                                |
| --------------- | -------------------------------------- |
| Fluent Bit      | Lightweight log shipper                |
| Grafana Loki    | Log aggregation & search               |
| CloudWatch Logs | Central AWS log management             |
| Kibana          | Powerful log search with Elasticsearch |

Log architecture example:

```
[Pod Logs] → Fluent Bit → Loki / CloudWatch → Grafana / Kibana
```

---

### 📁 Optional Separate File

This content can be linked from the README or maintained as a standalone `monitoring.md` file for clarity and maintainability.