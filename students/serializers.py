from .models import Students,Teacher,Marks,Subjects
from rest_framework import serializers



class StudentsSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    gender_name = serializers.SerializerMethodField()


    class Meta:
        model = Students
        fields = ( 'id','student_first_name','student_last_name', 'age', 'gender','reporting_teacher','teacher','gender_name')
    
    def get_teacher(self,obj):
    	if obj.reporting_teacher:
    		return obj.reporting_teacher.staff_first_name +" "+obj.reporting_teacher.staff_last_name
    	else:
    		return None
        
    def get_gender_name(self,obj):
    	if obj.gender:
    		return obj.get_gender_display()
    	else:
    		return None



class MarksSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Marks
        fields = ( 'id','student_name','student','subject', 'term','mark','total','subject_name')
    
    def get_total(self,obj):
    	if obj.mark:

    		return obj.mark
    	else:
    		return None
        
    def get_student_name(self,obj):
    	if obj.student:
    		return obj.student.student_first_name+" "+student_last_name
    	else:
    		return None
    def get_subject_name(self,obj):
    	if obj.subject:
    		return obj.subject.subject_name
    	else:
    		return None
