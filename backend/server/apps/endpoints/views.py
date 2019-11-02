from rest_framework import viewsets
from rest_framework import mixins

from apps.endpoints.models import Endpoint
from apps.endpoints.serializers import EndpointSerializer

from apps.endpoints.models import MLAlgorithm
from apps.endpoints.serializers import MLAlgorithmSerializer

from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.serializers import MLAlgorithmStatusSerializer

from apps.endpoints.models import MLRequest
from apps.endpoints.serializers import MLRequestSerializer

import json
from rest_framework import views, status
from rest_framework.response import Response
from apps.ml.registry import MLRegistry
from server.wsgi import registry

class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()


class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()

class MLAlgorithmStatusViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin, mixins.UpdateModelMixin
):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MLAlgorithmStatus.objects.all()

class MLRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()


class PredictView(views.APIView):
    def post(self, request, endpoint_name, format=None):

        # get status and version from url
        algorithm_status = self.request.query_params.get("status", "production")
        algorithm_version = self.request.query_params.get("version")
        # get ML algorithm status from database
        statuses = MLAlgorithmStatus.objects.filter(parent_endpoint__name = endpoint_name, status = algorithm_status)
        if algorithm_version is not None:
            statuses = statuses.filter(parent_mlalgorithm__version = algorithm_version)
        # there is no ML algorithm with such status and version
        if len(statuses) == 0:
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # there are more than 1 ML algorithm with specified status and version
        if len(statuses) != 1:
            return Response(
                {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # get the ML algorithm
        algorithm_object = registry.endpoints[statuses[0].parent_mlalgorithm.id]
        # compute the prediction
        prediction = algorithm_object.compute_prediction(request.data)
        # save the request and prediction outcome
        ml_request = MLRequest(
            input_data=json.dumps(request.data),
            response=prediction,
            feedback="",
            parent_mlalgorithm=statuses[0].parent_mlalgorithm,
        )
        ml_request.save()

        prediction["request_id"] = ml_request.id

        return Response(prediction)
