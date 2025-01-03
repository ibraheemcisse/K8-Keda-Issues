### KEDA Scaling with Minikube - Issues
---
**Overview**

This repository contains the setup for testing **KEDA (Kubernetes Event-Driven Autoscaler)** on **Minikube**, focusing on scaling one pod per HTTP request using the HTTP trigger. The project faced several challenges during implementation, which are documented here for review and further troubleshooting.

**Project Components**

### **1\. Application**

 A simple Rock-Paper-Scissors game written in Python and Flask.
    
*   Dockerized and deployed as myapp in the Kubernetes cluster.
    
### **2\. Key Kubernetes Manifests**

*   **deployment.yaml**: Deploys the myapp application.
    
*   **service.yaml**: Exposes the application within the cluster as a ClusterIP service.
    
*   **scaledobject.yaml**: Configures KEDA to scale myapp based on HTTP requests.
    

### **3\. KEDA HTTP Add-On**

*   Used to enable scaling based on HTTP triggers.
    

**Challenges Faced**
--------------------

### **1\. HTTP Scaler Not Found**

*   Reconciler error: no scaler found for type: http
    
*   **Observation**: The KEDA operator could not recognize the HTTP scaler, causing the ScaledObject to remain inactive.

### **2\. Service Exposure**

*   **Issue**: The service was configured as ClusterIP, making it inaccessible externally.
    
*   **Observation**: This restricted the ability to test HTTP requests from outside the cluster but I tried nodeport but it also did not work.
        
### **3\. Resource Constraints**

*   **Issue**: Minikube’s default resource allocation was insufficient for KEDA and the HTTP Add-On.
    
*   **Observation**: Resource contention led to performance issues during tests.
    
### **4\. Load Testing Timeout**

*   **Issue**: Load testing tools like hey timed out due to service misconfiguration or network issues.
    
*   **Observation**: HTTP requests failed with Client.Timeout exceeded while awaiting headers.
    
### **5\. Scaling Issues**

*   **Observation**: The ScaledObject showed READY=False and did not trigger scaling, even under simulated load.

Error logs:  failed to ensure HPA is correctly created for ScaledObjectno scaler found for type: http
    

### **6\. Networking Challenges**

*   **Issue**: Minikube's networking setup caused intermittent access issues to services.
    
*   **Observation**: The ClusterIP service was unreachable when accessed via DNS (myapp.default.svc.cluster.local).

### Error Logs and Output

```plaintext

1. Pods in `keda` Namespace:

NAME                                           READY   STATUS    RESTARTS   AGE
debug-pod                                      0/1     Error     0          42h
keda-add-ons-http-controller-manager-569c95b8bc-2zs7d   2/2     Running   22 (13h ago)   2d2h
keda-add-ons-http-external-scaler-5757c97b5c-n2jsc      1/1     Running   7              2d2h
keda-add-ons-http-external-scaler-5757c97b5c-vtxvp      1/1     Running   6 (13h ago)    2d2h
keda-add-ons-http-external-scaler-5757c97b5c-zn5dj      1/1     Running   7 (13h ago)    2d2h
keda-add-ons-http-interceptor-c8b97c46f-4mzzp           1/1     Running   5 (13h ago)    2d2h
keda-add-ons-http-interceptor-c8b97c46f-6wqs4           1/1     Running   6 (13h ago)    2d2h
keda-add-ons-http-interceptor-c8b97c46f-fgjxb           1/1     Running   6 (13h ago)    2d2h
keda-http-add-on-interceptor-fc6b45c7d-2vcjw            1/1     Running   5 (13h ago)    17h
keda-http-add-on-interceptor-fc6b45c7d-jsq8j            1/1     Running   5 (13h ago)    17h
keda-http-add-on-interceptor-fc6b45c7d-k29kz            1/1     Running   3 (13h ago)    17h
keda-http-add-on-operator-675bdfb55b-r8qjr              1/1     Running   3 (13h ago)    17h
keda-http-add-on-scaler-5fd5d76bc7-2ck7p                1/1     Running   6 (13h ago)    17h
keda-http-add-on-scaler-5fd5d76bc7-mvs5k                1/1     Running   6 (13h ago)    17h
keda-http-add-on-scaler-5fd5d76bc7-vrtxz                1/1     Running   6 (13h ago)    17h
keda-metrics-apiserver-6c7fb698db-c47sp                 1/1     Running   11 (13h ago)   2d2h
keda-operator-855c889db-4vhfx                           1/1     Running   18 (13h ago)   2d2h
myapp-99dddf697-mpqxb                                   1/1     Running   4 (13h ago)    42h

2. ScaledObjects in keda Namespace:

NAME                           SCALETARGETKIND       SCALETARGETNAME                MIN   MAX   READY   ACTIVE   FALLBACK   PAUSED   TRIGGERS   AUTHENTICATIONS   AGE
keda-add-ons-http-interceptor  apps/v1.Deployment    keda-add-ons-http-interceptor   3    50    True    False    False      Unknown  external                  2d2h
keda-http-add-on-interceptor   apps/v1.Deployment    keda-http-add-on-interceptor    3    50    True    False    False      Unknown  external                  17h
myapp-scaledobject             apps/v1.Deployment    myapp                           0    0     False   Unknown  False      Unknown  http                      17h

3. Deployment Status

NAME    READY   UP-TO-DATE   AVAILABLE   AGE
myapp   1/1     1            1           2d1h

4. Load Testing Output

Summary:
Total: 40.2525 secs
Slowest: 0.0000 secs
Fastest: 0.0000 secs
Average: NaN secs
Requests/sec: 2.4843

Response time histogram:
Latency distribution:

Details (average, fastest, slowest):
DNS+dialup: NaN secs, 0.0000 secs, 0.0000 secs
DNS-lookup: NaN secs, 0.0000 secs, 0.0000 secs
req write: NaN secs, 0.0000 secs, 0.0000 secs
resp wait: NaN secs, 0.0000 secs, 0.0000 secs
resp read: NaN secs, 0.0000 secs, 0.0000 secs

Status code distribution:
Error distribution:
[100] Get http://192.168.49.2:80: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)

5. KEDA Operator Logs

2024-12-18T21:38:19Z ERROR Reconciler error {"controller": "scaledobject", "controllerGroup": "keda.sh", "controllerKind": "ScaledObject", "ScaledObject": {"name":"rock-paper-scissors-scaler","namespace":"default"}, "namespace": "default", "name": "rock-paper-scissors-scaler", "reconcileID": "edcea0e9-aebf-4f6c-9e89-4e34c017a44a", "error": "no scaler found for type: http"}
