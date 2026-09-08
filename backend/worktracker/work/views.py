from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Task, Dependency
from .serializers import TaskSerializer, DependencySerializer


# ------------------ SEED DATA ------------------
def seed_data():
    if User.objects.exists():
        return

    admin = User.objects.create(
        name="Admin",
        email="admin@test.com",
        password="1234",
        role="admin"
    )

    member = User.objects.create(
        name="Member",
        email="member@test.com",
        password="1234",
        role="member"
    )

    Task.objects.create(
        title="Task A",
        description="First task",
        assigned_to=admin,
        progress=100,
        status="done"
    )

    Task.objects.create(
        title="Task B",
        description="Second task",
        assigned_to=member,
        progress=0,
        status="blocked"
    )


# ------------------ AUTH ------------------
@api_view(['POST'])
def register(request):
    data = request.data

    if User.objects.filter(email=data.get('email')).exists():
        return Response({"error": "User already exists"})

    user = User.objects.create(
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password'),
        role=data.get('role')
    )

    return Response({"msg": "User created"})


@api_view(['POST'])
def login(request):
    data = request.data
    user = User.objects.filter(email=data.get('email')).first()

    if not user:
        return Response({"error": "User not found"})

    if user.password != data.get('password'):
        return Response({"error": "Wrong password"})

    return Response({
        "id": user.id,
        "role": user.role
    })


# ------------------ TASKS ------------------
@api_view(['GET'])
def get_tasks(request):
    seed_data()  # Auto-create demo data

    tasks = Task.objects.all()
    return Response(TaskSerializer(tasks, many=True).data)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['PUT'])
def update_task(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"})

    serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        update_dependencies(task.id)
        return Response(serializer.data)

    return Response(serializer.errors)


# ------------------ DEPENDENCY LOGIC ------------------
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


# ------------------ CYCLE DETECTION ------------------
def has_cycle(start, target, graph, visited=None):
    if visited is None:
        visited = set()

    if start == target:
        return True

    if start in visited:
        return False

    visited.add(start)

    for neighbor in graph.get(start, []):
        if has_cycle(neighbor, target, graph, visited):
            return True

    return False


# ------------------ CREATE DEPENDENCY ------------------
@api_view(['POST'])
def create_dependency(request):
    data = request.data

    if data.get('threshold', 0) <= 0:
        return Response({"error": "Threshold must be > 0"})

    deps = Dependency.objects.all()
    graph = {}

    for d in deps:
        graph.setdefault(d.predecessor_id, []).append(d.successor_id)

    if has_cycle(data.get('successor'), data.get('predecessor'), graph):
        return Response({"error": "Cycle detected"})

    serializer = DependencySerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
