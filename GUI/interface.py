import flet as ft
import os
import asyncio

import process

class App:
    def __init__(self):
        self.input_dir = None
        self.output_dir = None
        self.input_TorF = False
        self.output_TorF = False
        self.finished = False

    def main(self, page: ft.Page):

        def toggle_running_button():
            running_button.visible = self.input_TorF and self.output_TorF
            running_button.update()

        def toggle_finished_message():
            finished_message.visible = self.finished
            finished_message.update()

        # 入力フォルダの選択
        def get_input_dir(event: ft.FilePickerResultEvent):
            self.input_dir = event.path if event.path else None
            selected_input_dir.value = self.input_dir if self.input_dir else "キャンセルされました。"
            selected_input_dir.update()
            self.input_TorF = os.path.isdir(self.input_dir)
            toggle_running_button()

        # 出力フォルダの選択
        def get_output_dir(event: ft.FilePickerResultEvent):
            self.output_dir = event.path if event.path else None
            selected_output_dir.value = self.output_dir if self.output_dir else "キャンセルされました。"
            selected_output_dir.update()
            self.output_TorF = os.path.isdir(self.output_dir)
            toggle_running_button()



        # 処理開始
        async def running():
            running_button.disabled = True
            running_button.update()

            try:
                # 処理開始
                process.process(self.input_dir, self.output_dir)

                # 処理完了
                self.finished = True
                finished_message.value = "処理が完了しました！"  # 完了メッセージを設定
                finished_message.color = "green"  # メッセージの色を緑に設定
                toggle_finished_message()

            except Exception as e:
                # エラーが発生した場合の処理
                finished_message.value = f"エラーが発生しました: {e}"
                finished_message.color = "red"
                finished_message.visible = True
                finished_message.update()

            finally:
                running_button.disabled = False
                running_button.update()





        # 完了メッセージ
        finished_message = ft.Text(
            value="",
            visible=False,
            color="green",
            size=20,
            text_align=ft.TextAlign.CENTER,
        )

        # ボタンとテキスト
        running_button = ft.ElevatedButton(
            "処理開始",
            icon=ft.Icons.DIRECTIONS_RUN,
            icon_color="pink500",
            visible=False,
            on_click=lambda _: asyncio.run(running()),
        )
        finish_button = ft.ElevatedButton(
            "ウィンドウを閉じる",
            icon=ft.Icons.CLOSE,
            icon_color="red500",
            on_click=lambda _: page.window_close(),
        )
        selected_input_dir = ft.Text(value="選択されていません", color="blue")
        selected_output_dir = ft.Text(value="選択されていません", color="blue")
        dir_input_picker = ft.FilePicker(on_result=get_input_dir)
        dir_output_picker = ft.FilePicker(on_result=get_output_dir)
        page.overlay.extend([dir_input_picker, dir_output_picker])

        # テーマ設定
        page.theme_mode = ft.ThemeMode.LIGHT
        page.title = "画像処理ツール"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window_height = 600
        page.window_width = 800

        # レイアウト
        page.add(
            ft.Column(
                [
                    ft.Text("画像処理ツール", size=30, weight=ft.FontWeight.BOLD),
                    ft.Divider(height=20, thickness=1),
                    ft.Text("1. 入力フォルダを選択してください", size=18),
                    ft.ElevatedButton(
                        "フォルダを指定",
                        icon="DRIVE_FOLDER_UPLOAD_ROUNDED",
                        icon_color="blue500",
                        on_click=lambda _: dir_input_picker.get_directory_path(),
                    ),
                    ft.Text("選択フォルダ:", size=16),
                    selected_input_dir,
                    ft.Divider(height=20, thickness=1),
                    ft.Text("2. 出力先を選択してください", size=18),
                    ft.ElevatedButton(
                        "フォルダを指定",
                        icon="DRIVE_FOLDER_UPLOAD_ROUNDED",
                        icon_color="blue500",
                        on_click=lambda _: dir_output_picker.get_directory_path(),
                    ),
                    ft.Text("選択フォルダ:", size=16),
                    selected_output_dir,
                    ft.Divider(height=20, thickness=1),
                    running_button,
                    finished_message,
                    ft.Divider(height=20, thickness=1),
                    finish_button,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )


