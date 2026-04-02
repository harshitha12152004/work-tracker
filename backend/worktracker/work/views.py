from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task,Dependency
from .serializers import TaskSerializer
'''
# CREATE TASK
@rest_framework.decorators.work_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''

# GET TASKS
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    return Response(TaskSerializer(tasks, many=True).data)

# CREATE TASK
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



#UPDATE TASK
'''
@rest_framework.decorators.work_view(['PUT'])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        update_dependencies(task.id)

    return Response(serializer.data)


# DEPENDENCY LOGIC
def update_dependencies(task_id):
    deps = Dependency.objects.filter(predecessor_id=task_id)

    for dep in deps:
        successor = dep.successor
        pred = dep.predecessor

        blocked = False

        if dep.type == "full" and pred.progress < 100:
            blocked = True
        if dep.type == "partial" and pred.progress < dep.threshold:
            blocked = True

        successor.status = "blocked" if blocked else "in-progress"
        successor.save()


# CREATE DEPENDENCY
@rest_framework.decorators.work_view(['POST'])
def create_dependency(request):
    serializer = DependencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''