from flask import Flask, jsonify, request
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

INF = int(1e9)
app = Flask(__name__)
# 보너스 과제2
# DB 연동
# 최초 실행 시 데이터에 접근
engine = create_engine("sqlite:///cafe.db?check_same_thread=False")

# ORM 선언
db = declarative_base()
db.metadata.create_all(engine)

# 매핑 클래스 선언
# ORM의 사용은 객체를 릴레이션에 매핑
# 따라서 다음과 같이 클래스로 db테이블에 매핑
class Cafe_menus(db):
    # cafe_menus에 해당하는 테이블에 매핑
    __tablename__ = 'cafe_menus'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    price = Column(String(32))

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    # 출력형식 정의
    def __repr__(self):
        return f"<menu {self.id}>, <{self.name}>, <{self.price}>"

# 세션 생성
# engine과 연동된 데이터베이스를 다룸
# DB와 Session을 통해 대화한다고 생각하면 됨
Session = sessionmaker(bind=engine)
session = Session()


# db 불러오기
# SELECT * FROM Cafe_menus
table = session.query(Cafe_menus.id, Cafe_menus.name, Cafe_menus.price).all()

# 불러온 db출력
print(table)
# 메뉴 추가시 id의 값은 최종 데이터의 id값에 +1 된 값으로 id저장
curr_menus = table[-1][0] if table else 1


# db에서 데이터를 불러와서 table에 값을 저장
# 메뉴를 담을 리스트
menus = []
for elements in table:
    # db에서 한 행씩 읽고, 각 요소들을 row의 원소로 저장
    row = {}
    row['id'], row['name'], row['price'] = elements
    # 메뉴에 추가
    menus.append(row)


@app.route('/')
def hello_flask():
    return "Hello World!"


# GET /menus | 자료를 가져온다.
@app.route('/menus')
def get_menus():
    return jsonify({'menus': menus})


# curr_menus를 전역변수로 설정, 메뉴가 추가될 때마다 메뉴중복 검사
# 메뉴가 추가될 때마다 id가 1씩 추가되어 값이 저장
# POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu():
    global curr_menus
    # 전달받은 자료를 menus자원에 추가
    # json형태로 받은 데이터를 파싱한 후 request_data에 저장
    request_data = request.get_json()  # {'name': ..., 'price': ...}

    # 입력받은 메뉴가 기존에 있던 메뉴라면
    # "Already exists" 반환
    for menu in menus:
        if menu['name'] == request_data['name']:
            return "Already Exists"

    # 입력받은 메뉴가 기존에 있지 않은 신규메뉴라면
    # 기존에 저장되어 있던 id = id + 1 하여 메뉴에 저장
    curr_menus += 1
    new_menu = {'id': curr_menus, 'name': request_data['name'], 'price': request_data['price']}
    menus.append(new_menu)

    # 추가된 메뉴를 db에 저장
    # 클라이언트로부터 요청된 데이터들을 매핑 클래스에 값을 할당
    add_menu = Cafe_menus(curr_menus, request_data['name'], request_data['price'])
    # db에 추가
    # INSERT INTO Cafe_menus(id, name, price) VALUES (curr_menus, request_data['name'], request_data['price'])
    # COMMIT
    session.add(add_menu)
    session.commit()

    # 추가한 메뉴를 반환
    return jsonify(new_menu)


# PUT /menus/<int:id> | 기존에 있는 자료를 수정(해당하는 id의 메뉴를 수정)
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    # 전달받은 자료를 menus에 있는 자원수정
    request_data = request.get_json()  # {'name': ..., 'price': ...}
    # 최초 인덱스 변수는 가장 마지막 메뉴의 아이디 + 1
    # 입력 받은 id가 메뉴에 없을 경우 "Invalid Id"반환
    idx = INF
    for i, menu in enumerate(menus):
        if menu['id'] == id:
            idx = i
            break
    # 메뉴수정(해당하는 아이디가 Invalid Id반환)
    try:
        menus[idx]['name'], menus[idx]['price'] = request_data['name'], request_data['price']
        # db에 id가 클라이언트로 입력받은 id와 같은 메뉴를 수정
        # UPDATE Cafe_menus SET name = request_data['name'], price = request_data['price] WHERE id = idx
        session.query(Cafe_menus).filter(Cafe_menus.id == id).update({'name': request_data['name'],\
                                                                      'price': request_data['price']})
        session.commit()
    except:
        return "Invalid Id"
    else:
        # 수정한 메뉴 반환
        return jsonify(menus[idx])


# DELETE / menus/<int:id> | 해당하는 ID의 데이터 삭제
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    # 최초 인덱스는 매우 큰 값으로 설정
    # 해당하는 id가 없을 때 "Invalid ID"반환
    idx = INF
    for i in range(len(menus)):
        if menus[i]['id'] == id:
            idx = i
            break
    # 메뉴삭제
    try:
        menus.remove(menus[idx])
        # db에서 데이터 삭제
        d_m = session.query(Cafe_menus).filter(Cafe_menus.id == idx).first()
        # DELETE FROM Cafe_menus WHERE id = idx
        session.delete(d_m)
        session.commit()
    except:
        return "Invalid Id"
    else:
        # 메뉴 반환
        return jsonify({'menus': menus})


# 함수를 직접적으로 실행했을 때 app을 실행해라
if __name__ == '__main__':
    app.run()