# neo4j-demo

## install


### Docker

```sh
$ sudo docker run \
    -d \
    --name neo4j \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=/home/xxxx/volume/neo4j/data:/data \
    neo4j
```

### kubernetes

```sh
$ helm install \
  stable/neo4j  \
  --name test \
  --set acceptLicenseAgreement=yes  \
  --set neo4jPassword=mypassword
```