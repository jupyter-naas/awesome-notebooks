# Elasticsearch connector

### 1. Pre-requisite:
- Python3
- Ubuntu 18.04
- Java1.8

### 2. Elasticsearch server on local machine

#### Install Linux packages
```sh
$ sudo apt update
$ sudo apt-get install apt-transport-http
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo add-apt-repository "deb https://artifacts.elastic.co/packages/7.x/apt stable main"
$ sudo apt update
$ sudo apt install elasticsearch 
```

#### Check status of Elasticsearch server (Local)
```sh
$ sudo /etc/init.d/elasticsearch status
```
#### Start Elasticsearch server (Local)
```sh
$ sudo /etc/init.d/elasticsearch start
```

##### Note : Install Java 1.8 and set Java environment variables path
&nbsp;
### 3. Elasticsearch on cloud
&nbsp;
#### Step 1: Login to https://www.elastic.co/ and create a deployment
#### Step 2: On successful deployment get credentials
#### Step 3: Create Elasticsearch credentials JSON
&nbsp;
#### Credentials Json format
```sh
{
	"endpoint": "< Elasticsearch endpoint from elasticsearch cloud >",
	"port": "< Port number as mentioned in elasticsearch cloud >",
	"user": "< User as mentioned in elasticsearch cloud >",
	"password": "< Elasticsearch cloud user password >",
	"protocol": "https"
}
```