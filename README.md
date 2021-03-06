# aws_iot_line_notify
AWS の IoT 1-Click で呼び出す Lambda から LINE に通知を送る

# 環境に合わせて修正する箇所
apex/functions/notify/function.json  
1. "role": "arn:aws:iam::123456789012:role/lambda-execution-role",  
→「123456789012」：自分のAWSアカウントに変更。  
→「lambda-execution-role」：お好きなロールに変更。とりあえずCloudWatch Logsに読み書き可能であればOK  
2. "token": "ABCDEFG",  
→「"ABCDEFG"」：LINE Notifyで取得したtokenに変更。
3. 通知内容の編集  
"clickType_single": シングルクリック時に通知する内容  
"clickType_double": ダブルクリック時に通知する内容  
"clickType_long": ロングクリック時に通知する内容  

# Lambda関数のデプロイ方法
apexを使っているので、apexディレクトリの下で以下のコマンドを実行。  

```
apex deploy
```

デプロイすると、iot_line_notifyというLambda関数が作成される。  
apexを使いたくない場合は、notifyディレクトリ以下をzipで固めて直接Lambdaにアップロードする。  
Lambdaの設定内容はfunction.jsonを参照。  

# Lambdaのテストパラメータ
```
{
  "deviceInfo": {
    "deviceId": "G030PMXXXXXXXXXX",
    "type": "button",
    "remainingLife": 99.3,
    "attributes": {
      "projectRegion": "ap-northeast-1",
      "projectName": "sample-project",
      "placementName": "Sample-Placement",
      "deviceTemplateName": "SampleRequest"
    }
  },
  "deviceEvent": {
    "buttonClicked": {
      "clickType": "SINGLE",
      "reportedTime": "2018-10-28T16:16:08.000Z"
    }
  },
  "placementInfo": {
    "projectName": "Sample-Project",
    "placementName": "Sample-Placement",
    "attributes": {
      "key": "value"
    },
    "devices": {
      "Sample-Request": "G030PMXXXXXXXXXX"
    }
  }
}
```
