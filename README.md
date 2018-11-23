# aws_iot_line_notify
AWS の IoT 1-Click で呼び出す Lambda から LINE に通知を送る

# 環境に合わせて修正する箇所
apex/functions/notify/function.json  
1. "role": "arn:aws:iam::123456789012:role/lambda-execution-role",  
→「123456789012」：自分のAWSアカウントに変更。  
→「lambda-execution-role」：お好きなロールに変更。とりあえずCloudWatch Logsに読み書き可能であればOK  
2. "token": "ABCDEFG",  
→「"ABCDEFG"」：LINE Notifyで取得したtokenに変更。

