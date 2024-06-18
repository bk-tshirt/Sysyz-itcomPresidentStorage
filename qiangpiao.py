import os,time,pickle
from time import sleep
from selenium import webdriver
damai_url="https://www.damai.cn/"
login_url="https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F",
target_url='https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.591b23e112KF7G&id=727372741693'
class concert:
    def __init__(self):
        self.status=0
        self.login_method=1
        self.driver=webdriver.Firefox(service='geckodriver.exe')


    def set_cookie(self):
        self.driver.get(damai_url)
        print('###点击登录###')
        while self.driver.title.find('大麦网-全球演出赛事官方购票平台')!=-1:
            sleep(1)
        print("###请扫码登陆###")

        while self.driver.title!='大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
            sleep(1)
        print("###扫码成功###")
        pickle.dump(self.driver.get_cookies(),open("cookies.pkl","wb"))
        print("###Cooik保存成功###")
        self.driver.get(target_url)
    

    def get_cookie(self):
        try:
            cookies=pickle.load(open("cookies.pkl","rb"))
            for cookie in cookies:
                cookie_dict={
                    'domain':'.damai.cn',
                    'name':cookie.get('name'),
                    'value':cookie.get('value')
                }
                self.driver.add_cookie(cookie_dict)
            print("###载入模块###")

        except Exception as d:
            print(d)


    def login(self):
        if self.login_method==0:
            self.driver.get(login_url)
            print("###开始登陆###")
        elif self.login_method==1:
            if not os.path.exists("cookies.pkl"):
                self.get_cookie()
            else:
                self.driver.get(target_url)
                self.get_cookie()
    
    def enter_concert(self):
        print("###打开浏览器，进入大麦网###")
        self.login()
        self.driver.refresh()
        self.status=2
        print("###登陆成功###")
        if self.isElementExist('/html/body/div[2]/div[2]/div/div/div[3]/div[2]'):
            self.driver.find_element('/html/body/div[2]/div[2]/div/div/div[3]/div[2]').click()

    def isElementExist(self,element):
        flag=True
        brower=self.driver
        try:
            brower.find_element(element)
            return flag
        except:
            flag=False
            return flag        
    
    def choose_ticket(self):
        if self.status==2:
            print("="*30)
            print("###开始日期和票价选择###")
            while self.driver.title.find('确认订单')==-1:
                try:
                    buybutton=self.driver.find_element('buybtn').text
                    if buybutton=="提交缺货登记":
                        self.status=2
                        self.driver.get(target_url)
                        print('###抢票还未开始，请刷新等待###')
                        continue
                    elif buybutton=='立即预定':
                        self.driver.find_element('buybtn').click()
                        self.status=3
                    elif buybutton=='立即购买':
                        self.driver.find_element('buybtn').click()
                        self.status=4
                    elif buybutton=='选座购买':
                        self.driver.find_element('buybtn').click()
                        self.status=5
                except:
                    print('###未跳转到订单结算页面###')
                title=self.driver.title
                if title=='选座购买':
                    self.choice_seats()
                elif title=='确认订单':
                    while True:
                        print('waiting.......')
                        if self.isElementExist('//[@id="containter"]/div/div[9]/button'):
                            self.check_order()
                            break

    def check_order(self):
        if self.status in [3,4,5]:
            print('###开始确认订单')
            try:
                self.driver.find_element().click()
            except Exception as e:
                print("###购票人信息选中失败，请查看元素位置")
                time.sleep(0.7)
                self.driver.find_element('//div[@class="w1200"]//div[2]//div//div[9]//button[1]').click()



    def choice_seats(self):
        while self.driver.title=='选座购买':
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img'):
                print('请快速选择你的座位。。')
                while self.isElementExist('*[@id="app"]/div[2]/div[2]/div[2]/div'):
                    self.driver.find_element('//*[@id="app"]/div[2]/div[2]/div[2]/button').click()
    

    def finish(self):
        self.driver.quit()


if __name__=='__main__':
    try:
        con=concert
        con.enter_concert(None)
        con.choose_ticket(None)
    
        
    except Exception as e:
        print(e)
        con.finish()
        
        #练习
        