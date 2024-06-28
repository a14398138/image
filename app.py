from flask import Flask, send_file, render_template_string
from PIL import Image
import io
import random

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!doctype html>
    <title style=" text-align: center;">運が良ければエッチな画像が出てくるかもしれないサイト</title>
    <h1>運が良ければエッチな画像が出てくるかもしれないサイト</h1>
    <button class="custom-button" onclick="generateImage()">画像を生成</button>
    <br>

<style>
  .container {
    display: flex;
    flex-direction: column; /* 縦方向に並べる */
    align-items: center; /* 中央揃え */
  }
  
        body {
            background-color: black;
            color: orange;
text-align: center;
        }
    .custom-button {
            background: linear-gradient(to right, pink, violet); /* グラデーション背景 */
            color: brack; /* ボタンの文字色 */
            border: none; /* ボーダーなし */
            padding: 15px 32px; /* パディング */
            text-align: center; /* テキスト中央揃え */
            text-decoration: none; /* テキスト装飾なし */
            display: inline-block; /* インラインブロック表示 */
            font-size: 16px; /* フォントサイズ */
            margin: 4px 2px; /* マージン */
            cursor: pointer; /* カーソルをポインターに */
            border-radius: 50px; /* 角を丸く */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* ボックスシャドウ */
            transition: background 0.3s; /* 背景色の遷移 */
        }
</style>
<div class="container">
    <img id="randomImage" src="/image">
<iframe src="https://www.ppc-direct.com/index14.html?affid=235754" width="450" height="20" frameborder="no" scrolling="no" title="テキストバナー"></iframe>

<iframe src="https://www.ppc-direct.com/index22.html?affid=235754" width="728" height="90" frameborder="no" scrolling="no" title="バナー"></iframe>
<iframe src="https://www.mmaaxx.com/index7.html?affid=235754" width="700" height="200" frameborder="no" scrolling="no"></iframe>
<iframe src="https://www.mmaaxx.com/genre/944400X/index700.html?affid=235754" width="700" height="200" frameborder="no" scrolling="no" title="バナー"></iframe>
<iframe src="https://www.ppc-direct.com/index8.html?affid=235754" width="700" height="200" frameborder="no" scrolling="no" title="バナー"></iframe>
<iframe src="https://www.ppc-direct.com/index16.html?affid=235754" width="600" height="200" frameborder="no" scrolling="no" title="バナー"></iframe>
</div>
    <script>
        function generateImage() {
            fetch('/generate')
                .then(response => response.blob())
                .then(blob => {
                    const url = URL.createObjectURL(blob);
                    document.getElementById('randomImage').src = url;
                });
        }
window.addEventListener('load', generateImage);
    </script>
    '''
    return render_template_string(html)

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    width, height = 512,512
    img = Image.new('RGB', (width, height))
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
