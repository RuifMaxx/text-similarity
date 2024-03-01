# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein


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
    # 在此实现SimHash算法
    # 可以使用第三方库如 Simhash 或者实现自己的SimHash算法
    # 此处简化为直接返回0
    return 0

def calculate_similarity(text1, text2, method):
    if method == 'cosine':
        return calculate_cosine_similarity(text1, text2)
    elif method == 'levenshtein':
        return calculate_levenshtein_similarity(text1, text2)
    elif method == 'simhash':
        return calculate_simhash_similarity(text1, text2)
    else:
        return None


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
    app.run(debug=False, host='0.0.0.0', port=80)