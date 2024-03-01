from simhash import Simhash


def simhash_demo(text_a, text_b):
    """
    求两文本的相似度
    :param text_a:
    :param text_b:
    :return:
    """
    a_simhash = Simhash(text_a)
    b_simhash = Simhash(text_b)
    max_hashbit = max(len(bin(a_simhash.value)), len(bin(b_simhash.value)))
    # 汉明距离
    distince = a_simhash.distance(b_simhash)
    print(distince)
    similar = 1 - distince / max_hashbit
    return similar


if __name__ == '__main__':
    text1 = "傲游AI专注于游戏领域,多年的AI技术积淀,一站式提供文本、图片、音/视频内容审核,游戏AI以及数据平台服务"
    text2 = "傲游AI专注于游戏领域,多年的AI技术积淀,二站式提供文本、图片、音 视频内容审核,游戏AI以及数据平台服务"
    text3 = '"傲游AI专注于游戏领域,多年的AI技术积淀,三站式提供文本、图片、音视频内容审核，游戏AI以及数据平台服务"'
    similar = simhash_demo(text1, text2)
    similar2 = simhash_demo(text1, text3)
    similar3 = simhash_demo(text2, text3)
    print(similar)
    print(similar2)
    print(similar3)
