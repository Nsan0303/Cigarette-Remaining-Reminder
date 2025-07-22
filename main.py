import flet as ft

def main(page: ft.Page):
    page.title = "Flet Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 銘柄登録画面を表示する関数
    def show_brand_registration(e):
        page.controls.clear()
        print("銘柄登録画面が表示されました")
        # 銘柄名入力用テキストフィールド
        brand_name_field = ft.TextField(label="銘柄名を入力してください")
        # タバコの残り本数入力用テキストフィールド
        count_field = ft.TextField(label="タバコの残りの本数を入力してください")

        # 「登録」ボタンが押されたときの処理
        def register_brand(e):
            # 入力された銘柄名と本数を取得
            brand_name = brand_name_field.value
            count = count_field.value
            print(f"登録された銘柄名: {brand_name}, 本数: {count}")
            # 登録完了メッセージを表示
            page.add(ft.Text(f"在庫登録完了！ 銘柄名: {brand_name}, 本数: {count},"))

        # 銘柄登録画面のUIを追加
        page.add(ft.Text("銘柄登録画面", size=30, weight=ft.FontWeight.BOLD))
        page.add(brand_name_field)
        page.add(count_field)
        page.add(ft.ElevatedButton(text="登録", on_click=register_brand))
        page.add(ft.ElevatedButton(text="戻る", on_click=show_main_screen))
        page.update()

    # 喫煙本数登録画面を表示する関数
    def show_smoking_registration(e):
        page.controls.clear()
        print("喫煙ログ登録画面が表示されました")
        # 銘柄名入力用テキストフィールド
        brand_name_field_smoking = ft.TextField(label="銘柄名を入力してください")
        # 喫煙本数入力用テキストフィールド
        count_smoking_field = ft.TextField(label="喫煙した本数を入力してください")

        # 「登録」ボタンが押されたときの処理
        def register_smoking(e):
            smoking_brand_name = brand_name_field_smoking.value
            smoking_count = count_smoking_field.value
            print(f"登録された銘柄名: {smoking_brand_name}, 本数: {smoking_count}")
            # 登録完了メッセージを表示
            page.add(ft.Text(f"喫煙ログ登録完了！ 銘柄名: {smoking_brand_name}, 本数: {smoking_count}"))

        # 喫煙本数登録画面のUIを追加
        page.add(ft.Text("喫煙ログ登録画面", size=30, weight=ft.FontWeight.BOLD))
        page.add(brand_name_field_smoking)
        page.add(count_smoking_field)
        page.add(ft.ElevatedButton(text="登録", on_click=register_smoking))
        page.add(ft.ElevatedButton(text="戻る", on_click=show_main_screen))
        page.update()

    # タバコ管理画面を表示する関数（未実装）後でグラフや統計情報を表示予定
    def show_cigarette_management_screen(e):
        page.controls.clear()
        # 今後グラフや統計情報を表示予定
        page.add(ft.Text("タバコ管理画面はまだ実装されていません。"))
        page.add(ft.Text("ここでは、タバコの使用状況や統計情報を表示する予定です。"))
        page.add(ft.ElevatedButton(text="戻る", on_click=show_main_screen))
        page.update()

    # メイン画面を表示する関数
    def show_main_screen(e=None):
        print("メイン画面が表示されました")
        page.controls.clear()
        page.add(ft.Text("Cigarette Remaining Reminder", size=30, weight=ft.FontWeight.BOLD))
        page.add(ft.Button(text="銘柄登録", on_click=show_brand_registration))
        page.add(ft.Button(text="喫煙本数登録", on_click=show_smoking_registration))
        page.add(ft.Button(text="タバコ管理", on_click=show_cigarette_management_screen))
        page.update()

    show_main_screen()

if __name__ == "__main__":
    ft.app(target=main)