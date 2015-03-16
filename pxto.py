#-*- coding:utf-8 -*-

import requests
import sys
import json
import time

ExpressList={	'ems':'EMS',
				'shentong':'申通快递',
				'shunfeng':'顺丰速运',
				'yuantong':'圆通速递',
				'yunda':'韵达快运',
				'zhongtong':'中通快递',
				'huitongkuaidi':'汇通快运',
				'tiantian':'天天快递',
				'zhaijisong':'宅急送',
				'youzhengguonei':'邮政国内包裹',
				'youzhengguoji':'邮政国际包裹',
				'emsguoji':'EMS国际快递',
				'aae':'AAE-中国',
				'anjiekuaidi':'安捷快递',
				'anxindakuaixi':'安信达',
				'youzhengguonei':'包裹/平邮/挂号信',
				'bht':'BHT国际快递',
				'baifudongfang':'百福东方',
				'cces':'CCES（希伊艾斯）',
				'lijisong':'成都立即送',
				'dhl':'DHL',
				'dhlde':'DHL德国',
				'dsukuaidi':'D速物流',
				'debangwuliu':'德邦物流',
				'datianwuliu':'大田物流',
				'dpex':'DPEX',
				'disifang':'递四方',
				'ems':'EMS - 国内',
				'emsguoji':'EMS - 国际',
				'ems':'E邮宝',
				'rufengda':'凡客',
				'fedexus':'FedEx - 美国',
				'fedex':'FedEx - 国际',
				'lianbangkuaidi':'FedEx - 国内',
				'feikangda':'飞康达',
				'youzhengguonei':'挂号信',
				'ganzhongnengda':'能达速递',
				'gongsuda':'共速达',
				'gls':'GLS',
				'tiantian':'海航天天',
				'huitongkuaidi':'汇通快运',
				'tiandihuayu':'华宇物流',
				'hengluwuliu':'恒路物流',
				'haiwaihuanqiu':'海外环球',
				'huaxialongwuliu':'华夏龙',
				'jiajiwuliu':'佳吉快运',
				'jialidatong':'嘉里大通',
				'jiayiwuliu':'佳怡物流',
				'jinguangsudikuaijian':'京广速递',
				'jindawuliu':'金大物流',
				'jinyuekuaidi':'晋越快递',
				'jixianda':'急先达',
				'jiayunmeiwuliu':'加运美',
				'kuaijiesudi':'快捷速递',
				'lianbangkuaidi':'联邦快递',
				'longbanwuliu':'龙邦速递',
				'lanbiaokuaidi':'蓝镖快递',
				'lijisong':'立即送',
				'lejiedi':'乐捷递',
				'lianhaowuliu':'联昊通',
				'minghangkuaidi':'民航快递',
				'meiguokuaidi':'美国快递',
				'menduimen':'门对门',
				'ocs':'OCS',
				'quanfengkuaidi':'全峰快递',
				'quanyikuaidi':'全一快递',
				'quanchenkuaidi':'全晨快递',
				'quanjitong':'全际通',
				'quanritongkuaidi':'全日通',
				'rufengda':'如风达',
				'shentong':'申通E物流',
				'shentong':'申通快递',
				'shunfeng':'顺丰速运',
				'suer':'速尔快递',
				'shenghuiwuliu':'盛辉物流',
				'shengfengwuliu':'盛丰物流',
				'shangda':'上大国际',
				'santaisudi':'三态速递',
				'haihongwangsong':'山东海红',
				'saiaodi':'赛澳递',
				'tnt':'TNT',
				'tiantian':'天天快递',
				'tiandihuayu':'天地华宇',
				'tonghetianxia':'通和天下',
				'ups':'UPS',
				'usps':'USPS（美国邮政）',
				'wanjiawuliu':'万家物流',
				'wanxiangwuliu':'万象物流',
				'weitepai':'微特派',
				'xinhongyukuaidi':'鑫飞鸿',
				'xinbangwuliu':'新邦物流',
				'xinfengwuliu':'信丰物流',
				'cces':'希伊艾斯（CCES）',
				'yuantong':'圆通速递',
				'yunda':'韵达快运',
				'youzhengguonei':'邮政国内包裹',
				'youzhengguoji':'邮政国际包裹',
				'ems':'邮政特快专递',
				'yuanchengwuliu':'远成物流',
				'yafengsudi':'亚风速递',
				'yuanweifeng':'源伟丰',
				'youshuwuliu':'优速快递',
				'yuanzhijiecheng':'元智捷诚',
				'yuefengwuliu':'越丰物流',
				'yuananda':'源安达',
				'yuanfeihangwuliu':'原飞航',
				'yinjiesudi':'银捷速递',
				'yuntongkuaidi':'运通中港',
				'zhaijisong':'宅急送',
				'zhongtong':'中通快递',
				'zhongtiewuliu':'中铁快运',
				'ztky':'中铁物流',
				'zhongyouwuliu':'中邮物流',
				'zhimakaimen':'芝麻开门',
				'zhongxinda':'忠信达',
				'zhengzhoujianhua':'郑州建华'	}

'''
MakeExpress={	'ems':'ems',
				'shentong':'shentong',
				'申通快递':'shentong',
				'申通':'shentong',
				'st':'shentong',
				'sto':'shentong',
				'顺丰速运':'shunfeng',
				'顺丰':'shunfeng',
				'shunfeng':'shunfeng',
				'sf':'shunfeng',
				'圆通速递':'yuantong',
				'圆通':'yuantong',
				'yt':'yuantong',
				'yto':'yuantong',
				'yuantong':'yuantong',
				'韵达快运':'yunda',
				'yunda':'yunda',
				'韵达':'yunda',
				'yd':'yunda',
				'中通快递':'zhongtong',
				'中通':'zhongtong',
				'zhongtong':'zhongtong',
				'zto':'zhongtong',
				'zt':'zhongtong',
				'汇通快运':'huitongkuaidi',
				'汇通':'huitongkuaidi',
				'汇通快运':'huitongkuaidi',
				'huitong':'huitongkuaidi',
				'huitongkuaidi':'huitongkuaidi',
				'天天快递':'tiantian',
				'天天':'tiantian',
				'tiantian':'tiantian',
				'tt':'tiantian',
				'宅急送':'zhaijisong',
				'zhaijisong':'zhaijisong',
				'zjs':'zhaijisong',
				'邮政国内包裹':'youzhengguonei',
				'youzhengguonei':'youzhengguonei',
				'邮政':'youzhengguonei',
				'youzheng':'youzhengguonei',
				'yz':'youzhengguonei',
				'邮政国际包裹':'youzhengguoji',
				'youzhengguoji':'youzhengguoji',
				'邮政国际':'youzhengguoji',
				'EMS国际快递':'emsguoji',
				'emsguoji':'emsguoji',
				'AAE-中国':'aae',
				'安捷快递':'anjiekuaidi',
				'安信达':'anxindakuaixi',
				'包裹/平邮/挂号信':'youzhengguonei',
				'BHT国际快递':'bht',
				'百福东方':'baifudongfang',
				'CCES（希伊艾斯）':'cces',
				'成都立即送':'lijisong',
				'DHL':'dhl',
				'DHL德国':'dhlde',
				'D速物流':'dsukuaidi',
				'德邦物流':'debangwuliu',
				'大田物流':'datianwuliu',
				'DPEX':'dpex',
				'递四方':'disifang',
				'EMS - 国内':'ems',
				'EMS - 国际':'emsguoji',
				'E邮宝':'ems',
				'凡客':'rufengda',
				'FedEx - 美国':'fedexus',
				'FedEx - 国际':'fedex',
				'FedEx - 国内':'lianbangkuaidi',
				'飞康达':'feikangda',
				'挂号信':'youzhengguonei',
				'能达速递':'ganzhongnengda',
				'共速达':'gongsuda',
				'GLS':'gls',
				'海航天天':'tiantian',
				'汇通快运':'huitongkuaidi',
				'华宇物流':'tiandihuayu',
				'恒路物流':'hengluwuliu',
				'海外环球':'haiwaihuanqiu',
				'华夏龙':'huaxialongwuliu',
				'佳吉快运':'jiajiwuliu',
				'嘉里大通':'jialidatong',
				'佳怡物流':'jiayiwuliu',
				'京广速递':'jinguangsudikuaijian',
				'金大物流':'jindawuliu',
				'晋越快递':'jinyuekuaidi',
				'急先达':'jixianda',
				'加运美':'jiayunmeiwuliu',
				'快捷速递':'kuaijiesudi',
				'联邦快递':'lianbangkuaidi',
				'龙邦速递':'longbanwuliu',
				'蓝镖快递':'lanbiaokuaidi',
				'立即送':'lijisong',
				'乐捷递':'lejiedi',
				'联昊通':'lianhaowuliu',
				'民航快递':'minghangkuaidi',
				'美国快递':'meiguokuaidi',
				'门对门':'menduimen',
				'OCS':'ocs',
				'全峰快递':'quanfengkuaidi',
				'全一快递':'quanyikuaidi',
				'全晨快递':'quanchenkuaidi',
				'全际通':'quanjitong',
				'全日通':'quanritongkuaidi',
				'如风达':'rufengda',
				'申通E物流':'shentong',
				'申通快递':'shentong',
				'顺丰速运':'shunfeng',
				'速尔快递':'suer',
				'盛辉物流':'shenghuiwuliu',
				'盛丰物流':'shengfengwuliu',
				'上大国际':'shangda',
				'三态速递':'santaisudi',
				'山东海红':'haihongwangsong',
				'赛澳递':'saiaodi',
				'TNT':'tnt',
				'天天快递':'tiantian',
				'天地华宇':'tiandihuayu',
				'通和天下':'tonghetianxia',
				'UPS':'ups',
				'USPS（美国邮政）':'usps',
				'万家物流':'wanjiawuliu',
				'万象物流':'wanxiangwuliu',
				'微特派':'weitepai',
				'鑫飞鸿':'xinhongyukuaidi',
				'新邦物流':'xinbangwuliu',
				'信丰物流':'xinfengwuliu',
				'希伊艾斯（CCES）':'cces',
				'圆通速递':'yuantong',
				'韵达快运':'yunda',
				'邮政国内包裹':'youzhengguonei',
				'邮政国际包裹':'youzhengguoji',
				'邮政特快专递':'ems',
				'远成物流':'yuanchengwuliu',
				'亚风速递':'yafengsudi',
				'源伟丰':'yuanweifeng',
				'优速快递':'youshuwuliu',
				'元智捷诚':'yuanzhijiecheng',
				'越丰物流':'yuefengwuliu',
				'源安达':'yuananda',
				'原飞航':'yuanfeihangwuliu',
				'银捷速递':'yinjiesudi',
				'运通中港':'yuntongkuaidi',
				'宅急送':'zhaijisong',
				'中通快递':'zhongtong',
				'中铁快运':'zhongtiewuliu',
				'中铁物流':'ztky',
				'中邮物流':'zhongyouwuliu',
				'芝麻开门':'zhimakaimen',
				'忠信达':'zhongxinda',
				'郑州建华':'zhengzhoujianhua'	}
'''

UrlBase0='http://www.kuaidi100.com/query?type='
UrlBase2='&postid='

'''
Status={	'0':'货物处于运输过程中...',
			'1':'货物已由快递公司揽收',
			'2':'货物交付过程出现了问题',
			'3':'货物已被收件人签收',
			'4':'货物退回, 发件人已确认',
			'5':'快递正在被派送中',
			'6':'货物正在被退回发件人的途中'	}
'''

Status={	'0':'运输中...',
			'1':'已揽收',
			'2':'疑难件',
			'3':'已签收',
			'4':'已退回',
			'5':'派送中',
			'6':'退回中'	}

def Now():
	Now=time.strftime('%Y-%m-%d %H:%M:%S')
	return Now

def GetCompany(track_number):    
    base_url='http://www.kuaidi100.com/autonumber/auto?num='
    url = "{0}{1}".format(base_url, track_number)
    request = requests.get(url)
    if request.status_code == 200:
        content = json.loads(request.content)
        return content[0]["comCode"]


def RunDirect(company, track_number):
    Request=requests.get(UrlBase0+company+UrlBase2+track_number)
    #print Request
    if Request.status_code==200:
        PJSON=json.loads(Request.content)
        #print PJSON
        status=PJSON.get('status',-1)
        if status==-1:
            print 'Unknown error!'
        else:
            if status=='200':
                #print ('快递公司: '+ExpressList.get(company).decode('utf8'))
                #print ('运 单 号: '+track_number).decode('utf8')
                #print ('状　　态: '+Status.get(PJSON.get('state','Unknown error!'),'Unknown error!')).decode('utf8')
                print ('快递公司: '+ExpressList.get(company))
                print ('运 单 号: '+track_number)
                print ('状　　态: '+Status.get(PJSON.get('state','Unknown error!'),'Unknown error!'))
                print '================================'
                for Item in PJSON.get('data',[{'time':Now(),'context':'Unknown error!'}]):
                    print '['+Item.get('time','Unknown error!')+']	'+Item.get('context','Unknown error!')
            else:
                #if status=='201':
                    #print status
                print '====================Error!===================='
                print PJSON.get('message','Unknown error!')
    #raw_input('Press Enter to exit')

if __name__=='__main__':
    if len(sys.argv) == 2:
        company = GetCompany(sys.argv[1])
        #print company
        if company:
            RunDirect(company, sys.argv[1])
        else:
            print "没有发现合适的快递公司名"
    elif len(sys.argv) == 3:    
	RunDirect(sys.argv[1], sys.argv[2])
    else:
        print """
        python pxto.py 快递单号 

        OR

        python pxto.py 快递公司拼音名  快递单号 
        """

