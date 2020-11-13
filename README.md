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

## ML Community :rocket:

Currently, I'm working on an Automated Machine Learning Python Package, called: [mljar-supervised](https://github.com/mljar/mljar-supervised). I've created a [slack channel](https://mljar-supervised.slack.com/join/shared_invite/zt-gkhfsvhw-H6LMKxxV5adeTmn9V7nbZw#/) for ML disscussions (not only about AutoML), feel free to join conversations and ask questions! :+1:

## Django + React Tutorial :books:

I'm working on complete tutorial how to build SaaS (software as a Service) application with Django and React from scratch. The tutorial is available at [SaaSitive](https://saasitive.com) website: https://saasitive.com/django-react/boilerplate/
