# Snyk Boot Web Demo - Pas DOTC Events

![alt tag](https://i.ibb.co/7tnp1B6/snyk-logo.png)

## Steps to create the container image

- Ensure you have JDK 17 installed as follows

```shell
$ java -version
openjdk version "17.0.13" 2024-10-15
OpenJDK Runtime Environment (build 17.0.13+11)
OpenJDK 64-Bit Server VM (build 17.0.13+11, mixed mode, sharing)
```

- Build the artifact image as follows

```shell
$ mvn package
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------< com.example:snyk-boot-web >----------------------
[INFO] Building snyk-boot-web 0.0.1-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
....

[INFO]
[INFO] --- maven-jar-plugin:3.2.0:jar (default-jar) @ snyk-boot-web ---
[INFO] Building jar: /Users/pasapicella/snyk/demos/languages-code-demos/java/snyk-boot-web/target/snyk-boot-web-0.0.1-SNAPSHOT.jar
[INFO]
[INFO] --- spring-boot-maven-plugin:2.3.10.RELEASE:repackage (repackage) @ snyk-boot-web ---
[INFO] Replacing main artifact with repackaged archive
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  5.595 s
[INFO] Finished at: 2024-02-14T11:03:49+11:00
[INFO] ------------------------------------------------------------------------
```

- Make sure Springboot JAR file was created at "**target/snyk-boot-web-0.0.1-SNAPSHOT.jar**"

- Create a container image as follows here I am using Dockerhub and you would need Docker desktop running to perform these steps

```shell
$ docker build --tag=snyk-boot-web:latest .
$ docker tag snyk-boot-web:latest {userID}/snyk-boot-web:latest
$ docker push {USERID}/snyk-boot-web:latest
```
## Run on Kubernetes

- The following Kubernetes config file exists in the ./kubernetes folder you can use that as a starting guide. 

_Note: No service is exposed so you can't access the application without a Service or using port forward to allow access. The Kubernetes integration does not need the application exposed_ 

```yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: snyk-boot-web
  namespace: apples
spec:
  selector:
    matchLabels:
      app: snyk-boot-web
  replicas: 1
  template:
    metadata:
      labels:
        app: snyk-boot-web
    spec:
      containers:
        - name: snyk-boot-web
          image: pasapples/snyk-boot-web:v1
          imagePullPolicy: Always
          ports:
            - containerPort: 5000
```

<hr />
Pas Apicella [pas at snyk.io] is a Principal Solution Engineer at Snyk APJ 