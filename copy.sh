#!/bin/bash

destination_dir="$(dirname $0)"
source_file="/../article/summary.bib"
source_full_path="$destination_dir$source_file"

echo "-----"
echo $source_full_path
echo $destination_dir
echo "-----"

# コピーを実行
cp "$source_full_path" "$destination_dir"

# 成功メッセージを表示
echo "File $source_file が $destination_dir にコピーされました。"

cd $destination_dir
git add -A
git commit -m "update"
git push