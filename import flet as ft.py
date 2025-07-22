# 雑記
# フロントエンドの基本部分が完成したので、
# これをベースにバックエンドの実装を進めます。
# その後、フロントエンドの細かい調整を行う予定
# コメントアウトの部分は後ほどGItHubにアップロードする際に削除する予定

# 今後追加する機能:
# - タバコの在庫をJSONなどのデータベースに保存する
# - タバコごとに固有IDを生成して在庫管理を行う、固有IDごとに喫煙ログを管理す、
# - 可能であれば外部データベースを利用し、スマホアプリも開発する
# web版を実装する場合はユーザー認証を追加し、ユーザーごとにデータを管理する必要がある
# 現在の動作ではweb版で動かすのは難しいため、web版用のコードを別途用意する必要がある、そのため、まずはデスクトップ版の機能を完成させ、
# デザインやUIの調整は後回しにして、機能の実装を優先する



# ここまでの実装内容:
# - Fletを使って基本的なUIを作成
# - 銘柄登録画面と喫煙ログ登録画面を実装
# - メイン画面から各画面に遷移できるようにした
# - タバコ管理画面は未実装だが、将来の機能として計画中

# 課題
# Jsonなどの勉強をする必要がある
# - ユーザー認証やセキュリティ、データベースの設計を学ぶ必要がある
# - タバコごとに固有IDを生成する方法を調査する
# サーバーの調達を検討する必要がある
# swiftやkotlinなどのモバイルアプリ開発言語を学ぶ必要がある
# 公開する場合販売場所、価格、販売方法などを検討する必要がある



import os

import flet as ft
import datetime

global json_path


# 現在時刻を文字列で取得
now = datetime.datetime.now() 
str_now = now.strftime('%Y-%m-%d %H:%M:%S')


def main(page: ft.Page):
    page.title = "Flet Example"
    page.window.width = 490
    page.window.height = 490
    page.window.min_width = 490
    page.window.min_height = 490
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 銘柄登録画面を表示する関数
    def show_brand_registration(e):
        page.controls.clear()
        print("銘柄登録画面が表示されました")
        brand_name_field = ft.TextField(label="銘柄名を入力してください")
        count_field = ft.TextField(label="タバコの残りの本数を入力してください")

        def register_brand(e):
            brand_name = brand_name_field.value
            count = count_field.value
            print(f"登録された銘柄名: {brand_name}, 本数: {count}, 登録時間: {str_now},ユーザーネーム")
            page.add(ft.Text(f"在庫登録完了！ 銘柄名: {brand_name}, 本数: {count}, 登録時間: {str_now},ユーザーネーム"))
            
        page.add(
            ft.Column(
                [
                    ft.Text("銘柄登録画面", size=30, weight=ft.FontWeight.BOLD),
                    brand_name_field,
                    count_field,
                    ft.Row(
                        [
                            ft.ElevatedButton(text="登録", on_click=register_brand),
                            ft.ElevatedButton(text="戻る", on_click=show_main_screen),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # 喫煙本数登録画面を表示する関数
    def show_smoking_registration(e):
        page.controls.clear()
        print("喫煙ログ登録画面が表示されました")
        brand_name_field_smoking = ft.TextField(label="銘柄名を入力してください")
        count_smoking_field = ft.TextField(label="喫煙した本数を入力してください")

        def register_smoking(e):
            smoking_brand_name = brand_name_field_smoking.value
            smoking_count = count_smoking_field.value
            print(f"登録された銘柄名: {smoking_brand_name}, 本数: {smoking_count}, 登録時間: {str_now},ユーザーネーム")
            page.add(ft.Text(f"喫煙ログ登録完了！ 銘柄名: {smoking_brand_name}, 本数: {smoking_count}, 登録時間: {str_now},ユーザーネーム"))

        page.add(
            ft.Column(
                [
                    ft.Text("喫煙ログ登録画面", size=30, weight=ft.FontWeight.BOLD),
                    brand_name_field_smoking,
                    count_smoking_field,
                    ft.Row(
                        [
                            ft.ElevatedButton(text="登録", on_click=register_smoking),
                            ft.ElevatedButton(text="戻る", on_click=show_main_screen),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # タバコ管理画面を表示する関数（未実装）
    def show_cigarette_management_screen(e):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("タバコ管理画面はまだ実装されていません。"),
                    ft.Text("ここでは、タバコの使用状況や統計情報を表示する予定です。"),
                    ft.ElevatedButton(text="戻る", on_click=show_main_screen),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # メイン画面を表示する関数
    def show_main_screen(e=None):
        print("メイン画面が表示されました")
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("Cigarette Remaining Reminder", size=30, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton(text="銘柄登録", on_click=show_brand_registration),
                    ft.ElevatedButton(text="喫煙本数登録", on_click=show_smoking_registration),
                    ft.ElevatedButton(text="タバコ管理", on_click=show_cigarette_management_screen),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    show_main_screen()
    print()
if __name__ == "__main__":
    ft.app(target=main)
