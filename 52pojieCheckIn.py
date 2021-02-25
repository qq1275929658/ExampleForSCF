# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/SCU95403T3eaf2a3a591959dcb43c846277b9c9aa5ea3891ba3686.send?text=" + info + "&desp=" + specific,headers=headers)


def main(*args):
    headers={
        'Cookie': 'htVD_2132_saltkey=SF6t40QF; htVD_2132_lastvisit=1614262687; Hm_lvt_46d556462595ed05e05f009cdafff31a=1612321430,1614264069,1614264234,1614266285; htVD_2132_seccodecSAnrLXie=7394953.25bd0c1dc63b8fce23; htVD_2132_seccodecSAnrL=7394952.47676eb7cc96cdf6b2; htVD_2132_con_request_uri=https%3A%2F%2Fwww.52pojie.cn%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dhttps%253A%252F%252Fwww.52pojie.cn%252Fhome.php%253Fmod%253Dspace%2526username%253DReheart; htVD_2132_client_created=1614266298; htVD_2132_client_token=8BB04BB6A4EDAA6DB5E0AEF3856D2D12; htVD_2132_ulastactivity=1614266298%7C0; htVD_2132_auth=95542ax2eIo%2FGJSITgsHBoMgJxM183pVdd6p6%2BDAXyyCmqUT6hnNSP9ENlflxnZT7ZFOe6ylF88w8izgtzWWb20yopM%2B; htVD_2132_connect_login=1; htVD_2132_connect_is_bind=1; htVD_2132_connect_uin=8BB04BB6A4EDAA6DB5E0AEF3856D2D12; htVD_2132_stats_qc_login=3; htVD_2132_sid=0; htVD_2132_checkpm=1; htVD_2132_lastcheckfeed=1591656%7C1614266299; htVD_2132_checkfollow=1; htVD_2132_lastact=1614266300%09home.php%09space; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1614266298' ,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()
