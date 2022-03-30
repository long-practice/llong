from flask import Flask, jsonify, request

app = Flask(__name__)
INF = int(1e9)
menus = [
    {'id': 1, 'name': 'Espresso', 'price': 3800},
    {'id': 2, 'name': 'Americano', 'price': 4100},
    {'id': 3, 'name': 'Cafe Latte', 'price': 4600},
]

# '/'주소를 요청받았을 때 밑의 함수를 실행해라
@app.route('/')
def hello_flask():
    return "Hello World!"


# GET /menus | 자료를 가져온다.
@app.route('/menus')
def get_menus():
    return jsonify({'menus': menus})

# POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods = ['POST'])
def create_menu():
    # 전달받은 자료를 menus자원에 추가
    # json형태로 받은 데이터를 파싱한 후 request_data에 저장
    request_data = request.get_json() # {'name': ..., 'price': ...}
    new_menu = {'id' : 4, 'name': request_data['name'], 'price': request_data['price']}
    menus.append(new_menu)
    # 추가한 메뉴를 반환
    return jsonify(new_menu)


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# 필수과제
# PUT /menus/<int:id> | 기존에 있는 자료를 수정(해당하는 id의 메뉴를 수정)
@app.route('/menus/<int:id>', methods = ['PUT'])
def update_menu(id):
    # 전달받은 자료를 menus에 있는 자원수정
    request_data = request.get_json() # {'name': ..., 'price': ...}
    # 최초 인덱스 변수는 가장 마지막 메뉴의 아이디 + 1
    # 입력 받은 id가 메뉴에 없을 경우 "Invalid Id"반환
    idx = INF
    for i, menu in enumerate(menus):
        if menu['id'] == id:
            idx = i
            break
    # 메뉴수정(해당하는 아이디가 없으면 메뉴 추가)
    try:
        menus[idx]['name'], menus[idx]['price'] = request_data['name'], request_data['price']
    except:
        return "Invalid Id"
    else:
        # 수정한 메뉴 반환
        return jsonify(menus[idx])

# DELETE / menus/<int:id> | 해당하는 ID의 데이터 삭제
@app.route('/menus/<int:id>', methods = ['DELETE'])
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
    except:
        return "Invalid Id"
    else:
        # 메뉴 반환
        return jsonify({'menus': menus})

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# 함수를 직접적으로 실행했을 때 app을 실행해라
if __name__ == '__main__':
    app.run()