from django.shortcuts import render

# Create your views here.


def show_ari(request):
    context = {
        'group_name': 'kda',
        'name': 'ari',
        'img_src':"https://media.bunjang.co.kr/product/200514473_1_1675936339_w%7Bres%7D.jpg"
    }
    return render(request, 'kda/멤버.html',context=context)
  #  return render(request, 'kda/ari.html')

def show_akali(request):
    context = {
        'group_name': 'kda',
        'name': 'akali',
        'img_src': "https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt9e3ffdcedbc7bb90/5f4041c113ba7e23cc5b6754/AkaliTeaserImage_16_9.jpg?quality=90&crop=1%3A1&width=600"
    }
    return render(request, 'kda/멤버.html',context=context)
  #  return render(request, 'kda/akali.html')