## Error Logs and Output

---

### 1. Pods and ScaledObject Status

#### Pods in `keda` Namespace

NAME READY STATUS RESTARTS AGE debug-pod 0/1 Error 0 42h keda-add-ons-http-controller-manager-569c95b8bc-2zs7d 2/2 Running 22 (13h ago) 2d2h keda-add-ons-http-external-scaler-5757c97b5c-n2jsc 1/1 Running 7 2d2h keda-add-ons-http-external-scaler-5757c97b5c-vtxvp 1/1 Running 6 (13h ago) 2d2h keda-add-ons-http-external-scaler-5757c97b5c-zn5dj 1/1 Running 7 (13h ago) 2d2h keda-add-ons-http-interceptor-c8b97c46f-4mzzp 1/1 Running 5 (13h ago) 2d2h keda-add-ons-http-interceptor-c8b97c46f-6wqs4 1/1 Running 6 (13h ago) 2d2h keda-add-ons-http-interceptor-c8b97c46f-fgjxb 1/1 Running 6 (13h ago) 2d2h keda-http-add-on-interceptor-fc6b45c7d-2vcjw 1/1 Running 5 (13h ago) 17h keda-http-add-on-interceptor-fc6b45c7d-jsq8j 1/1 Running 5 (13h ago) 17h keda-http-add-on-interceptor-fc6b45c7d-k29kz 1/1 Running 3 (13h ago) 17h keda-http-add-on-operator-675bdfb55b-r8qjr 1/1 Running 3 (13h ago) 17h keda-http-add-on-scaler-5fd5d76bc7-2ck7p 1/1 Running 6 (13h ago) 17h keda-http-add-on-scaler-5fd5d76bc7-mvs5k 1/1 Running 6 (13h ago) 17h keda-http-add-on-scaler-5fd5d76bc7-vrtxz 1/1 Running 6 (13h ago) 17h keda-metrics-apiserver-6c7fb698db-c47sp 1/1 Running 11 (13h ago) 2d2h keda-operator-855c889db-4vhfx 1/1 Running 18 (13h ago) 2d2h myapp-99dddf697-mpqxb 1/1 Running 4 (13h ago) 42h

yaml
Copy code

---

#### ScaledObjects in `keda` Namespace

NAME SCALETARGETKIND SCALETARGETNAME MIN MAX READY ACTIVE FALLBACK PAUSED TRIGGERS AUTHENTICATIONS AGE keda-add-ons-http-interceptor apps/v1.Deployment keda-add-ons-http-interceptor 3 50 True False False Unknown external 2d2h keda-http-add-on-interceptor apps/v1.Deployment keda-http-add-on-interceptor 3 50 True False False Unknown external 17h myapp-scaledobject apps/v1.Deployment myapp 0 0 False Unknown False Unknown http 17h

yaml
Copy code

---

### 2. Deployment Status

NAME READY UP-TO-DATE AVAILABLE AGE myapp 1/1 1 1 2d1h

yaml
Copy code

---

### 3. Load Testing Output

#### Summary

Total: 40.2525 secs Slowest: 0.0000 secs Fastest: 0.0000 secs Average: NaN secs Requests/sec: 2.4843

shell
Copy code

#### Response Time Histogram

Latency distribution:

shell
Copy code

#### Details (Average, Fastest, Slowest)

DNS+dialup: NaN secs, 0.0000 secs, 0.0000 secs DNS-lookup: NaN secs, 0.0000 secs, 0.0000 secs req write: NaN secs, 0.0000 secs, 0.0000 secs resp wait: NaN secs, 0.0000 secs, 0.0000 secs resp read: NaN secs, 0.0000 secs, 0.0000 secs

shell
Copy code

#### Status Code Distribution

Error distribution: [100] Get http://192.168.49.2:80: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)

yaml
Copy code

---

### 4. KEDA Operator Logs

2024-12-18T21:38:19Z ERROR Reconciler error {"controller": "scaledobject", "controllerGroup": "keda.sh", "controllerKind": "ScaledObject", "ScaledObject": {"name":"rock-paper-scissors-scaler","namespace":"default"}, "namespace": "default", "name": "rock-paper-scissors-scaler", "reconcileID": "edcea0e9-aebf-4f6c-9e89-4e34c017a44a", "error": "no scaler found for type: http"}

yaml
Copy code
### 1. ## Error Logs and Output

### 1. Pods and ScaledObject Status

#### Pods in `keda` Namespace:

```plaintext
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
ScaledObjects in keda Namespace:
plaintext
Copy code
NAME                           SCALETARGETKIND       SCALETARGETNAME                MIN   MAX   READY   ACTIVE   FALLBACK   PAUSED   TRIGGERS   AUTHENTICATIONS   AGE
keda-add-ons-http-interceptor  apps/v1.Deployment    keda-add-ons-http-interceptor   3    50    True    False    False      Unknown  external                  2d2h
keda-http-add-on-interceptor   apps/v1.Deployment    keda-http-add-on-interceptor    3    50    True    False    False      Unknown  external                  17h
myapp-scaledobject             apps/v1.Deployment    myapp                           0    0     False   Unknown  False      Unknown  http                      17h
2. Deployment Status
plaintext
Copy code
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
myapp   1/1     1            1           2d1h
3. Load Testing Output
plaintext
Copy code
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
4. KEDA Operator Logs
plaintext
Copy code
2024-12-18T21:38:19Z ERROR Reconciler error {"controller": "scaledobject", "controllerGroup": "keda.sh", "controllerKind": "ScaledObject", "ScaledObject": {"name":"rock-paper-scissors-scaler","namespace":"default"}, "namespace": "default", "name": "rock-paper-scissors-scaler", "reconcileID": "edcea0e9-aebf-4f6c-9e89-4e34c017a44a", "error": "no scaler found for type: http"}
