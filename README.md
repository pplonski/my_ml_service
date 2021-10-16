# Deploy Machine Learning Models with Django

This is a source code from the tutorial available at [deploymachinelearning.com](https://deploymachinelearning.com)

This web service makes Machine Learning models available with REST API. It is different from most of the tutorials available on the internet:

- it keeps information about many ML models in the web service. There can be several ML models available at the same endpoint with different versions. What is more, there can be many endpoint addresses defined.
- it stores information about requests sent to the ML models, this can be used later for model testing and audit.
- it has tests for ML code and server code,
- it can run A/B tests between different versions of ML models.

## The code structure

In the `research` directory there are:

- code for training machine learning models on Adult-Income dataset [link](https://github.com/pplonski/my_ml_service/blob/master/research/train_income_classifier.ipynb)
- code for simulating A/B tests [link](https://github.com/pplonski/my_ml_service/blob/master/research/ab_test.ipynb)

In the `backend` directory there is Django application.

In the `docker` directory there are dockerfiles for running the service in the container.

## Getting Started

```
$ conda create -n pplonski_ml_service "python==3.7.10"
$ conda activate pplonski_ml_service
$ pip install -r requirements.txt
$ docker-compose down
$ docker-compose build
$ docker-compose up
```

Then visit [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)

## Django + Svelte

John is working on a [django backend for svelte](gitlab.com/tangibleai/proai_playground_backend) 

## Attribution

The original author of the  `my_ml_service` project is `pplonski` [on GitHub](https://github.com/pplonski). 

He's working on a "tutorial how to build SaaS (software as a Service) application with Django and React from scratch. The tutorial is available at [SaaSitive.com](https://saasitive.com) website: [saasitive.com/django-react/boilerplate](https://saasitive.com/django-react/boilerplate/)."
