import  requests
import time
import os

class GetYZM:
    def __init__(self):
        self.http=requests.Session()
        self.http.headers.update(
            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            ,"Referer":"https://lgn.yy.com/lgn/oauth/authorize.do?oauth_token=1e86b5a19494b7135b6e80cb255de86ec80ebc3c05ef144cb5a878c995eb91f9061f546fd6753f094a4af8e6e9205c23&denyCallbackURL=http://vip.yy.com/service/web/auth/fail&UIStyle=xqlogin&rdm=0.3950091572117025"
            ,"Accept":"image/webp,image/*,*/*;q=0.8"
            ,"Accept-Language": "zh-CN,zh;q=0.8,ko;q=0.6,zh-TW;q=0.4"
            
            }
        )
        self.cookies='hiido_ui=0.46785925464965605; hd_newui=0.4318241186668985; Hm_lvt_c493393610cdccbddc1f124d567e36ab=1468983462,1470533704,1470533846; LGNJSESSIONID=c5ea333be3b2f2942fc7956f33b803bbefbb8c37; token=aug3_3vvt8h0:3xv5vyyzu3v3v38vxy337v:21u427904524u7x9799656684'
        self.http.headers.update({'Cookie':self.cookies})
        #self.http.proxies= {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080'}  #用于调试
        self.imgpath=os.path.join(os.getcwd(),'imgs')
        if(os.path.exists(self.imgpath)==False):
            os.mkdir(self.imgpath)
    def get(self,num):
        f_idx=0
        for i in range(num):
            print('%d/%d' % (i+1,num))
            res=self.http.get("https://lgn.yy.com/verify/x2/getsvcode.do?appid=5034&username=dsfawefasdfawfawef&_ts=%d" % int(time.time()*1000)
                ,verify=False)
            imgname=os.path.join(self.imgpath,'%d.png' % f_idx)
            while(os.path.isfile(imgname)):
                f_idx+=1
                imgname=os.path.join(self.imgpath,'%d.png' % f_idx)
            f=open(imgname,'wb')
            f.write(res.content)
            f.close()
            f_idx+=1

if __name__=="__main__":   
    obj=GetYZM()
    obj.get(10000)