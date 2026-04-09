from flask import Flask, render_template, request

app = Flask(__name__)

menus = {
    1: {
        "name": "カフェラテ", 
        "category": "drink", 
        "hot": "①牛乳をコーヒーマシーンにセットする\n②カフェラテのボタンを押す", 
        "ice": "①グラスに氷を入れる\n②冷たい牛乳を注ぐ\n③エスプレッソのボタンを押す"
    },
    2: {
        "name": "アイスコーヒー", 
        "category": "drink", 
        "ice": "①グラスに氷を入れる\n②コーヒーを注ぐ"
    },
    3: {"name": "明太子パスタ", "category": "food", "recipe": "①ソースを湯煎で温める(4分)\n②大葉を2枚刻む\n③パスタを茹でる(45秒)\n④ソースとパスタを混ぜ、大葉をトッピングする"},
    4: {"name": "チキンオーバーライス", "category": "food", "recipe": "①チキンマリネを湯煎で温める(4分)\n②バーレライスをレンジで解凍(4分)\n③レタスを千切りにし、トマトを角切りにする\n④バーレライスの上にチキンマリネを乗せ、レタスとトマトをトッピングする\n⑤ホットソースを5gかけ、ヨーグルトソースを網目状にかける"},
    5: {"name": "レジ締め", "category": "closing", "recipe": "①現金を数える\n②報告書を書く"},
    6: {
        "name": "ブレンドコーヒー", 
        "category": "drink", 
        "hot": "①コーヒーマシーンのホットコーヒーのボタンを押す",
    },
    7: {"name": "Aサンド", "category": "food", "recipe": "①パニーニを半分に切り、マスタード、マヨネーズ、シーザードレッシングを塗る\n②ハム、パストラミ、チーズの順で挟む\n③パニーニをクッキングシートで包みプレスして焼く(片面2分の計4分)"},
    8: {"name": "その他", "category": "other", "recipe": "ほうき、クイックルワイパーで店内を掃除する\nゴミをまとめる\nトイレ掃除をする\nテーブルを拭く\n店内の備品を補充する\netc"},
}

@app.route("/")
def index():
    return render_template("index.html", menus=menus)

@app.route("/menu/<int:menu_id>")
def detail(menu_id):
    menu = menus[menu_id]
    return render_template("detail.html", menu=menu)

@app.route("/search")
def search():
    
    query = request.args.get("q", "")
    
    results = {}
    for id, menu in menus.items():
        
        if query.lower() in menu["name"].lower():
            results[id] = menu
            
    return render_template("index.html", menus=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)
