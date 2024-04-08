#helloidol
***
1. startproject helloidol
   1. python -m pip install django~=4.2
   2. django-admin startproject _helloidol_ .
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_
   1. Terminal 
      1. python manage.py startapp _playground_
   2. helloidol/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달 : urls -> (models -> ) templates
   - 코드 작성 : (models -> ) views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4.  -> templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ ->_say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html_/ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
---
5. startapp _kda_
   1. Terminal
      1. python manage.py startapp kda
   2. helloidol/settings.py
      1. 'kda', in INSTALLED_APPS
6. kda/
   1. views
      1. ~~show_ari()~~
      2. ~~show_akali()~~
      3. -> templates에 context전달
      4. 정보를 하나로 묶고, 거기에서 꺼내오자
      5. show_멤버()
      6. image link -> image file(static)
      7. show_멤버리스트()
   2. templates/kda/
      1. ~~ari.html~~
         1. title: kda - ari
         2. h1: kda
         3. h2: ari
         4. img: ari 프로필 사진
            1. border-radius: 50%
      2. ~~akali.html~~
      3. 멤버.html
         1. group_name, name, img_src
         2. `{% load static %} <img src="{%static img_src%}">`
         3. ```
            {% extends 'base.html' %}
            {% block title %}{% endblock %}
            {% block content %}{% endblock %}
            ```
      4. 멤버리스트.html
         1. {% url '앱이름:path이름' %}
         2. {% url '앱이름:path이름' 변수=값 %}
         3. ```
            {% extends 'base.html' %}
            {% block title %}{% endblock %}
            {% block content %}{% endblock %}
            ```
   3. urls
      1. ~~kda/ -> ari/ -> show_ari()~~
      2. ~~kda/ -> akali/ -> show_akali()~~
      3. kda/ -> <멤버>/ -> show_멤버(멤버)
      4. kda/ -> 멤버리스트/ -> show_멤버리스트()
   4. static/kda/images/
      1. akali.jpg, ari.jpg, kaisa.jpg
7. template/
   1. base.html
      ``` 
      {% block title %}{% endblock %}
      {% block css %}{% endblock %}
      {% block content %}{%endblock %}
      ```
8. hellodiol/
   1. in TEMPLATES in settings.py
      1. 'DIRS':[BASE_DIR / 'templates'],
         
