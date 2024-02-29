from flask import Flask, render_template, request, redirect
import Levenshtein

app = Flask(__name__)

def calculate_similarity(text1, text2):
    # 计算两个字符串的相似度
    similarity = 1 - Levenshtein.distance(text1, text2) / max(len(text1), len(text2))
    return similarity

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route('/', methods=['GET', 'POST'])
def index():
    similarity = None

    if request.method == 'POST':
        paper1 = request.form['paper1']
        paper2 = request.form['paper2']

        # 计算相似度
        similarity = calculate_similarity(paper1, paper2)

    return render_template('index.html', similarity=similarity)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=443,ssl_context=('sim.ppeak.site_bundle.crt','sim.ppeak.site.key'))
