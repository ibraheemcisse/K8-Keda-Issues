KEDA Scaling with Minikube - Challenges

Overview

This repository contains the setup for testing KEDA (Kubernetes Event-Driven Autoscaler) on Minikube, focusing on scaling one pod per HTTP request using the HTTP trigger. The project faced several challenges during implementation, which are documented here for review and further troubleshooting.

Project Components

1. Application

A simple Rock-Paper-Scissors game written in Python and Flask.

Dockerized and deployed as myapp in the Kubernetes cluster.

2. Key Kubernetes Manifests

deployment.yaml: Deploys the myapp application.

service.yaml: Exposes the application within the cluster as a ClusterIP service.

scaledobject.yaml: Configures KEDA to scale myapp based on HTTP requests.

3. KEDA HTTP Add-On

Used to enable scaling based on HTTP triggers.

Challenges Faced

1. HTTP Scaler Not Found

Error:

Reconciler error: no scaler found for type: http

Observation: The KEDA operator could not recognize the HTTP scaler, causing the ScaledObject to remain inactive.

2. Service Exposure

Issue: The service was configured as ClusterIP, making it inaccessible externally.

Observation: This restricted the ability to test HTTP requests from outside the cluster.

3. Ingress Configuration

Issue: Enabling Ingress for external traffic proved challenging.

Observation: Although Minikube's Ingress add-on was enabled, there were configuration mismatches, and the service remained unreachable.

4. Resource Constraints

Issue: Minikube’s default resource allocation was insufficient for KEDA and the HTTP Add-On.

Observation: Resource contention led to performance issues during tests.

5. Load Testing Timeout

Issue: Load testing tools like hey timed out due to service misconfiguration or network issues.

Observation: HTTP requests failed with Client.Timeout exceeded while awaiting headers.

6. Scaling Issues

Observation: The ScaledObject showed READY=False and did not trigger scaling, even under simulated load.

Error Logs:

failed to ensure HPA is correctly created for ScaledObject
no scaler found for type: http

7. Networking Challenges

Issue: Minikube's networking setup caused intermittent access issues to services.

Observation: The ClusterIP service was unreachable when accessed via DNS (myapp.default.svc.cluster.local).

Next Steps

The issues listed above need further investigation and resolution. This document serves as a summary for review and feedback. Please advise on possible solutions or additional steps to troubleshoot these challenges.
