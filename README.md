# サンプル（プロダクト名）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2023/07/JPHACKS2023_ogp.png)](https://www.youtube.com/watch?v=yYRQEdfGjEg)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
### 製品説明（具体的な製品の説明）
```mermaid
sequenceDiagram
title JPHack2023シーケンス
Actor O as 運用者
participant Device_1 as 運用者端末
participant Front as フロントエンド
participant Back as バックエンド
participant System as 処理系
participant Device_2 as 処理系端末

activate Back
Note over Back: データ収集処理
loop XX秒ごと
    System ->> Device_2 : 撮影要求
    Note over Device_2: 撮影
    Device_2 ->> System : 画像データ+ファイルパス保存
    Note over System: 画像解析
    System ->> Back : DB保存処理
    Back -->> System : Ack
    Note over System: 追跡量計算?
    System ->> Device_2 : 追跡要求
    Note over Device_2: 追跡
    Device_2 ->> System : 追跡完了通知
    System ->> Back : DB保存処理
end
Deactivate Back

activate O
Note over O: 検索要求(検索対象名など)
O ->> Device_1 : 検索要求
Device_1 ->> Front : 検索要求
Front ->> Back : DB検索要求
Back ->> Front : 検索結果
Front ->> Device_1 : 検索結果
Device_1 -->> O : 検索結果確認
Deactivate O

```

### 特長
#### 1. 特長1
#### 2. 特長2
#### 3. 特長3

### 解決出来ること
### 今後の展望
### 注力したこと（こだわり等）
* 
* 

## 開発技術
### 活用した技術
#### API・データ
* 
* 

#### フレームワーク・ライブラリ・モジュール
* 
* 

#### デバイス
* 
* 

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
* 
