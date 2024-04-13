import json
from django.http import HttpResponse
def test(request):
    # result = {"status":"错误正确","data":"正确","city":"北京"}
    # #json返回为中文
    # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    # if request.method == 'GET' and 'question' in request.GET:
    #     question = request.GET['question']
    #     print(question)
    #     data = {"answer": "answer"}
        # ensure_ascii=False用于处理中文
    data = {
            "code": 'code',
            "msg": "成功",
            "data": 'data',
        }
    #return HttpResponse(json.dumps(data, ensure_ascii=False))
    return HttpResponse(json.dumps(data,ensure_ascii=False), content_type="application/json;charset=utf-8")


def index(request):
    # 查询出Person对象信息，也就是数据表中的所有数据
    # 一行数据就是一个对象，一个格子的数据就是一个对象的一个属性值
    objs = CustomUser.objects.all()

    # locals函数可以将该函数中出现过的所有变量传入到展示页面中，即index.html文件中
    return render(request, 'index.html', locals())

# def response_as_json(data, foreign_penetrate=False):
#     jsonString = serializer(data=data, output_type="json", foreign=foreign_penetrate)
#     response = HttpResponse(
#             # json.dumps(dataa, cls=MyEncoder),
#             jsonString,
#             content_type="application/json",
#     )
#     response["Access-Control-Allow-Origin"] = "*"
#     return response
# def json_response(data, code=200, foreign_penetrate=False, **kwargs):
#     data = {
#         "code": code,
#         "msg": "成功",
#         "data": data,
#     }
#     return response_as_json(data, foreign_penetrate=foreign_penetrate)
