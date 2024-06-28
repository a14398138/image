from flask import Flask, send_file, render_template_string
from PIL import Image
import io
import random

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!doctype html>
    <title>ランダムピクセル画像生成</title>
    <h1>ランダムピクセル画像生成</h1>
    <button onclick="generateImage()">画像生成</button>
    <br>

<style>
  .container {
    display: flex;
    flex-direction: column; /* 縦方向に並べる */
    align-items: center; /* 中央揃え */
  }
</style>
<div class="container">
    <img id="randomImage" src="/image" alt="ランダムピクセル画像">
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
