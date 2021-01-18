from django.shortcuts import render
from django.http.response import JsonResponse

from firstApi.models import PytorchModel
from firstApi.serializers import PytorchModelSerializer

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
# pk = primary key = id

@api_view(['GET', 'POST', 'DELETE'])
def pytorchModel_list(request):
    if request.method == 'GET':
        req_id = request.GET.get('id', None)
        if req_id is not None:
            try:
                db_row = PytorchModel.objects.get(pk=req_id)
                serialized_row = PytorchModelSerializer(db_row)
                return JsonResponse(serialized_row.data)
            except PytorchModel.DoesNotExist:
                return JsonResponse({'message': 'The Model does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            db_row = PytorchModel.objects.all()
            serialized_row = PytorchModelSerializer(db_row,many=True)
            return JsonResponse(serialized_row.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        instance = PytorchModelSerializer(data=data)
        if instance.is_valid():
            instance.save()
            return JsonResponse(instance.data, status=status.HTTP_201_CREATED)
        return JsonResponse(instance.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        req_id = request.GET.get('id', None)
        if req_id is not None:
            try:
                db_row = PytorchModel.objects.get(pk=req_id)
                db_row.delete()
                return JsonResponse({'message': 'Model deleted successfully'}, status=status.HTTP_200_OK)
            except PytorchModel.DoesNotExist:
                return JsonResponse({'message': 'The Model does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            req_name = request.GET.get('name', None)
            if req_name is not None:
                try:
                    db_row = PytorchModel.objects.get(name=req_name)
                    db_row.delete()
                    return JsonResponse({'message': 'Model with name {} deleted successfully'.format(req_name)}, status=status.HTTP_200_OK)
                except PytorchModel.DoesNotExist:
                    return JsonResponse({'message': 'The Model does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def runModel(request):
    ## Dummy code
    req_id = request.GET.get('id', None)
    if req_id is not None:
        try:
            db_row = PytorchModel.objects.get(pk=req_id)
            db_ser = PytorchModelSerializer(db_row)
            return JsonResponse(db_ser.data)
        except PytorchModel.DoesNotExist:
            return JsonResponse({'message': 'The Model does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        req_name = request.GET.get('name', None)
        if req_name is not None:
            try:
                db_row = PytorchModel.objects.get(name=req_name)
                db_row.delete()
                return JsonResponse({'message': 'Model with name {} deleted successfully'.format(req_name)}, status=status.HTTP_200_OK)
            except PytorchModel.DoesNotExist:
                return JsonResponse({'message': 'The Model does not exist'}, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(instance.errors, status=status.HTTP_400_BAD_REQUEST)
