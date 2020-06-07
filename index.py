#-*- coding: UTF-8 -*-

# 主程式
# SESSION 插件
import os
import json
# MVC 插件
from flask import Flask, render_template ,redirect,request,url_for,session,Response
import math 

# 其他頁面插件
# import admin_cur as ac #管理插件
import data as dt      #資料插件

# 建立 MVC 及 SESSION KEY
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac333c-f0bf-11e5-9e39-d3b532c10a28'

# 設定全域變數(媽的老是跳錯)
val = {}
vsum = 0
test_dic = ""
# HAMYS = {}
# Age = {}
# Aum = {}
# Lum = {}
# Compo = {}

# 主首頁
@app.route("/")
def index():
	if 'act' in session:
		name = dt.get_name(session['act'])
		act = session['act']
		img = dt.get_img(session['act'])

		tags_l1=dt.tags_l1_list()
		tags_l2=dt.tags_l2_list()
		tags_list=dt.tags_list()
		if 'file' in session:
			test = dt.test_sql("",session['file'])
			total=dt.total("",session['file'])
			for x in session['file']:
				pass
		else:
			test = dt.test_sql("","")
			total=dt.total("","")

	    # test={}
	    # test2={}
	    # test2={'b':'a','c':'d'}
	    # test={'a':test2}

	    # col_type=getval((dt.tags_col_type(tags_list)).split(","),2)

	    # 設定全域變數
	    # global HAMYS , Age , Aum , Lum , Compo
	    # global  Age , Aum , Lum , Compo
	    # HAMYS = {}
	    # Age = {}
	    # Aum = {}
	    # Lum = {}
	    # Compo = {}

	    # HAMYS = getval(total['HAMYS_count'],1)
		HAMYS = getval(total['HAMYS_count'].split(","),2,total['total_count'])

	    # for i in range(len(total['HAMYS_count'])):
	    #     HAMYS[total['HAMYS_count'][i][0].split(":")[0]] = total['HAMYS_count'][i][0].split(":")[1]

	    # Age_all = total['Age_count'].split(",")

	    # for i in range(len(Age_all)):
	    #     Age[Age_all[i].split(":")[0]] = Age_all[i].split(":")[1]

		Age = getval(total['Age_count'].split(","),2,total['total_count'])

	    # Aum_all = total['Aum_count'].split(",")

	    # for i in range(len(Aum_all)):
	    #     Aum[Aum_all[i].split(":")[0]] = Aum_all[i].split(":")[1]

		Aum_sum = getsum(total['Aum_count'].split(","))
		Aum = getval(total['Aum_count'].split(","),2,Aum_sum)

	    # Lum_all = total['Lum_count'].split(",")

	    # for i in range(len(Lum_all)):
	    #     Lum[Lum_all[i].split(":")[0]] = Lum_all[i].split(":")[1]

		Lum_sum = getsum(total['Lum_count'].split(","))
		Lum = getval(total['Lum_count'].split(","),2,Lum_sum)

	    # Compo_all = total['Compo_count'].split(",")

	    # for i in range(len(Compo_all)):
	    #     Compo[Compo_all[i].split(":")[0]] = Compo_all[i].split(":")[1]

		Compo = getval(total['Compo_count'].split(","),2,total['total_count'])
		income = getval(total['income_count'].split(","),2,total['total_count'])
		nextBest = getval(total['nextBest_count'].split(","),2,0)
		dna = getval(total['dna_count'].split(","),2,total['total_count'])
		# dna = total['dna_count']

	    #3個圖用的假資料
	    # incomeAmount = {'REV_SAV':15093,'REV_FUND':12754,'REV_ETF':19327,'REV_BOND':81592,'REV_SI_SN':80647,'REV_OTH_INV':74970,'REV_INS_INV':24080,'REV_INS_SAV':97483,'REV_OTH_INS':81609,'REV_MTG':18773,'REV_LOAN':87599}
	    # incomePeople = {'REV_SAV':349,'REV_FUND':670,'REV_ETF':2940,'REV_BOND':519,'REV_SI_SN':682,'REV_OTH_INV':928,'REV_INS_INV':454,'REV_INS_SAV':768,'REV_OTH_INS':863,'REV_MTG':489,'REV_LOAN':836}
	    # nextBest = {'INS_INV_RES':322,'RSP_FUND_RES':577,'FUND_RES':228,'ETF_RES':649,'INS_RES':610,'AO_RES':741,'LN_RES':474}
	    # dna = {'PAR_FLG':830,   'BABY_FLG':659, 'HOUSEOWNER_FLG':177,   'MOBILEPAY_FLG':621,    'HIGHSPEEDRAILWAY_FLG':376, 'COMMUTING_FLG':112,    'NORTHDRIFT_FLG':583,   'LAZY_FLG':104, 'ONLINESHOPPING_FLG':855,   'CAROWNER_FLG':110, 'CROSSCOUNTRYTRAVEL_FLG':550,   'THREEC_FLG':172,   'INCOUNTRYTRAVEL_FLG':912,  'MUSIC_FLG':456,    'SHOPPING_FLG':837, 'TRAVEL_FLG':477,   'APPLE_FLG':789,    'BACKPACKING_FLG':206,  'OTAKU_FLG':855,    'EAT_FLG':62,   'SPORT_FLG':772,    'MOVIE_FLG':332,    'COFFEE_FLG':417,   'DIGITAL_FLG':982,  'NIGHT_FLG':388,    'JAPAN_FLG':446,    'KOREA_FLG':47, 'USA_FLG':440,  'CHINA_FLG':755,    'TECHNOLOGY_FLG':110,   'EUROPE_FLG':611}
		incomeAmount = {'REV_SAV':income['REV_SAV_sum']   , 'REV_FUND':income['REV_FUND_sum']   , 'REV_ETF':income['REV_ETF_sum']   , 'REV_BOND':income['REV_BOND_sum']   , 'REV_SI_SN':income['REV_SI_SN_sum']   , 'REV_OTH_INV':income['REV_OTH_INV_sum']   , 'REV_INS_INV':income['REV_INS_INV_sum']   , 'REV_INS_SAV':income['REV_INS_SAV_sum']   , 'REV_OTH_INS':income['REV_OTH_INS_sum']   , 'REV_MTG':income['REV_MTG_sum']   , 'REV_LOAN':income['REV_LOAN_sum']  }
		incomePeople = {'REV_SAV':income['REV_SAV_count'] , 'REV_FUND':income['REV_FUND_count'] , 'REV_ETF':income['REV_ETF_count'] , 'REV_BOND':income['REV_BOND_count'] , 'REV_SI_SN':income['REV_SI_SN_count'] , 'REV_OTH_INV':income['REV_OTH_INV_count'] , 'REV_INS_INV':income['REV_INS_INV_count'] , 'REV_INS_SAV':income['REV_INS_SAV_count'] , 'REV_OTH_INS':income['REV_OTH_INS_count'] , 'REV_MTG':income['REV_MTG_count'] , 'REV_LOAN':income['REV_LOAN_count']}
		nextBest = {'INS_INV_RES':nextBest['INS_INV_RES'],   'RSP_FUND_RES':nextBest['RSP_FUND_RES'], 'FUND_RES':nextBest['FUND_RES'],  'ETF_RES':nextBest['ETF_RES'],  'INS_RES':nextBest['INS_RES'],  'AO_RES':nextBest['AO_RES'],   'LN_RES':nextBest['LN_RES']}
		dna ={'PAR_FLG':dna['PAR_FLG'],    'BABY_FLG':dna['BABY_FLG'], 'HOUSEOWNER_FLG':dna['HOUSEOWNER_FLG'],   'MOBILEPAY_FLG':dna['MOBILEPAY_FLG'],    'HIGHSPEEDRAILWAY_FLG':dna['HIGHSPEEDRAILWAY_FLG'],  'COMMUTING_FLG':dna['COMMUTING_FLG'],    'NORTHDRIFT_FLG':dna['NORTHDRIFT_FLG'],   'LAZY_FLG':dna['LAZY_FLG'], 'ONLINESHOPPING_FLG':dna['ONLINESHOPPING_FLG'],   'CAROWNER_FLG':dna['CAROWNER_FLG'],  'CROSSCOUNTRYTRAVEL_FLG':dna['CROSSCOUNTRYTRAVEL_FLG'],   'THREEC_FLG':dna['THREEC_FLG'],   'INCOUNTRYTRAVEL_FLG':dna['INCOUNTRYTRAVEL_FLG'],   'MUSIC_FLG':dna['MUSIC_FLG'],    'SHOPPING_FLG':dna['SHOPPING_FLG'], 'TRAVEL_FLG':dna['TRAVEL_FLG'],    'APPLE_FLG':dna['APPLE_FLG'],    'BACKPACKING_FLG':dna['BACKPACKING_FLG'], 'OTAKU_FLG':dna['OTAKU_FLG'],    'EAT_FLG':dna['EAT_FLG'],  'SPORT_FLG':dna['SPORT_FLG'],    'MOVIE_FLG':dna['MOVIE_FLG'],    'COFFEE_FLG':dna['COFFEE_FLG'],   'DIGITAL_FLG':dna['DIGITAL_FLG'],  'NIGHT_FLG':dna['NIGHT_FLG'],    'JAPAN_FLG':dna['JAPAN_FLG'],    'KOREA_FLG':dna['KOREA_FLG'],    'USA_FLG':dna['USA_FLG'],  'CHINA_FLG':dna['CHINA_FLG'],    'TECHNOLOGY_FLG':dna['TECHNOLOGY_FLG'],   'EUROPE_FLG':dna['EUROPE_FLG']}
		# dna={'dna',dna}
		Score = {'s1':7.96,	's2':5.55,	's3':12.33,	's4':10.37,	's5':12.58,	's6':9.87,	's7':9.31,	's8':1.83,	's9':5.27,	's10':5.47,	's11':7.54,	's12':11.93}
		creditCard = {'MCC_A01_FLG':68.39,	'MCC_A02_FLG':94.09,	'MCC_B_FLG':81.86,	'MCC_C_FLG':98.18,	'MCC_C01_FLG':39.67,	'MCC_D_FLG':11.46,	'MCC_E01_FLG':57.15,	'MCC_E02_FLG':73.08,	'MCC_E03_FLG':52.92,	'MCC_F01_FLG':31.92,	'MCC_F02_FLG':9.37,	'MCC_F03_FLG':98.69,	'MCC_H01_FLG':36.21,	'MCC_H02_FLG':17.67,	'MCC_I_FLG':94.63,	'MCC_J_FLG':71.87,	'MCC_L01_FLG':13.06,	'MCC_M_FLG':12.7}
		othBank = {'othBank_1':4.12,	'othBank_1_3':24.12,	'othBank_3_15':12.16,	'othBank_15_30':42.23,	'othBank_30':17.36}

		#將第一次算完的全行客戶基準
		#於session塞八個dictionary物件 用於八張圖表的呈現
		#if session.get() == True  => 記得加入session是否已存在物件 避免過度每進首頁都撈DB
		# session['total'] = format(total['total_count'],',')
		session['total'] = total['total_count']
		# session['totalHAMYS'] = {'H':100,'A':200,'M':150,'Y':123,'S':93}
		session['totalHAMYS'] = {'H':HAMYS['H'],'A':HAMYS['A'],'M':HAMYS['M'],'Y':HAMYS['Y']}
		# session['totalAge'] = {'20':200,'35':300,'50':500,'60':300,'70':123,'80':70,'120':40}
		session['totalAge'] = {'19':Age['AGE_CNT_19'],'29':Age['AGE_CNT_20_29'],'39':Age['AGE_CNT_30_39'],'49':Age['AGE_CNT_40_49'],'59':Age['AGE_CNT_50_59'],'69':Age['AGE_CNT_60_69'],'79':Age['AGE_CNT_70_79'],'80':Age['AGE_CNT_80']}
		# session['totalAum'] = {'twd':20,'fx':35,'invest':15,'insure':30}
		session['totalAum'] = {'AUM_PO_AMT':Aum['AUM_PO_AMT'],'AUM_SAVE_AMT':Aum['AUM_SAVE_AMT'],'AUM_INVEST_AMT':Aum['AUM_INVEST_AMT']}
		# session['totalLum'] = {'credit':37,'mortgage':63}
		#session['totalLum'] = {'LN01_M0_AMT':Lum['LN01_M0_AMT'],'LN02_M0_AMT':Lum['LN02_M0_AMT']}
		session['score'] = {'s1':Score['s1'],'s2':Score['s2'],'s3':Score['s3'],'s4':Score['s4'],'s5':Score['s5'],'s6':Score['s6'],'s7':Score['s7'],'s8':Score['s8'],'s9':Score['s9'],'s10':Score['s10'],'s11':Score['s11'],'s12':Score['s12']}
		session['creditCard'] = {'MCC_A01_FLG':creditCard['MCC_A01_FLG'],	'MCC_A02_FLG':creditCard['MCC_A02_FLG'],	'MCC_B_FLG':creditCard['MCC_B_FLG'],	'MCC_C_FLG':creditCard['MCC_C_FLG'],	'MCC_C01_FLG':creditCard['MCC_C01_FLG'],	'MCC_D_FLG':creditCard['MCC_D_FLG'],	'MCC_E01_FLG':creditCard['MCC_E01_FLG'],	'MCC_E02_FLG':creditCard['MCC_E02_FLG'],	'MCC_E03_FLG':creditCard['MCC_E03_FLG'],	'MCC_F01_FLG':creditCard['MCC_F01_FLG'],	'MCC_F02_FLG':creditCard['MCC_F02_FLG'],	'MCC_F03_FLG':creditCard['MCC_F03_FLG'],	'MCC_H01_FLG':creditCard['MCC_H01_FLG'],	'MCC_H02_FLG':creditCard['MCC_H02_FLG'],	'MCC_I_FLG':creditCard['MCC_I_FLG'],	'MCC_J_FLG':creditCard['MCC_J_FLG'],	'MCC_L01_FLG':creditCard['MCC_L01_FLG'],	'MCC_M_FLG':creditCard['MCC_M_FLG']}
		session['othBank'] = {'othBank_1':othBank['othBank_1'],	'othBank_1_3':othBank['othBank_1_3'],	'othBank_3_15':othBank['othBank_3_15'],	'othBank_15_30':othBank['othBank_15_30'],	'othBank_30':othBank['othBank_30']}

		# session['totalCompo'] = {'CC_FLG':40,'EB_MB_ACTIVE':60,'HA':40,'BRANCH':94,'SALARY_FLG':50,'SEC_ACCT_FLG':40,'STOCK_INT_2Y_FLG':43,'OTHBANK_HIGHT':34,'OTHBANK_TOP':60}
		# session['totalCompo'] = {'CC_FLG':Compo['CC_FLG'],'EB_MB_ACTIVE':Compo['EB_MB_ACTIVE'],'HA':Compo['HA'],'BRANCH':Compo['BRANCH'],'SALARY_FLG':Compo['SALARY_FLG'],'SEC_ACCT_FLG':Compo['SEC_ACCT_FLG'],'STOCK_INT_2Y_FLG':Compo['STOCK_INT_2Y_FLG'],'OTHBANK_HIGHT':Compo['OTHBANK_HIGHT'],'OTHBANK_TOP':Compo['OTHBANK_TOP']}
		session['totalCompo'] = {'SALARY_FLG':Compo['SALARY_FLG'],'SEC_ACCT_FLG':Compo['SEC_ACCT_FLG'],'EB_MB_ACTIVE':Compo['EB_MB_ACTIVE'],'EMPLOYEE':Compo['EMPLOYEE'],'lineoa':Compo['lineoa'],'CC_FLG':Compo['CC_FLG']}
		# return render_template("index.html",tags_f=tags_f,tags_list=tags_list,col_type=col_type,test="ttt")

	    #收益分布    有兩個 一個是總金額  一個是人數
		session['incomeAmount'] = {'REV_SAV':incomeAmount['REV_SAV'],'REV_FUND':incomeAmount['REV_FUND'],'REV_ETF':incomeAmount['REV_ETF'],'REV_BOND':incomeAmount['REV_BOND'],'REV_SI_SN':incomeAmount['REV_SI_SN'],'REV_OTH_INV':incomeAmount['REV_OTH_INV'],'REV_INS_INV':incomeAmount['REV_INS_INV'],'REV_INS_SAV':incomeAmount['REV_INS_SAV'],'REV_OTH_INS':incomeAmount['REV_OTH_INS'],'REV_MTG':incomeAmount['REV_MTG'],'REV_LOAN':incomeAmount['REV_LOAN']}
		session['incomePeople'] = {'REV_SAV':incomePeople['REV_SAV'],'REV_FUND':incomePeople['REV_FUND'],'REV_ETF':incomePeople['REV_ETF'],'REV_BOND':incomePeople['REV_BOND'],'REV_SI_SN':incomePeople['REV_SI_SN'],'REV_OTH_INV':incomePeople['REV_OTH_INV'],'REV_INS_INV':incomePeople['REV_INS_INV'],'REV_INS_SAV':incomePeople['REV_INS_SAV'],'REV_OTH_INS':incomePeople['REV_OTH_INS'],'REV_MTG':incomePeople['REV_MTG'],'REV_LOAN':incomePeople['REV_LOAN']}

		#NextBestOffer
		session['nextBest'] = {'INS_INV_RES':nextBest['INS_INV_RES'],'RSP_FUND_RES':nextBest['RSP_FUND_RES'],'FUND_RES':nextBest['FUND_RES'],'ETF_RES':nextBest['ETF_RES'],'INS_RES':nextBest['INS_RES'],'AO_RES':nextBest['AO_RES'],'LN_RES':nextBest['LN_RES']}

		#客戶DNA
		session['dna'] = {'PAR_FLG':dna['PAR_FLG'],'BABY_FLG':dna['BABY_FLG'],'HOUSEOWNER_FLG':dna['HOUSEOWNER_FLG'],'MOBILEPAY_FLG':dna['MOBILEPAY_FLG'],'HIGHSPEEDRAILWAY_FLG':dna['HIGHSPEEDRAILWAY_FLG'],   'COMMUTING_FLG':dna['COMMUTING_FLG'],   'NORTHDRIFT_FLG':dna['NORTHDRIFT_FLG'], 'LAZY_FLG':dna['LAZY_FLG'], 'ONLINESHOPPING_FLG':dna['ONLINESHOPPING_FLG'], 'CAROWNER_FLG':dna['CAROWNER_FLG'], 'CROSSCOUNTRYTRAVEL_FLG':dna['CROSSCOUNTRYTRAVEL_FLG'], 'THREEC_FLG':dna['THREEC_FLG'], 'INCOUNTRYTRAVEL_FLG':dna['INCOUNTRYTRAVEL_FLG'],'MUSIC_FLG':dna['MUSIC_FLG'],'SHOPPING_FLG':dna['SHOPPING_FLG'],'TRAVEL_FLG':dna['TRAVEL_FLG'],'APPLE_FLG':dna['APPLE_FLG'],   'BACKPACKING_FLG':dna['BACKPACKING_FLG'],   'OTAKU_FLG':dna['OTAKU_FLG'],   'EAT_FLG':dna['EAT_FLG'],   'SPORT_FLG':dna['SPORT_FLG'],   'MOVIE_FLG':dna['MOVIE_FLG'],   'COFFEE_FLG':dna['COFFEE_FLG'], 'DIGITAL_FLG':dna['DIGITAL_FLG'],   'NIGHT_FLG':dna['NIGHT_FLG'],   'JAPAN_FLG':dna['JAPAN_FLG'],   'KOREA_FLG':dna['KOREA_FLG'],'USA_FLG':dna['USA_FLG'],'CHINA_FLG':dna['CHINA_FLG'],'TECHNOLOGY_FLG':dna['TECHNOLOGY_FLG'],'EUROPE_FLG':dna['EUROPE_FLG']}
		# session['dna'] = {'dna':dna}

		return render_template("index.html",tags_l1=tags_l1,tags_l2=tags_l2,tags_list=tags_list,act=act,name=name,img=img,test=test)
	else:
		return redirect(url_for("logout"))

# 取得目標客戶  這是讓user打ajax過來取資料的API
@app.route("/targetCust" , methods=["POST"])
def targetCust():
	if 'file' in session:
		test = dt.test_sql(request.form['data'],session['file'])
		target=dt.total(request.form['data'],session['file'])
	else:
		test = dt.test_sql(request.form['data'],"")
		target=dt.total(request.form['data'],"")

	percent = target['total_count'] / session['total'] * 100

	if target['total_count'] == 0:
		HAMYS = getval(target['HAMYS_count'].split(","),2,0)
		Age = getval(target['Age_count'].split(","),2,0)
		Aum = getval(target['Aum_count'].split(","),2,0)
		Lum = getval(target['Lum_count'].split(","),2,0)
		Compo = getval(target['Compo_count'].split(","),2,0)
		income = getval(target['income_count'].split(","),2,0)
		nextBest = getval(target['nextBest_count'].split(","),2,0)
		dna = getval(target['dna_count'].split(","),2,0)
	else:
		HAMYS = getval(target['HAMYS_count'].split(","),2,target['total_count'])
		Age = getval(target['Age_count'].split(","),2,target['total_count'])
		Aum_sum = getsum(target['Aum_count'].split(","))
		Aum = getval(target['Aum_count'].split(","),2,Aum_sum)
		Lum_sum = getsum(target['Lum_count'].split(","))
		Lum = getval(target['Lum_count'].split(","),2,Lum_sum)
		Compo = getval(target['Compo_count'].split(","),2,target['total_count'])
		income = getval(target['income_count'].split(","),2,target['total_count'])
		nextBest = getval(target['nextBest_count'].split(","),2,0)
		dna = getval(target['dna_count'].split(","),2,target['total_count'])

	# dna = target['dna_count']

    #三張圖的假資料
    # incomeAmount = {'REV_SAV':50962,    'REV_FUND':75474,   'REV_ETF':16821,    'REV_BOND':24225,   'REV_SI_SN':65901, 'REV_OTH_INV':87151,    'REV_INS_INV':11904,    'REV_INS_SAV':93024,    'REV_OTH_INS':13614,    'REV_MTG':35765,    'REV_LOAN':6500}
    # incomePeople = {'REV_SAV':281,  'REV_FUND':231, 'REV_ETF':797,  'REV_BOND':322, 'REV_SI_SN':712,   'REV_OTH_INV':2000, 'REV_INS_INV':93,   'REV_INS_SAV':380,  'REV_OTH_INS':471,  'REV_MTG':436,  'REV_LOAN':257}
    # nextBest = {'INS_INV_RES':57,   'RSP_FUND_RES':962, 'FUND_RES':77,  'ETF_RES':655,  'INS_RES':613,  'AO_RES':605,   'LN_RES':643}
    # dna ={'PAR_FLG':326,    'BABY_FLG':475, 'HOUSEOWNER_FLG':460,   'MOBILEPAY_FLG':150,    'HIGHSPEEDRAILWAY_FLG':50,  'COMMUTING_FLG':267,    'NORTHDRIFT_FLG':172,   'LAZY_FLG':730, 'ONLINESHOPPING_FLG':991,   'CAROWNER_FLG':65,  'CROSSCOUNTRYTRAVEL_FLG':363,   'THREEC_FLG':501,   'INCOUNTRYTRAVEL_FLG':25,   'MUSIC_FLG':649,    'SHOPPING_FLG':593, 'TRAVEL_FLG':64,    'APPLE_FLG':203,    'BACKPACKING_FLG':3000, 'OTAKU_FLG':862,    'EAT_FLG':932,  'SPORT_FLG':482,    'MOVIE_FLG':675,    'COFFEE_FLG':886,   'DIGITAL_FLG':651,  'NIGHT_FLG':251,    'JAPAN_FLG':393,    'KOREA_FLG':305,    'USA_FLG':917,  'CHINA_FLG':679,    'TECHNOLOGY_FLG':322,   'EUROPE_FLG':602}
    # nextBest = {'INS_INV_RES':120,'RSP_FUND_RES':212,'FUND_RES':300,'ETF_RES':1230,'INS_RES':120,'AO_RES':300,'INS_RES':400,'LN_RES':23}
	incomeAmount = {'REV_SAV':income['REV_SAV_sum']   , 'REV_FUND':income['REV_FUND_sum']   , 'REV_ETF':income['REV_ETF_sum']   , 'REV_BOND':income['REV_BOND_sum']   , 'REV_SI_SN':income['REV_SI_SN_sum']   , 'REV_OTH_INV':income['REV_OTH_INV_sum']   , 'REV_INS_INV':income['REV_INS_INV_sum']   , 'REV_INS_SAV':income['REV_INS_SAV_sum']   , 'REV_OTH_INS':income['REV_OTH_INS_sum']   , 'REV_MTG':income['REV_MTG_sum']   , 'REV_LOAN':income['REV_LOAN_sum']  }
	incomePeople = {'REV_SAV':income['REV_SAV_count'] , 'REV_FUND':income['REV_FUND_count'] , 'REV_ETF':income['REV_ETF_count'] , 'REV_BOND':income['REV_BOND_count'] , 'REV_SI_SN':income['REV_SI_SN_count'] , 'REV_OTH_INV':income['REV_OTH_INV_count'] , 'REV_INS_INV':income['REV_INS_INV_count'] , 'REV_INS_SAV':income['REV_INS_SAV_count'] , 'REV_OTH_INS':income['REV_OTH_INS_count'] , 'REV_MTG':income['REV_MTG_count'] , 'REV_LOAN':income['REV_LOAN_count']}
	nextBest = {'INS_INV_RES':nextBest['INS_INV_RES'],   'RSP_FUND_RES':nextBest['RSP_FUND_RES'], 'FUND_RES':nextBest['FUND_RES'],  'ETF_RES':nextBest['ETF_RES'],  'INS_RES':nextBest['INS_RES'],  'AO_RES':nextBest['AO_RES'],   'LN_RES':nextBest['LN_RES']}
	dna ={'PAR_FLG':dna['PAR_FLG'],    'BABY_FLG':dna['BABY_FLG'], 'HOUSEOWNER_FLG':dna['HOUSEOWNER_FLG'],   'MOBILEPAY_FLG':dna['MOBILEPAY_FLG'],    'HIGHSPEEDRAILWAY_FLG':dna['HIGHSPEEDRAILWAY_FLG'],  'COMMUTING_FLG':dna['COMMUTING_FLG'],    'NORTHDRIFT_FLG':dna['NORTHDRIFT_FLG'],   'LAZY_FLG':dna['LAZY_FLG'], 'ONLINESHOPPING_FLG':dna['ONLINESHOPPING_FLG'],   'CAROWNER_FLG':dna['CAROWNER_FLG'],  'CROSSCOUNTRYTRAVEL_FLG':dna['CROSSCOUNTRYTRAVEL_FLG'],   'THREEC_FLG':dna['THREEC_FLG'],   'INCOUNTRYTRAVEL_FLG':dna['INCOUNTRYTRAVEL_FLG'],   'MUSIC_FLG':dna['MUSIC_FLG'],    'SHOPPING_FLG':dna['SHOPPING_FLG'], 'TRAVEL_FLG':dna['TRAVEL_FLG'],    'APPLE_FLG':dna['APPLE_FLG'],    'BACKPACKING_FLG':dna['BACKPACKING_FLG'], 'OTAKU_FLG':dna['OTAKU_FLG'],    'EAT_FLG':dna['EAT_FLG'],  'SPORT_FLG':dna['SPORT_FLG'],    'MOVIE_FLG':dna['MOVIE_FLG'],    'COFFEE_FLG':dna['COFFEE_FLG'],   'DIGITAL_FLG':dna['DIGITAL_FLG'],  'NIGHT_FLG':dna['NIGHT_FLG'],    'JAPAN_FLG':dna['JAPAN_FLG'],    'KOREA_FLG':dna['KOREA_FLG'],    'USA_FLG':dna['USA_FLG'],  'CHINA_FLG':dna['CHINA_FLG'],    'TECHNOLOGY_FLG':dna['TECHNOLOGY_FLG'],   'EUROPE_FLG':dna['EUROPE_FLG']}
	Score ={'s1':1.29,	's2':2.88,	's3':17.52,	's4':18.07,	's5':13.76,	's6':10.12,	's7':4.99,	's8':8.87,	's9':5.25,	's10':10.9,	's11':2.77,	's12':3.59}
	creditCard = {'MCC_A01_FLG':51.41,	'MCC_A02_FLG':29.69,	'MCC_B_FLG':41.67,	'MCC_C_FLG':94.29,	'MCC_C01_FLG':85.36,	'MCC_D_FLG':45.69,	'MCC_E01_FLG':42.36,	'MCC_E02_FLG':1.02,	'MCC_E03_FLG':82.02,	'MCC_F01_FLG':86.13,	'MCC_F02_FLG':33.11,	'MCC_F03_FLG':58.7,	'MCC_H01_FLG':46.74,	'MCC_H02_FLG':25.53,	'MCC_I_FLG':29.27,	'MCC_J_FLG':89.36,	'MCC_L01_FLG':22.79,	'MCC_M_FLG':93.12}
	othBank = {'othBank_1':19.39,	'othBank_1_3':19.01,	'othBank_3_15':8.98,	'othBank_15_30':32.97,	'othBank_30':19.65}
    # session['test']=HAMYS["'H'"]

    # dna-test
	global test_dic
	test_dic = ""
	for i in range(len(test)):
		# test_dic = test[i][0] + "," + test[i][1] + "," + test[i][2] + "," + str(test[i][3])
		# test_dic[i] = test[i][0] + "," + test[i][1] + "," + test[i][2] + "," + str(test[i][3])
		test_dic = test_dic + test[i][0] + "," + test[i][1] + "," + test[i][2] + "," + str(test[i][3]) + ";"

    #以下請於targetCust塞八個dictionary物件 用於八張圖表的總目標客戶
	targetCust = {
	# target_total
	'target_total':{'number':format(target['total_count'],','),'percent':percent},
	# 'HAMYS':{'H':40,'A':100,'M':75,'Y':90,'S':70},
	# 'HAMYS':{'H':40,'A':100,'M':75,'Y':90},
	'HAMYS':{'H':HAMYS['H'],'A':HAMYS['A'],'M':HAMYS['M'],'Y':HAMYS['Y']},
	# 'HAMYS':{'H':HAMYS["'H'"],'A':HAMYS["'A'"],'M':HAMYS["'M'"],'Y':HAMYS["'Y'"]},
	# 'age':{'20':60,'35':100,'50':130,'60':150,'70':100,'80':30,'120':20},
	# 'age':{'19':60,'29':100,'39':130,'49':150,'59':100,'69':30,'79':20,'80':22},
	'age':{'19':Age['AGE_CNT_19'],'29':Age['AGE_CNT_20_29'],'39':Age['AGE_CNT_30_39'],'49':Age['AGE_CNT_40_49'],'59':Age['AGE_CNT_50_59'],'69':Age['AGE_CNT_60_69'],'79':Age['AGE_CNT_70_79'],'80':Age['AGE_CNT_80']},
	# 'aum':{'twd':10,'fx':40,'invest':35,'insure':15},
	# 'aum':{'AUM_PO_AMT':9999999,'AUM_SAVE_AMT':888888,'AUM_INVEST_AMT':77777777},
	'aum':{'AUM_PO_AMT':Aum['AUM_PO_AMT'],'AUM_SAVE_AMT':Aum['AUM_SAVE_AMT'],'AUM_INVEST_AMT':Aum['AUM_INVEST_AMT']},
	# 'lum':{'credit':50,'mortgage':50},
	# 'lum':{'LN01_M0_AMT':500000,'LN02_M0_AMT':5066666},
	'lum':{'LN01_M0_AMT':Lum['LN01_M0_AMT'],'LN02_M0_AMT':Lum['LN02_M0_AMT']},
	# 'compo':{'CC_FLG':20,'EB_MB_ACTIVE':30,'HA':12,'BRANCH':34,'SALARY_FLG':10,'SEC_ACCT_FLG':20,'STOCK_INT_2Y_FLG':10,'OTHBANK_HIGHT':15,'OTHBANK_TOP':20}
	# 'compo':{'CC_FLG':Compo['CC_FLG'],'EB_MB_ACTIVE':Compo['EB_MB_ACTIVE'],'HA':Compo['HA'],'BRANCH':Compo['BRANCH'],'SALARY_FLG':Compo['SALARY_FLG'],'SEC_ACCT_FLG':Compo['SEC_ACCT_FLG'],'STOCK_INT_2Y_FLG':Compo['STOCK_INT_2Y_FLG'],'OTHBANK_HIGHT':Compo['OTHBANK_HIGHT'],'OTHBANK_TOP':Compo['OTHBANK_TOP']}
	'compo':{'CC_FLG':Compo['CC_FLG'],'EB_MB_ACTIVE':Compo['EB_MB_ACTIVE'],'HA':Compo['HA'],'BRANCH':Compo['BRANCH'],'SALARY_FLG':Compo['SALARY_FLG'],'SEC_ACCT_FLG':Compo['SEC_ACCT_FLG'],'STOCK_INT_2Y_FLG':Compo['STOCK_INT_2Y_FLG'],'OTHBANK_TOP':Compo['OTHBANK_TOP']},

	#收益分布
	'incomeAmount':{'REV_SAV':incomeAmount['REV_SAV'],'REV_FUND':incomeAmount['REV_FUND'],'REV_ETF':incomeAmount['REV_ETF'],'REV_BOND':incomeAmount['REV_BOND'],'REV_SI_SN':incomeAmount['REV_SI_SN'],'REV_OTH_INV':incomeAmount['REV_OTH_INV'],'REV_INS_INV':incomeAmount['REV_INS_INV'],'REV_INS_SAV':incomeAmount['REV_INS_SAV'],'REV_OTH_INS':incomeAmount['REV_OTH_INS'],'REV_MTG':incomeAmount['REV_MTG'],'REV_LOAN':incomeAmount['REV_LOAN']},
	'incomePeople':{'REV_SAV':incomePeople['REV_SAV'],'REV_FUND':incomePeople['REV_FUND'],'REV_ETF':incomePeople['REV_ETF'],'REV_BOND':incomePeople['REV_BOND'],'REV_SI_SN':incomePeople['REV_SI_SN'],'REV_OTH_INV':incomePeople['REV_OTH_INV'],'REV_INS_INV':incomePeople['REV_INS_INV'],'REV_INS_SAV':incomePeople['REV_INS_SAV'],'REV_OTH_INS':incomePeople['REV_OTH_INS'],'REV_MTG':incomePeople['REV_MTG'],'REV_LOAN':incomePeople['REV_LOAN']},

	#NextBestOffer
	'nextBest' : {'INS_INV_RES':nextBest['INS_INV_RES'],'RSP_FUND_RES':nextBest['RSP_FUND_RES'],'FUND_RES':nextBest['FUND_RES'],'ETF_RES':nextBest['ETF_RES'],'INS_RES':nextBest['INS_RES'],'AO_RES':nextBest['AO_RES'],'LN_RES':nextBest['LN_RES']},

	#DNA
	'dna':{'PAR_FLG':dna['PAR_FLG'],'BABY_FLG':dna['BABY_FLG'],'HOUSEOWNER_FLG':dna['HOUSEOWNER_FLG'],'MOBILEPAY_FLG':dna['MOBILEPAY_FLG'],'HIGHSPEEDRAILWAY_FLG':dna['HIGHSPEEDRAILWAY_FLG'],  'COMMUTING_FLG':dna['COMMUTING_FLG'],   'NORTHDRIFT_FLG':dna['NORTHDRIFT_FLG'], 'LAZY_FLG':dna['LAZY_FLG'], 'ONLINESHOPPING_FLG':dna['ONLINESHOPPING_FLG'], 'CAROWNER_FLG':dna['CAROWNER_FLG'], 'CROSSCOUNTRYTRAVEL_FLG':dna['CROSSCOUNTRYTRAVEL_FLG'], 'THREEC_FLG':dna['THREEC_FLG'], 'INCOUNTRYTRAVEL_FLG':dna['INCOUNTRYTRAVEL_FLG'],'MUSIC_FLG':dna['MUSIC_FLG'],'SHOPPING_FLG':dna['SHOPPING_FLG'],'TRAVEL_FLG':dna['TRAVEL_FLG'],'APPLE_FLG':dna['APPLE_FLG'],   'BACKPACKING_FLG':dna['BACKPACKING_FLG'],   'OTAKU_FLG':dna['OTAKU_FLG'],   'EAT_FLG':dna['EAT_FLG'],   'SPORT_FLG':dna['SPORT_FLG'],   'MOVIE_FLG':dna['MOVIE_FLG'],   'COFFEE_FLG':dna['COFFEE_FLG'], 'DIGITAL_FLG':dna['DIGITAL_FLG'],   'NIGHT_FLG':dna['NIGHT_FLG'],   'JAPAN_FLG':dna['JAPAN_FLG'],   'KOREA_FLG':dna['KOREA_FLG'],'USA_FLG':dna['USA_FLG'],'CHINA_FLG':dna['CHINA_FLG'],'TECHNOLOGY_FLG':dna['TECHNOLOGY_FLG'],'EUROPE_FLG':dna['EUROPE_FLG']},
	# 'dna':{'dna':dna},



	'test':test_dic,
	# 'sql':test['sql'],

	'where_txt':{'where_txt':target['where_txt']},
	'score': {'s1':Score['s1'],'s2':Score['s2'],'s3':Score['s3'],'s4':Score['s4'],'s5':Score['s5'],'s6':Score['s6'],'s7':Score['s7'],'s8':Score['s8'],'s9':Score['s9'],'s10':Score['s10'],'s11':Score['s11'],'s12':Score['s12']},
	'creditCard':{'MCC_A01_FLG':creditCard['MCC_A01_FLG'],	'MCC_A02_FLG':creditCard['MCC_A02_FLG'],	'MCC_B_FLG':creditCard['MCC_B_FLG'],	'MCC_C_FLG':creditCard['MCC_C_FLG'],	'MCC_C01_FLG':creditCard['MCC_C01_FLG'],	'MCC_D_FLG':creditCard['MCC_D_FLG'],	'MCC_E01_FLG':creditCard['MCC_E01_FLG'],	'MCC_E02_FLG':creditCard['MCC_E02_FLG'],	'MCC_E03_FLG':creditCard['MCC_E03_FLG'],	'MCC_F01_FLG':creditCard['MCC_F01_FLG'],	'MCC_F02_FLG':creditCard['MCC_F02_FLG'],	'MCC_F03_FLG':creditCard['MCC_F03_FLG'],	'MCC_H01_FLG':creditCard['MCC_H01_FLG'],	'MCC_H02_FLG':creditCard['MCC_H02_FLG'],'MCC_I_FLG':creditCard['MCC_I_FLG'],'MCC_J_FLG':creditCard['MCC_J_FLG'],'MCC_L01_FLG':creditCard['MCC_L01_FLG'],'MCC_M_FLG':creditCard['MCC_M_FLG']},
	'othBank':{'othBank_1':othBank['othBank_1'],	'othBank_1_3':othBank['othBank_1_3'],	'othBank_3_15':othBank['othBank_3_15'],	'othBank_15_30':othBank['othBank_15_30'],	'othBank_30':othBank['othBank_30']}
	}
	return Response(json.dumps(targetCust), mimetype='application/json')

# 上傳檔案
@app.route("/upload", methods=['POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file:
			data = str(file.read().decode("utf-8")).replace("\r\n",",")
			session['file'] = data[:-1]
			session['filename'] = file.filename

		return redirect(url_for("index"))
	else:
		return redirect(url_for("logout"))

# 刪除上傳檔案
@app.route("/delfile")
def delfile():
	session.pop('file',None)
	session.pop('filename',None)

	return redirect(url_for("index"))

# 登入程式
@app.route("/login_post" , methods=["POST"])
def login_post():
	if request.form.get("act") != "" and request.form.get("pwd") != "":
		session['act'] = request.form.get("act")
		return redirect(url_for("index"))
	else:
		return redirect(url_for("login"))

# 登入程式
@app.route("/login")
def login():
	return render_template("login.html")

# 忘記密碼
@app.route("/forgot_password")
def forgot_password():
	return render_template("forgot-password.html")

# 登出，並清除 SESSION
@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("login"))

# 刪除搜尋的 SESSION
def killtr():
    session.pop('target_total',None)

# 整理各值
def getval(obj,mt,tal):
    val = {}
    if mt == 1:
        for i in range(len(obj)):
            if tal > 0:
                val[obj[i][0].split(":")[0]] = round(float(obj[i][0].split(":")[1]) / tal * 100)
            else:
                val[obj[i][0].split(":")[0]] = obj[i][0].split(":")[1]

    elif mt == 2:
        for i in range(len(obj)):
            if tal > 0:
                val[obj[i].split(":")[0]] = round(float(obj[i].split(":")[1]) / tal * 100)
            else:
                val[obj[i].split(":")[0]] = obj[i].split(":")[1]

    else:
        val = {}

    return val

def getsum(obj):
    vsum = 0
    for i in range(len(obj)):
        vsum = int(vsum) + int(obj[i].split(":")[1])

    return vsum

# 執行頁面
if __name__ == "__main__":
	app.run(debug=True)
	# app.run(port=3333)
	# app.run(host='0.0.0.0',port=80)
	# app.run(host='0.0.0.0',port=3333)
