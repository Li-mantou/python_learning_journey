from random import randint as rint
def good_cost(*args :tuple[str,int|float,int],discont=0,score=0,expense)->float:
    """

    :param args:商品名称 价格 数量
    :param discont: 优惠卷价格
    :param score: 积分数量
    :param expense: 运费
    :return:
    """

    discont: float|int
    score: int
    expense: int|float
    # 储存商品信息,把输入的商品信息价格通过列表解包
    goods_spend = [goods[1] * goods[2] for goods in args ]
    # 商品价格清楚解包计算整个总价格 总价格等于商品总价格-优惠价格-积分价格+运费
    total_prise = sum(goods_spend)
    # 计算优惠后价格
    if total_prise >= 5000:
        total_prise -= discont
    if total_prise >= 5000:
        total_prise -= score//100
    return total_prise + expense

print(good_cost( ("手机",1145,1),("电脑",3997,2),discont=10,score=678,expense=9.9))