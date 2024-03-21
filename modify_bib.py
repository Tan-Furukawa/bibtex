
#!----------------------------------------------------
#! 注意! bibdeskと紐づいているパスでこのコードを実行しないこと
#!----------------------------------------------------
# まあゆうて大丈夫

#%%
import re
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
#%%