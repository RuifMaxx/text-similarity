from flask import Flask, render_template, request

import Levenshtein
import re
import math

app = Flask(__name__)

def calculate_cosine_similarity(text1, text2):
    # 文本预处理：去除标点符号和空格，将文本转为小写
    text1 = re.sub(r'[^\w\s]', '', text1.lower())
    text2 = re.sub(r'[^\w\s]', '', text2.lower())

    # 分词
    words1 = text1.split()
    words2 = text2.split()

    # 构建词频字典
    word_frequency = {}
    for word in set(words1 + words2):
        word_frequency[word] = (words1.count(word), words2.count(word))

    # 计算余弦相似度
    dot_product = sum(f1 * f2 for f1, f2 in word_frequency.values())
    magnitude1 = math.sqrt(sum(f1 ** 2 for f1, _ in word_frequency.values()))
    magnitude2 = math.sqrt(sum(f2 ** 2 for _, f2 in word_frequency.values()))

    if magnitude1 * magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)

def calculate_levenshtein_similarity(text1, text2):
    # 计算两个字符串的相似度
    similarity = 1 - Levenshtein.distance(text1, text2) / max(len(text1), len(text2))
    return similarity

def simhash(text):
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
        hash1 = simhash(text1)
        hash2 = simhash(text2)
        # 在此计算SimHash相似度
        # 此处简化为直接返回0
        return 0
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
    app.run(debug=True, host='0.0.0.0', port=443,ssl_context=('sim.ppeak.site_bundle.crt','sim.ppeak.site.key'))
