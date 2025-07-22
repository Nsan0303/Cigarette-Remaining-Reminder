import json
import uuid
import os

json_path = 'qiita_json.json'
global cigarette_stock
cigarette_stock = "ピースアンバーノート"


# ファイルが存在しない場合は空のJSONファイルを作成
if not os.path.exists(json_path):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({}, f, ensure_ascii=False, indent=4)

# 新しい銘柄を追加する関数
def add_cigarette(brand, stock):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # UUIDを生成し、キーを作成
    new_id = "cigarette_" + str(uuid.uuid4())
    data[new_id] = {
        "brand": brand,
        "cigarette_stock": stock
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return new_id  # 追加したIDを返すと使いやすい

# 既存の銘柄情報を更新する関数
def update_cigarette(cigarette_id, brand=None, stock=None):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    if cigarette_id in data:
        if brand is not None:
            data[cigarette_id]['brand'] = brand
        if stock is not None:
            data[cigarette_id]['cigarette_stock'] = stock
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    else:
        return False

# 銘柄情報を削除する関数
def delete_cigarette(cigarette_id):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    if cigarette_id in data:
        del data[cigarette_id]
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    else:
        return False

# 使い方の例
if __name__ == "__main__":
    # 新しい銘柄を追加しIDを受け取る
    new_id = add_cigarette("セブンスター", 10)
    print(f"追加した銘柄のID: {new_id}")

    # 追加したIDを使って更新
    updated = update_cigarette(new_id, brand="セブンスター・リニューアル", stock=15)
    print("更新成功:", updated)

    # 削除も同様にIDを使って行う
    deleted = delete_cigarette(new_id)
    print("削除成功:", deleted)
