# cerke_code

机戦のアプリをpygameで書いています。

## To 遊んでみたい人
- PC用です。
- imageフォルダに加えてWinユーザーの方々はexeファイルを、非Winユーザーの方々は.pyファイル5つをダウンロードして同じ場所において走らせると動作するはずです。
- このアプリによる損害や賠償などについて、私は一切責任を負えません。

### 機能説明

- メッセージログを左下のエリアに配置しています。
- 右上のエリアで現在の手番・レート・選択している駒の画像と位置が確認できます。
- ウィンドウのxボタンかEscキーで終了できます。
- クリックで動かしたい駒を選択でき、rキーで反転、移動先にクリックで駒を動かせます。
- スペースキーで駒の選択をキャンセルできます。
- cキーで裁(5D2-5)の結果をメッセージログに表示します。
- zキーでundoが、qキーでredoができます。(最大10手まで)
- p, mキーで点数の増減が行えます。
- 0, 1キーでレートの増減が行えます。
- aボタンで手番の変更ができます。盤面を変えずに相手に手を渡したい時・駒を取って手番が右上とずれた時などの調整にどうぞ。
- iキーで駒の配置を初期配置に戻せますが、向きは戻りません。選択→rで地道に戻してください。
- 既に駒があるところへは駒が動きません。(表示がもろに重なって混乱のもとになるため)


## これから実装したい機能
- 棋譜の生成
- GUI化
- オンライン対戦
- 1Pプレイ
- 多言語対応
