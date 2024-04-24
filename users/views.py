from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from .models import *


@csrf_exempt
def user_login(request):
    global input_email
    if request.method == 'GET':
        # 设置字符编码为 UTF-8
        request.encoding = 'utf-8'

        input_email = request.GET.get('email')
        input_password = request.GET.get('password')

    # # 使用 authenticate 函数来验证用户
    # user = authenticate(request, email=email, password=password)

    user = CustomUser.objects.get(email=input_email)
    email = user.email
    password = user.password

    if email == input_email and password == input_password:
        # 用户认证成功，可以进行其他操作，比如返回成功信息
        return JsonResponse({'status': 'success', 'message': 'Authentication successful'})
    else:
        # 用户认证失败，返回错误信息
        return JsonResponse({'status': 'error', 'message': 'Authentication failed'}, {'custom_users': user})


@csrf_exempt
def user_register(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        password = request.GET.get('password')

        # 检查 email 和 password 是否有效
        if not email or not password:
            return JsonResponse({'error': 'Email and both passwords are required.'}, status=400)

        # 创建用户
        try:
            CustomUser.objects.create_user(email=email, password=password)
            return JsonResponse({'message': 'User created successfully.'})
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)


def get_stkstatus(request):
    data = serialize('json', stkStatus.objects.all(), fields=(
    'createtime', 'x_current', 'y_current', 'z_current', 'x_speed', 'y_speed', 'z_speed', 'pos_x', 'pos_y', 'pos_z'))
    return JsonResponse(data, safe=False)


def database(request):
    # 查询出对象信息，也就是数据表中的所有数据
    # 一行数据就是一个对象，一个格子的数据就是一个对象的一个属性值
    custom_users = CustomUser.objects.all()

    return render(request, 'test.html', {'custom_users': custom_users})
