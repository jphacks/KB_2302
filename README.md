# 探しAI(さがしあい)

[![](https://img.youtube.com/vi/FrMOqFT5mPo/0.jpg)](https://www.youtube.com/watch?v=FrMOqFT5mPo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
私たちは複数人で衛星開発を行っており，道具や部品が散らばったり，無くなったりする事がよくある．これは自分がどこにしまったか忘れてしまっていることや，他の人が移動させたことが原因で起きており，同様の問題は研究室や作業部屋といった複数人で空間を共有する場合のみならず個人の家の中であっても起こりうるものである．こうした課題を解決する紛失防止タグといった製品は需要があり，徐々に浸透してきているが，タグはそれ自体が高価であったり，取り付けにくいものがあるなどから，紛失防止が十分に達成されているとは言えないと思われる．私たちはこういった問題を解決するべく，より多くのものの捜索を行うことができるサービスを実現したいと考え，AIの画像認識を用いた物体追跡により，もの探しを支援するアプリの開発に至った．

### 製品説明（具体的な製品の説明）
本サービスはカメラを用いたもの探し支援アプリである．カメラで撮影したデータをAIによって処理することで物体をトラッキングし、物がしまわれた、持ち出された等を検知・記録する．使用者は、無くしたものを検索フォームから探すことができる．
### 特長
#### 1. 「低コスト」
トラッキングのためのデバイスをモノに取り付ける必要がないため，コストと手間が抑えられる．

#### 2. 「高いトラッキング性」
モノが消失するタイミングに焦点を当てることで，どのようなモノの無くなり方にも対応できる．
物が消失した際の写真を保持するので，無くした，持ち出された，捨てられたなどの物がなくなった原因であったり，その時の周りの状況であったりを同時に知ることができる．

#### 3. 「便利な検索機能」
AIを利用した画像処理を行っているので，キーワード入力で無くしたものを検索できる．

### 解決出来ること
* 紛失防止タグをつけづらい物やタグ本体よりも安価な物など，今までタグをつけることが無かった物の捜索を行うことができる．
* 探したい物が増えてもコストが増大しないため，ユーザにとって経済的である．
* 画像データで保存されるため，室内といった狭い場所でも正確な場所が分かる．
* 持ち出された際の状況や誰が持ち出したかなど，タグでは知ることは出来なかった，より詳細な情報をユーザに伝えることができる．
* 本システムは一般的なWebカメラ程度で動作し，特別なハードウェアを必要としない．そのため，ユーザへの負担が減る&開発者にとっても開発のイニシャルコストが低減でき，迅速に「モノ探しのコストを減らす」という機能を社会に提供できる．

### 今後の展望
* 人物を判定し，誰が持っているかを通知してくれるようにする．
* キーワード検索にとどまらず，画像検索など柔軟な検索が行えるようにする．
* 認識したものの個数を数えることができるため，物品の数量管理へ応用ができるようにする．

### 注力したこと（こだわり等）
* AIによる画像認識，画像認識結果の保持・更新，UIを分離したことで，AIの学習セットの変更や保持する情報の追加や削除，UIの更新に柔軟に対応し，将来的な機能追加を見据えたシステム構成としたこと．
* UIにおける探しもののキーワード検索画面にて，株式会社NTTドコモのテキストペア類似度APIを利用することで，曖昧なキーワード検索にも柔軟に対応し，ユーザのキーワード選定の負担を低減したこと．
* データベースにアップロードされた画像毎ではなく，ラベル毎にテキストペア類似度APIを用いることで，曖昧キーワード検索における検索速度を実測値として4倍以上高速化した(20秒以上→5秒)．
* 軽量なAI「Yolov8」を用いるとともに，画像認識結果の更新において無駄な処理をできる限り省いたことで，ラップトップ程度の一般的なCPUでも追跡対象の物体が追尾可能な7fps程度の準リアルタイム性を確保したこと．
* PWA(Progressive Web App)に対応し，スマートフォンでホームに追加した際にはネイティブアプリのように利用可能にしたこと．

## 開発技術
### 活用した技術
#### API・データ
* Firebase API
* [gooラボテキストペア類似度API](https://labs.goo.ne.jp/api/textpair_doc)

#### フレームワーク・ライブラリ・モジュール
* 物体検出用AI「Ultralytics YOLOv8 」
* FastAPI
* Vuetify
* 

#### デバイス
* Webカメラ
* 

#### インフラ
* Firebase
* Microsoft Azure
* Docker
* Render

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 物体のトラッキング機能
* 

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
* 
