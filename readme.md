1. activate virtualenv(runenv.sh), deactivate
2. python manage.py [Command]
  runserver, makemigrations, migrate, 
3. (DB 반영시) makemigrations -> migrate
4. migrate는 실제 DB에 반영하는 명령어이고 이 명령어는 마이그레이션 스크립트를 실행하는데 makemigrations 명령어로 마이그레이션 스크립트를 만듭니다. 번거롭게 데이터베이스 테이블을 우리가 변경하지 않아도 되니 참 편합니다.
5. 이용자가 URL로 접근하여 뭔가를 요청하면 그 URL에 대한 정보를 urls.py로 대표되는 URL dispatch에서 찾아서 연결된 구현부를 실행합니다.
6. 이렇게 URL과 구현부을 연결해주는 역할을 Django의 View 영역인 views.py가 합니다
7. $projectname/urls.py 에 연결할 url 입력
8. django Ver 2.0 으로 오면서 urls -> path를 사용함으로써 정규식을 사용하지 않아도 되게 되었다.
9. from django.shortcuts import get_object_or_404 를 사용하면 404 에러를 일으키고 오류페이지로 안내 가능
10. Pkg/setting.py에서 MEDIA_URL, MEDIA_ROOT를 설정해줌으로써 업로드 파일에 쉽게 접근, 관리 할 수 있음

