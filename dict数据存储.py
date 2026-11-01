print("欢迎使用购物车系统,请挑选您的商品")
menu ="""
"########## 购物车系统 ##########"
"#       1. 添加购物车          #"
"#       2. 修改购物车          #"
"#       3. 删除购物车          #"
"#       4. 查询购物车          #"
"#       5. 退出购物车          #"
"""
print(menu)
shoping_cart = {}
while True:
    chose = input("请选择您的操作(1-5):")
    if chose == "1":#添加购物车
         goods_name = input("请输入商品名称:")
         goods_prise = float(input("请输入商品价格:"))
         goods_num = int(input("请输入商品数量:"))
         if goods_name not in shoping_cart:
             shoping_cart[goods_name] = {"price":goods_prise, "num":goods_num}
             print("商品添加完毕")
         else:
             print("您输入的商品已经存在")

    elif chose == "2":#修改
        goods_name = input("请输入要修改商品名称:")
        goods_prise = float(input("请输入商品最新价格:"))
        goods_num = int(input("请输入商品最新数量:"))
        if goods_name not in shoping_cart:
            print("您输入的商品名称有误")
        else:
            shoping_cart[goods_name] = {"price": goods_prise, "num": goods_num}
            print("商品修改完毕")
    elif chose == "3":#删除
        goods_name = input("输入您想删除的商品名称")
        if goods_name not in shoping_cart:
            print("非法操作")
        else:
            del shoping_cart[goods_name]
    elif chose == "4":
        if shoping_cart == {}:
            print("当前商品为空")
        for goods_name in shoping_cart.keys():
            shooping_all = shoping_cart[goods_name]
            print(f"商品名称为{goods_name}价格为{shooping_all['price']}商品数量{shooping_all['num']}")
    elif chose == "5":#退出
        print("已安全退出")
        break
    else:
        print("请输入有效操作")