# 要求機能

- **楽譜入力**：デジタル形式の楽譜を画像ファイルとして入力。
- **音符認識**：楽譜内の五線譜（横線）と音符や休符の種類認識。
- **結果出力**：認識した情報を、人間が解釈可能な形に変換して出力。例えば、楽譜の音符をJSON形式で表現できる形式に出力する。

# 製作ステップ

1. **要件分析**
    - 何を認識する必要があるのか決める：
    ①音符の種類（音の高さと長さ、位置）
    ②五線譜（横線）の位置
    - 入力タイプの決定：
        - 印刷された画像（png）
2. **システム設計**
    - システム全体の構成を決定:
        - **フロントエンド**：ユーザーはアップロードされる楽譜画像を入力し、その結果を表示する。
        - **バックエンド**：画像処理および音符認識のロジックを実装する。
    - データフロー:
    ①楽譜のインプット -> 前処理 -> 音符検出 -> 画像クロップ -> 音符認識 -> 結果出力 (JSON)
    ②楽譜のインプット -> 前処理 -> 五線譜認識 -> 結果出力 (JSON)
3. **前処理**
①、②共通：**グレースケール変換**：入力画像をグレースケールに変換。
②のみ　**：エッジ検出+ハフ変換** : 水平な直線を検出
4. **音符認識のアルゴリズム**
Pytorchのオブジェクトディテクションタスクを使用
5. **データ変換と出力**
    - JSONで**音符、リズム、長さ、位置情報等**を構造化して出力。

# 出力形式

- JSON形式のリスト:
    - 音符の音程、長さを含む

# Required Features

- **Sheet Music Input**: Input digital sheet music as an image file.
- **Note Recognition**: Recognize the staff lines (horizontal lines) and types of notes and rests in the sheet music.
- **Output Results**: Convert the recognized information into a human-interpretable format. For example, output the notes in the sheet music in JSON format.

# Development Steps

1. **Requirements Analysis**
    - Determine what needs to be recognized:
    ① Types of notes (pitch, duration, position)
    ② Position of the staff lines (horizontal lines)
    - Decide on the input type:
        - Printed images (png)
2. **System Design**
    - Decide on the overall system architecture:
        - **Frontend**: Users upload the sheet music image and view the results.
        - **Backend**: Implement the logic for image processing and note recognition.
    - Data Flow:
    ① Sheet music input -> Preprocessing -> Note detection -> Image cropping -> Note recognition -> Output results (JSON)
    ② Sheet music input -> Preprocessing -> Staff line recognition -> Output results (JSON)
3. **Preprocessing**
Common for ① and ②: **Grayscale Conversion**: Convert the input image to grayscale.
Only for ②: **Edge Detection + Hough Transform**: Detect horizontal lines.
4. **Note Recognition Algorithm**
Use Pytorch's object detection task.
5. **Data Conversion and Output**
    - Output the notes, rhythm, duration, position information, etc., in a structured JSON format.

# Output Format

- JSON format list:
    - Includes the pitch and duration of the notes.