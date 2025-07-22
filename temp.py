import json
import uuid
import os

json_path = 'qiita_json.json'

# ファイルが存在しない場合は空のJSONファイルを作成
# os.path.exists(json_path) でファイルの有無を確認
if not os.path.exists(json_path):  # ファイルがなければ
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({}, f, ensure_ascii=False, indent=4)  # 空の辞書をJSONとして保存

# 既存データに新しいデータを追加して保存する関数
def add_cigarette(brand, stock):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # 既存のデータを読み込む
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルがない、または壊れていたら空の辞書にする

    new_id = "cigarette_" + str(uuid.uuid4())  # 一意なIDを作成
    data[new_id] = {
        "brand": brand,
        "cigarette_stock": stock
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # データを保存

# 書き換え（更新）関数
def update_cigarette(cigarette_id, brand=None, stock=None):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # 既存のデータを読み込む
    except (FileNotFoundError, json.JSONDecodeError):
        return False  # ファイルがない、または壊れていたら失敗

    # 指定したIDがデータに存在するか確認
    if cigarette_id in data:  # 存在する場合
        if brand is not None:  # brandが指定されていれば
            data[cigarette_id]['brand'] = brand  # brandを更新
        if stock is not None:  # stockが指定されていれば
            data[cigarette_id]['cigarette_stock'] = stock  # stockを更新
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)  # データを保存
        return True  # 成功
    return False  # IDがなければ失敗

# 削除関数
def delete_cigarette(cigarette_id):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # 既存のデータを読み込む
    except (FileNotFoundError, json.JSONDecodeError):
        return False  # ファイルがない、または壊れていたら失敗

    # 指定したIDがデータに存在するか確認
    if cigarette_id in data:  # 存在する場合
        del data[cigarette_id]  # データを削除
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)  # データを保存
        return True  # 成功
    return False  # IDがなければ失敗

# 使用例
add_cigarette("セブンスター", 10)
update_cigarette("cigarette_xxx", brand="新しいブランド", stock=5)
delete_cigarette("cigarette_xxx")
