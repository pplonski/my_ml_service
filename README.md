# Deploy Machine Learning Models with Django

This is source code from tutorial available at [deploymachinelearning.com](https://deploymachinelearning.com)

In the `research` directory there are:

- [code for training machine learning models on exmaple dataset](https://github.com/pplonski/my_ml_service/blob/master/research/train_income_classifier.ipynb)
- [code for simulating A/B test](https://github.com/pplonski/my_ml_service/blob/master/research/ab_test.ipynb)

In the `backend` directory there is Django application that:

- can handle several ML algorithms and make the available as web service with user defined REST API endpoints,
- store information about requests which are send to the ML models,
- allow to run A/B tests between algorithms.

In the `docker` directory there are dockerfiles for running the service in the container.

