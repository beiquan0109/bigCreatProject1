from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 检查 email 和 password 是否有效
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required.'}, status=400)

        # 验证用户
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful.'})
        else:
            return JsonResponse({'error': 'Invalid email or password.'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # 检查 email 和 password 是否有效
        if not email or not password or not password1:
            return JsonResponse({'error': 'Email and both passwords are required.'}, status=400)

        # 检查两次密码输入是否一致
        if password != password1:
            return JsonResponse({'error': 'Passwords do not match.'}, status=400)

        # 创建用户
        try:
            CustomUser.objects.create_user(email=email, password=password)
            return JsonResponse({'message': 'User created successfully.'})
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


def database(request):
    # 查询出对象信息，也就是数据表中的所有数据
    # 一行数据就是一个对象，一个格子的数据就是一个对象的一个属性值
    custom_users = CustomUser.objects.all()

    return render(request, 'test.html', {'custom_users': custom_users})
