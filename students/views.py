from django.shortcuts import render
from rest_framework import viewsets, status, filters, serializers
from .models import Students,Teacher,Marks,Subjects
from django.db.models import Sum
from .serializers import StudentsSerializer,MarksSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()

    def get_queryset(self):
        queryset = Students.objects.all()
        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response_data = {
            "status_code": "200",
            "status": True,
            "message": 'Students List',
            "data": data
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        response_data = {}
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            response = self.perform_update(serializer)
            
        except Exception as e:
          
            response_data['status_code'] = '400'
            response_data['status'] = True
            response_data['message'] = 'Error in updating students'
        else:
            response_data['status_code'] = '200'
            response_data['status'] = True
            response_data['message'] = 'You have succesfully updated students details'
        if response_data['status_code'] == '400':
            resp_status = status.HTTP_400_BAD_REQUEST
        elif response_data['status_code'] == '200':
            resp_status = status.HTTP_200_OK
        return Response(response_data, status=resp_status)

    def create(self, request, *args, **kwargs):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            response = super().create(request)
            response_data['status_code'] = '201'
            response_data['status'] = True
            response_data['message'] = 'Student added successfully'

        except Exception as e:
            print(e)
            response_data['status_code'] = '400'
            response_data['status'] = False
            response_data['message'] = 'Unable to add student'

        if response_data['status_code'] == '400':
            resp_status = status.HTTP_400_BAD_REQUEST
        elif response_data['status_code'] == '201':
            resp_status = status.HTTP_201_CREATED

        return Response(response_data, status=resp_status)


    def destroy(self, request, pk=None):
        response_data = {}
        record_to_delete = Students.objects.filter(id=pk).first()

        if record_to_delete:
            record_to_delete.is_deleted = True
            record_to_delete.save()
            
            response_data['status_code'] = '200'
            response_data['status'] = True
            response_data['message'] = 'Student record deleted successfully'

        else:
            response_data['status_code'] = '400'
            response_data['status'] = False
            response_data['message'] = 'Student record not found'

        if response_data['status_code'] == '200':
            resp_status = status.HTTP_200_OK
        elif response_data['status_code'] == '400':
            resp_status = status.HTTP_400_BAD_REQUEST

        return Response(response_data, status=resp_status)


class MarksViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    
    serializer_class = MarksSerializer
    queryset = Marks.objects.all()



    def get_queryset(self):
        queryset = Marks.objects.all()
        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # serializer = self.get_serializer(queryset, many=True)
        # data = serializer.data
        result = []
        result_data={}
        student_obj = Students.objects.all()

        for student_data in student_obj:
            print("student_data ",student_data)
            queryset =Marks.objects.filter(student__id=student_data.id).aggregate(Sum('mark'))
            print("queryset",queryset)
            result_data['id'] = student_data.id
            result_data['name']=student_data.student_first_name+" "+student_data.student_last_name
            result_data['total'] = queryset['mark__sum']

            marks_res = Marks.objects.filter(student__id=student_data.id)
            for marks_result in marks_res:

                result_data['subject']=marks_result.subject.subject_name
                result_data['mark'] = marks_result.mark
                result_data['term'] = marks_result.term

                result.append(result_data)
                result_data={}
                print("result_data",result)
            


            
        print("result_data",result_data)


        print("final....",result,"student ",student_data)
        

        response_data = {
            "status_code": "200",
            "status": True,
            "message": 'Mark List',
            "data": result
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        response_data = {}
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            response = self.perform_update(serializer)
            
        except Exception as e:
          
            response_data['status_code'] = '400'
            response_data['status'] = True
            response_data['message'] = 'Error in updating marks'
        else:
            response_data['status_code'] = '200'
            response_data['status'] = True
            response_data['message'] = 'You have succesfully updated marks'
        if response_data['status_code'] == '400':
            resp_status = status.HTTP_400_BAD_REQUEST
        elif response_data['status_code'] == '200':
            resp_status = status.HTTP_200_OK
        return Response(response_data, status=resp_status)    




    def create(self, request, *args, **kwargs):
        response_data = {}
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            response = super().create(request)
            response_data['status_code'] = '201'
            response_data['status'] = True
            response_data['message'] = 'Student mark added successfully'

        except Exception as e:
            print(e)
            response_data['status_code'] = '400'
            response_data['status'] = False
            response_data['message'] = 'Unable to add marks'

        if response_data['status_code'] == '400':
            resp_status = status.HTTP_400_BAD_REQUEST
        elif response_data['status_code'] == '201':
            resp_status = status.HTTP_201_CREATED

        return Response(response_data, status=resp_status)

    def destroy(self, request, pk=None):
        response_data = {}
        record_to_delete = Marks.objects.filter(id=pk).first()

        if record_to_delete:
            record_to_delete.is_deleted = True
            record_to_delete.save()
            
            response_data['status_code'] = '200'
            response_data['status'] = True
            response_data['message'] = 'Record deleted successfully'

        else:
            response_data['status_code'] = '400'
            response_data['status'] = False
            response_data['message'] = 'Record not found'

        if response_data['status_code'] == '200':
            resp_status = status.HTTP_200_OK
        elif response_data['status_code'] == '400':
            resp_status = status.HTTP_400_BAD_REQUEST

        return Response(response_data, status=resp_status)



