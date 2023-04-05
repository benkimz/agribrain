# AgriBrain 
---
Small-scale farmers face challenges in accessing quality information and markets for their produce, resulting in low productivity, poor yields, and limited income. Additionally, food insecurity is a prevalent issue in many regions around the world. The AgriBrain project aims to address these challenges by providing farmers with an AI-powered search portal that offers weather forecasting models and quality advice on farming practices, bringing farmers together in clusters to access a common market for their produce, and providing a charity program to help solve the hunger crisis.

### Running the application
---

#### Set up docker:
---
```console
$sudo apt-get update
$sudo apt-get install docker.io
$sudo systemctl start docker
```

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
> Start the application:

```console
$docker-compose up
```

# IMPLEMENTATION:
---
The architecture of the AgriBrain project is a microservices-based architecture, with the backend responsible for server-side logic and data storage, the frontend responsible for client-side logic and user interface, and machine learning components used for training and deploying AI models. The project uses Docker for containerization, Google Cloud Platform for hosting and deployment, and Google Earth Engine for visualizing and querying data. The development tools used include Git and Hugging Face.

* Backend: Responsible for handling server-side logic and data storage. This includes implementing the AI models, accessing and storing data, and communicating with the frontend. The backend was developed using Python and SQLite.

* Frontend: Responsible for handling client-side logic and user interface. This includes visualizing data, displaying information, and handling user input. The frontend was developed using Streamlit, HTML 5, JavaScript, and CSS.

* Technologies: Used to facilitate the development and deployment of the application. This includes Docker for containerization, Google Cloud Platform for hosting and deployment, and Google Earth Engine for visualizing and querying data.

* Machine Learning Components: Responsible for training and deploying the AI models used in the project. This includes TensorFlow/Keras API, transformers, and GPT-2.

* Development Tools: Used to facilitate development and collaboration among team members. This includes Git and Hugging Face.