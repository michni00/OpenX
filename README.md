# DevOps for the Data Science team intern

1. Create a web app backend (without frontend).

Implemented in Python using FastAPI framework and located in `backend` directory. The unique identifier is created with __uuid__ module stored in __app.state.app_id__ variable.

2. Create a docker image to run the application.

Created a __Dockerfile__ which creates an image with a preinstalled python slim version, downloads all the listed dependencies (didn't version them since it is a small preview project). Then the application is served through the uvicorn server bound to localhost on port 8080.

3. Create a helm chart to deploy your app in the Kubernetes (k8s) environment.

After installing and initializing both __Minikube__ and __Helm__ I have pushed the docker image to docker hub. After that I have used the command `helm create <name>` to create a simple chart. The app is scaled automatically based on the CPU usage limit of __.5__ of a single core and distributed within __1-5__ replicas depending on the demand, upping its size after reaching 50% of the CPU utilization across all pods.
```
limits:
  cpu: 500m
requests:
  cpu: 500m

autoscaling:
  enabled: true
  minReplicas: 1
  maxReplicas: 5
  targetCPUUtilizationPercentage: 50
```

The port is configurable through passing its value when using the command `helm install <name> <path> --set service.port=<port_number>`. The default value is __8080__.
To change the node port that it is being hosted on use parameter `--set service.nodeport=<node_port_number>` which should be between 30000-32767.
If we use __LoadBalancer__ (why it is not used here is explained later), port number would be assigned in a similar way.

I also decided to change the port type from __ClusterIP__ to __NodePort__ to make it accessible from outside the Kubernetes cluster.

If I had access to a cloud environment I would use __LoadBalancer__ and set ports correctly the way they are mentioned in the 'expected architecture of your solution' but sadly I do not.

Helm value file present in directory `Helm`, it was the only file after initialization that I have changed the content of.

4. Use a locust as a client for your app.

Locustfile and Dockerfile necessary for the implementation are located in `locust` directory. I did not publish it on DockerHub and did not create a Helm chart out of it because it is hosted on a __NodePort__ as mentioned above so connecting to it and giving requests through another machine is sadly not possible (if I could publish it as a LoadBalancer I would do so) but there is an upside to it. When creating a comparison of performance there will be no ping or packet loss issue and the measurements should be precise compared to the cloud implementation. I have created a Dockerfile though. If I had access to __LoadBalancer__ I would push an image created by the dockerfile to docker hub, put its repository in a Helm chart and deploy it in a Kubernetes environment. Some of the decisions made throughout this process have been described in the comparison PDF file in the `results` directory.  

5. Build a continuous integration process (CI) for your project.

I have implemented Checkout stage which downloads the repository from github through SSH since it is a private repo for now and created tests whether the result temperature in celsius is equal to what it is supposed to be. The pipeline file can be found in the `Jenkins` directory.

![pipeline](./images/Pipeline.png)

The test stage is failed on purpose. The pytest consists of four tests:

- integer equality web version
- integer equality TensorFlow version
- float equality web version
- float equality TensorFlow version

Since float is approximated differently in both scenarios, both of these fail:

![pipeline fail](./images/Pipeline%20fail.png)

6. Use TensorFlow Serving to serve a computational graph converting Fahrenheit temperature to Celsius.

I have created an additional method that is being used on another endpoint which involves TensorFlow Serving model. Docker image has been pushed to DockerHub again so that a helm chart can be created to deploy the application. Now the Locust tests will be happening on two __post__ http methods which include both normal and model temperature conversions. I have also encountered a problem with Helm not seeing the latest update on the DockerHub so I changed the __pullPolicy__ from `IfNotPresent` to `Always`.

7. Get the statistics files in csv format and attach them to the repo under the folder named results.

- ✅ Present in `results`.

8. Compare the performance of the web app solution to the tensorflow solution.

- ✅ Present in `results`.


