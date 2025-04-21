class product:
    def __init__(self,name,count,price,sell,state):
        self.name=name
        self.count=count
        self.price=price
        self.sell=sell
        self.state=state
    
    def display(self):
        state='没有该商品'
        if self.state==1:
            state='有该商品'
        return f'商品名称：{self.name},商品数量：{self.count},进货价格：{self.price},售价：{self.sell}'

class managesys:
    products=[]
    def init(self):
        self.products.append(product('沈星回棉花娃娃',520,52,131.4,1))
        self.products.append(product('沈星回立牌',520,1016,1314,1))
        self.products.append(product('星辰有信思念',1314,52,77,1))
    def menu(self):
        self.init()
        print('\"商品管理系统"\"菜单：')
        print('1.展示所有商品')
        print('2.增添商品')
        print('3.卖出商品')
        print('4.删除商品')
        print('5.统计利润')
        print('-1.退出系统')
        while(True):
            menu_item=int(input('请输入菜单编号: '))
            if menu_item==1:
                self.show_all_products()
            elif menu_item==2:
                self.add_products()
            elif menu_item==3:
                self.sell_products()
            elif menu_item==4:
                self.del_products()
            elif menu_item==5:
                self.count_products()
            elif menu_item==-1:
                print('欢迎搭档下次再来哦，再见~')
                break

    def show_all_products(self):
        for p in self.products:
           print(p.display())
    
    def add_products(self):
        product_name=input('请输入商品名称：')
        ret=self.check_products(product_name)
        if ret !=None:
            print(f'商品{ret}已经存在')
        else:
            product_count=int(input('请输入商品数量：'))
            product_price=float(input('请输入商品进价：'))
            product_sell=float(input('请输入商品售价：'))
            new_product=product(product_name,product_count,product_price,product_sell,state=1)
            self.products.append(new_product)
            print('添加成功')

    def sell_products(self):
        product_name=input("请输入想要的商品：")
        product_count=int(input("请输入卖出数量："))
        product=self.check_products(product_name)
        if product:
            if product.count>=product_count:
                fee=product.sell*product_count
                print(f'应支付{fee}元')
                while True:
                    pay=float(input('请输入支付金额：'))
                    if pay<fee:
                        print('金额不足')
                    else:
                        break
                if pay>=fee:
                    print(f'找零{pay-fee}元')
                    product.count-=product_count
                    print(f"卖出{product_name}{product_count}个")
            else:
        
                print("库存不足，无法卖出！")
        else:
            print('没有该商品')

    def del_products(self):
        product_name=input('请输入要删除的商品:')
        for i,product in enumerate(self.products):
            if product.name==product_name:
                del self.products[i]
                print('删除成功')
                break
        else:
            print('没有该商品')
            

    def count_products(self):
        money=0
        for p in self.products:
            money+=(p.sell-p.price)*p.count
        print(f'总利润为{money}元')

    def check_products(self,name):
        for p in self.products:
            if p.name==name:
                return p
        else:
                return None

if __name__=='__main__':
    m=managesys()
    m.menu()
