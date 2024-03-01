# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein
from simhash import Simhash


app = Flask(__name__)

def calculate_cosine_similarity(text1, text2):
    # 合并文本，用于构建文本向量
    combined_text = [text1, text2]

    # 使用CountVectorizer进行文本向量化
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(combined_text)

    # 计算余弦相似度
    similarity_matrix = cosine_similarity(vectors)
    cosine_similarity_value = similarity_matrix[0, 1]

    return cosine_similarity_value

def calculate_levenshtein_similarity(text1, text2):
    # 计算两个字符串的相似度
    similarity = 1 - Levenshtein.distance(text1, text2) / max(len(text1), len(text2))
    return similarity

def calculate_simhash_similarity(text1, text2):
    
    a_simhash = Simhash(text1)
    b_simhash = Simhash(text2)
    max_hashbit = max(len(bin(a_simhash.value)), len(bin(b_simhash.value)))
    distince = a_simhash.distance(b_simhash)
    similarity = 1 - distince / max_hashbit
    
    return similarity

def calculate_similarity(text1, text2, method):
    if method == 'cosine':
        return calculate_cosine_similarity(text1, text2)
    elif method == 'levenshtein':
        return calculate_levenshtein_similarity(text1, text2)
    elif method == 'simhash':
        return calculate_simhash_similarity(text1, text2)
    else:
        return None


@app.before_request
def before_request():
    if request.url.startswith('https://1'):
        url = f'https://sim.ppeak.site{request.path}'
        code = 301
        return redirect(url, code=code)


@app.route('/', methods=['GET', 'POST'])
def index():
    similarity = None
    default_method = 'cosine'  # 提供默认的 method
    
    if request.method == 'POST':
        paper1 = request.form.get('paper1', '')  # 使用 get 方法，如果不存在则返回空字符串
        paper2 = request.form.get('paper2', '')
        method = request.form.get('method', '')  # 同样使用 get 方法

        # 检查是否收到了有效的 method
        if method not in ['cosine', 'levenshtein', 'simhash']:
            return "Invalid method"

        # 计算相似度
        similarity = calculate_similarity(paper1, paper2, method)

    return render_template('index.html', similarity=similarity)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10007,ssl_context=('sim.ppeak.site_bundle.crt','sim.ppeak.site.key'))