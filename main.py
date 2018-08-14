import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    rps_pattern = {'グー': 0, 'チョキ': 1, 'パー': 2}
    res = {'computer': '', 'user': '', 'result': ''}
    #結果の取得
    str_user = request.args.get('user','')

    if str_user:
        #じゃんけんおボタンが押されている場合
        #ユーザーの手を取得
        user =rps_pattern[str_user]
        #コンピューターの手を作成
        computer= random.randint(0,2)
        #判定
        if user == computer:
            result = 'あいこ'
        else:
            if user == 0 and computer==1 \
                or user== 1 and computer ==2\
                or user == 2 and computer ==0:
                result  = '勝ち'
            else:
                result='負け'
        res = {'computer':computer,'user': user,'result':result}

    return render_template('index.html', res=res)

if __name__ == '__main__':
    # IPアドレス0.0.0.0の8000番ポートでアプリケーションを実行します
    #基本webアプリは必要  つなぐ時は、これ！  http://192.168.33.10:8000/
    app.run('0.0.0.0', 8000, debug=True)
