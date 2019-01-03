from django.shortcuts import render
from hello.models import Hello

# Create your views here.

# Get hello/
def hello(request):
    # ORM = Object Relastion Mapping
    # 파이썬 코드를 sql로 mapping 해줌
    # SELECT * FROM hello_hello
    post = Hello.objects.all()
    
    context = {
        'post': post
    }
    return render(request, 'hello/index.html', context=context)
