# Windows × Codex: Leo 日本語ナレーション

Windows の Codex から、**自分で正規に入手した** [tts-ja-harness](https://note.com/mrpocha/n/n5a84a60f1f95) と xAI Grok TTS の Leo 音声を使うための補助スキルです。長い原稿の分割、生成、読みと音量の検査、結合までを Codex に依頼できます。

**このリポジトリには有料ハーネス本体はありません。** 同梱のスクリプト、Skill 定義、サンプル、改変版の再配布も行いません。使う人ごとに作者から取得し、利用条件を守ってください。xAI の API キーと利用料金も各自で用意します。

## インストール

PowerShell で、このリポジトリを Codex のスキルフォルダーに取得します。

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/puuku0510/windows-leo-narration.git "$env:USERPROFILE\.codex\skills\windows-leo-narration"
```

続いて、購入したハーネスを**別の個人用フォルダー**に展開し、その版の手順で `run-narration-tts` を設定してください。Git Bash、Python、ffmpeg、`XAI_API_KEY` が必要です。API キーは GitHub に登録せず、実行環境へ安全に渡してください。

Codex では「`$windows-leo-narration` を使って、この原稿を Leo の日本語ナレーションにして」と依頼できます。最初は短いテスト原稿で試してください。

## 内容と制限

- [SKILL.md](SKILL.md): 制作フローと品質確認
- [Windows 実行メモ](references/windows.md): Git Bash、UTF-8、日本語 JSON の確認点

このスキルは購入ハーネスの操作を助ける独立した指示書です。ハーネス自体をインストールしたり、ライセンスを付与したりはしません。作者の Windows 動作確認は示されていないため、環境ごとに短い音声で検証してください。Leo は xAI の既成音声で、特定人物の声を複製するものではありません。

このリポジトリのオリジナル文書は [MIT License](LICENSE) で公開します。**購入ハーネスには適用されません。**
