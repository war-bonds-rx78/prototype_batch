import sys
import os
import click
import logging
import yaml
from datetime import datetime, timedelta, timezone


# 親ディレクトリをアプリケーションのホーム(${app_home})に設定
app_home = os.path.abspath(os.path.join( os.path.dirname(os.path.abspath(__file__)) , ".." ))
# ${app_home}をライブラリロードパスに追加
sys.path.append(os.path.join(app_home))

from lib import sample_service as service


def cmd () :

    # 処理
    try:

        # ログ開始

        # 設定値取得
        with open('./conf/config.yml', 'r') as yml_file:
            data = yaml.load(yml_file)
            print(data, type(data))

        print(data['msg']['ms001'])
        # メッセージID取得

        # ここで処理を呼ぶのは一回のみ
        # 呼び先で処理をコントロールする
        # 処理実行
        print("***")
        service.sample()

        
        # タイムゾーンの生成
        JST = timezone(timedelta(hours=+9), 'JST')
        datestr = datetime.now(JST).isoformat(timespec='seconds')
        print("現在日付: {0}".format(datestr))

        print("**")

        # ログ終了

    except Exception as e:
        # エラー返却
        print(e)
        # 処理のエラーをここでキャッチ
        sys.exit(1)

if __name__ == '__main__':
    cmd() 