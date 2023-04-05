# AgriBrain 
---
Small-scale farmers face challenges in accessing quality information and markets for their produce, resulting in low productivity, poor yields, and limited income. Additionally, food insecurity is a prevalent issue in many regions around the world. The AgriBrain project aims to address these challenges by providing farmers with an AI-powered search portal that offers weather forecasting models and quality advice on farming practices, bringing farmers together in clusters to access a common market for their produce, and providing a charity program to help solve the hunger crisis.

### Running the application
---

#### Beta dep:
---
```console
$docker run -p 80:80 benkimz/agribrain:beta
```

#### Alpha dep:
---
> start by cloning the repository:

```console
$git clone https://github.com/benkimz/agribrain.git
```
> Navigate to the directory ```agribrain``` and then to ```alpha-dep```

```console
$cd ./agribrain/alpha-dep/
```
#### Set up docker:
---
```console
$sudo apt-get update
$sudo apt-get install docker.io
$sudo systemctl start docker
```

> Start the application:

```console
$docker-compose up
```
