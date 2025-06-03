from bs4 import BeautifulSoup
import requests


# دلار
def dollar():
    url = 'https://www.tgju.org/profile/price_dollar_rl'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    dollar_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return dollar_price


# یورو
def euro():
    url = 'https://www.tgju.org/profile/price_eur'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    euro_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return euro_price


# درهم امارات
def DirhamUAE():
    url = 'https://www.tgju.org/profile/price_aed'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    dirhamuae_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return dirhamuae_price


# پوند انگلیس
def GBP():
    url = 'https://www.tgju.org/profile/price_gbp'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    gbp_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return gbp_price


# لیر ترکیه
def TRY():
    url = 'https://www.tgju.org/profile/price_try'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    try_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return try_price


# فرانک سوئیس
def Switzerland():
    url = 'https://www.tgju.org/profile/price_chf'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    chf_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return chf_price


# یوان چین
def China():
    url = 'https://www.tgju.org/profile/price_cny'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    yuan_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return yuan_price


# وون کره جنوبی
def South_Korea():
    url = 'https://www.tgju.org/profile/price_krw'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    krw_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return krw_price


# دلار کانادا
def Canadian_dollar():
    url = 'https://www.tgju.org/profile/price_cad'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    cad_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return cad_price


# دلار استرالیا
def Australian_dollar():
    url = 'https://www.tgju.org/profile/price_aud'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    australian_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return australian_price


# دلار نیوزیلند
def NewZealand():
    url = 'https://www.tgju.org/profile/price_nzd'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    nzd_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return nzd_price


# دلار سنگاپور
def Singapore():
    url = 'https://www.tgju.org/profile/price_sgd'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    SGD_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return SGD_price


# روپیه هند
def India():
    url = 'https://www.tgju.org/profile/price_inr'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    inr_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return inr_price


# روپیه پاکستان
def Pakistan():
    url = 'https://www.tgju.org/profile/price_pkr'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    pkr_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return pkr_price


# دینار عراق
def Iraq():
    url = 'https://www.tgju.org/profile/price_iqd'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    iqd_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return iqd_price


# پوند سوریه
def Syria():
    url = 'https://www.tgju.org/profile/price_syp'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    syp_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return syp_price


# افغانی
def Afghanistan():
    url = 'https://www.tgju.org/profile/price_afn'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    afn_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return afn_price


# کرون دانمارک
def Denmark():
    url = 'https://www.tgju.org/profile/price_dkk'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    dkk_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return dkk_price


# کرون سوئد
def Sweden():
    url = 'https://www.tgju.org/profile/price_sek'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    sek_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return sek_price


# کرون نروژ
def Norway():
    url = 'https://www.tgju.org/profile/price_nok'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    nok_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return nok_price


# ریال عربستان
def Saudi_Arabia():
    url = 'https://www.tgju.org/profile/price_sar'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    sar_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return sar_price


# ریال قطر
def Qatar():
    url = 'https://www.tgju.org/profile/price_qar'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    qar_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return qar_price


# ریال عمان
def Oman():
    url = 'https://www.tgju.org/profile/price_omr'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    omr_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return omr_price


# دینار کویت
def Kuwait():
    url = 'https://www.tgju.org/profile/price_kwd'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    kwd_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return kwd_price


# دینار بحرین
def Bahrain():
    url = 'https://www.tgju.org/profile/price_bhd'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    bhd_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return bhd_price


# رینگیت مالزی
def Malaysia():
    url = 'https://www.tgju.org/profile/price_myr'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    myr_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return myr_price


# بات تایلند
def Thailand():
    url = 'https://www.tgju.org/profile/price_thb'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    thb_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return thb_price


# دلار هنگ کنگ
def HongKong():
    url = 'https://www.tgju.org/profile/price_hkd'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    hkd_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return hkd_price


# روبل روسیه
def Russian():
    url = 'https://www.tgju.org/profile/price_rub'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    rub_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return rub_price


# منات آذربایجان
def Azerbaijan():
    url = 'https://www.tgju.org/profile/price_azn'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    azn_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return azn_price


# درام ارمنستان
def Armenian():
    url = 'https://www.tgju.org/profile/price_amd'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    amd_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return amd_price


# لاری گرجستان
def Georgian():
    url = 'https://www.tgju.org/profile/price_gel'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    gel_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return gel_price


# سوم قرقیزستان
def Kyrgystan():
    url = 'https://www.tgju.org/profile/price_kgs'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    kgs_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return kgs_price


# سامانی تاجیکستان
def Tajikistan():
    url = 'https://www.tgju.org/profile/price_tjs'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    tjs_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return tjs_price


# منات ترکمنستان
def Turkmenistan():
    url = 'https://www.tgju.org/profile/price_tmt'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    tmt_price = soup.find('span', {'data-col': 'info.last_trade.PDrCotVal'}).text
    return tmt_price
