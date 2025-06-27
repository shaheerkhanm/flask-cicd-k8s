## 🔒 Security & Best Practices

This section outlines security measures and best practices applied throughout the CI/CD and Kubernetes infrastructure.

---

### 🏠 Image Security

#### ✅ Image Scanning

* Enable automatic image scanning via Docker Hub or use tools like **Trivy** during CI to catch vulnerabilities.

#### ✅ Private Image Repository

* Use Docker Hub private repos or AWS ECR to restrict unauthorized access to images.

---

### ⚖️ IAM & RBAC Controls

#### ✅ IAM Best Practices

* Use IAM roles with least privilege for EKS and CI/CD pipeline.
* Avoid long-lived static credentials.

#### ✅ Kubernetes RBAC

* Apply RBAC rules to limit access to deployments, logs, secrets.

Example: `RBAC.yaml`

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: read-only-role
rules:
- apiGroups: [""]
  resources: ["pods", "services"]
  verbs: ["get", "list"]
```

---

### 🔐 Secret Management

#### ✅ GitHub Secrets

* CI pipeline secrets are stored securely in GitHub Actions (`Settings > Secrets`).

#### ✅ Kubernetes Secrets

* Store API keys, DB passwords as `Secret` objects:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: flask-secrets
stringData:
  DB_PASSWORD: mypassword
```

---

### 🚫 Network Policies

* Restrict pod communication using Kubernetes `NetworkPolicy`.

Example: `network-policy.yaml`

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web
spec:
  podSelector:
    matchLabels:
      app: flask-app
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 5000
```

---

### ♻️ Auto-Rollbacks

* Use Kubernetes deployment strategies that support rollback on failure.
* Monitor rollout status with `kubectl rollout status deployment/flask-app`

---

### ✉️ Notifications (Optional)

* Integrate GitHub Actions or Prometheus with Slack, Teams, or Email for deployment status alerts.

---

These practices provide:

* Runtime isolation
* Credential safety
* Minimized attack surface
* Alerting on misconfigurations

Security is an ongoing effort. Future enhancements can include:

* OPA/Gatekeeper for policy enforcement
* PodSecurityContext for runtime restrictions
* Service Mesh (e.g., Istio) for encrypted pod-to-pod traffic