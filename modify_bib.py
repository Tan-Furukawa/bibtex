
#!----------------------------------------------------
#! 注意! bibdeskと紐づいているパスでこのコードを実行しないこと
#!----------------------------------------------------
# まあゆうて大丈夫

#%%
#%%
import re

def modify_and_save_tex_file(file_path, save_path, str_from="{img/", to="{"):
    """
    指定された.texファイル内の"{img/"を"{"に置換し、新しいファイルに保存する。
    
    :param file_path: 変更する.texファイルのパス
    """
    try:
        # 入力ファイルを開き、内容を読み込む
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # "{img/"を"{"に置換
        modified_content = content.replace(str_from, to)
        
        # 置換した内容を新しいファイルに保存
        with open(save_path, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)
        
        print(f"ファイルが正常に変更され、{save_path}に保存されました。")
    except FileNotFoundError:
        print(f"指定されたファイルが見つかりません: {file_path}")
    except Exception as e:
        print(f"ファイルの変更中にエラーが発生しました: {e}")

def remove_url_fields_from_bib(bib_file, output_file):
    with open(bib_file, 'r') as file:
        bib_data = file.read()

    # 正規表現を使って各エントリーの間を切り分ける
    entries = re.split(r'(?=@)', bib_data)

    # 各エントリーごとに処理
    modified_entries = []
    for entry in entries:
        # 不要なフィールドを削除
        entry = re.sub(r'(url|biburl|eprint)\s*=\s*{[^{}]*},?\n?', '', entry)
        modified_entries.append(entry)

    # 更新されたエントリーを結合
    modified_bib_data = ''.join(modified_entries)

    # 更新された内容を新しいファイルに書き込む
    with open(output_file, 'w') as file:
        file.write(modified_bib_data)

# この部分は絶対に変更しない(まあゆうて大丈夫)
remove_url_fields_from_bib('summary.bib', 'summary_mod.bib')
modify_and_save_tex_file('summary_mod.bib', 'summary_mod.bib', "{https://","{")
#%%