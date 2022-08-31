
import random
import datetime
import bs4 as bs
import asyncio

# # BISNIS.COM 
async def get_data_bisnis(session):
    date_now = datetime.datetime.strftime(datetime.datetime.now().date(), "%Y-%m-%d")
    bisnis_url = [
        f"https://www.bisnis.com/index?c=194&d={date_now}",
        f"https://www.bisnis.com/index?c=5&d={date_now}",
        f"https://www.bisnis.com/index?c=43&d={date_now}"
    ]
    headers= {"user-agent":"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'"}
    all_data = []
    for i in bisnis_url:
        async with session.get(i, headers=headers) as data:
            data = await data.text()
            await asyncio.sleep(random.randint(0, 3))
            soup = bs.BeautifulSoup(data,'html.parser')
            for j in soup.find_all("div", {"class": "col-sm-4"})[:5]:
                title = j.a['title']
                link = j.a['href']
                all_data.append([title, link])
            
    return all_data


# #  KONTAN
async def get_data_kontan(session):
    d = datetime.datetime.now().day
    m = datetime.datetime.now().month
    y = datetime.datetime.now().year

    kontan_url = [
        f"https://www.kontan.co.id/search/indeks?kanal=keuangan&tanggal={d}&bulan={m}&tahun={y}&pos=indeks",
        f"https://www.kontan.co.id/search/indeks?kanal=investasi&tanggal={d}&bulan={m}&tahun={y}&pos=indeks",
        f"https://www.kontan.co.id/search/indeks?kanal=industri&tanggal={d}&bulan={m}&tahun={y}&pos=indeks"
    ]
    all_data = []
    for i in kontan_url:
        async with session.get(i) as data:
            data = await data.text()
            await asyncio.sleep(random.randint(0, 3))
            soup = bs.BeautifulSoup(data,'html.parser')
            for j in soup.find_all('h1')[:5]:
                tittle = j.find('a').text
                link = j.find('a')['href']
                all_data.append([tittle, link])
            
    return all_data


# #  CNBC
async def get_data_cnbc(session):
    d = datetime.datetime.now().day
    m = datetime.datetime.now().month
    y = datetime.datetime.now().year

    cnbc_url = [
        f'https://www.cnbcindonesia.com/market/indeks/5/1?date={y}/{m}/{d}',
        f'https://www.cnbcindonesia.com/investment/indeks/6/1?date={y}/{m}/{d}']

    all_data = []
    for i in cnbc_url:
        async with session.get(i) as data:
            data = await data.text()
            await asyncio.sleep(random.randint(0, 3))
            soup = bs.BeautifulSoup(data,'html.parser')
            for j in soup.find_all('article')[:5]:
                title = j.find('h2').text
                link = j.find('a')['href']
                all_data.append([title, link])

    return all_data


# #  INVESTOR 
async def get_data_investor(session):
    date_now = datetime.datetime.strftime(datetime.datetime.now().date(), "%d-%m-%Y")

    investor_url = [
        f"https://investor.id/indeks?category=market-and-corporate&date={date_now}",
        f"https://investor.id/indeks?category=finance&date={date_now}",
        f"https://investor.id/indeks?category=business&date={date_now}"
    ]
    all_data = []
    for i in investor_url:
        async with session.get(i) as data:
            data = await data.text()
            await asyncio.sleep(random.randint(0, 3))
            soup = bs.BeautifulSoup(data,'html.parser')
            for j in soup.find_all("p", {"class": "font-summary-semibold mb5"})[:5]:
                title = j.text.replace('\n','').replace('\t', "")
                link = j.find('a')['href']
                all_data.append([title, link])
    
    return all_data


# #  KATADATA
async def get_data_katadata(session):
    all_data = []
    async with session.get("https://katadata.co.id/indeks/search/-/-/-") as data:
        data = await data.text()
        await asyncio.sleep(random.randint(0, 3))
        soup = bs.BeautifulSoup(data,'html.parser')
        for i in soup.find_all("div", {"class": "content-text"})[:5]:
            title = i.find('h2').text
            link = i.find('a')['href']
            all_data.append([title, link])
        
    return all_data


# #  KOMPAS
async def get_data_kompas(session):
    date_now = datetime.datetime.strftime(datetime.datetime.now().date(), "%Y-%m-%d")
    url = f"https://indeks.kompas.com/?site=money&date={date_now}"
    all_data = []
    async with session.get(url) as data:
        data = await data.text()
        await asyncio.sleep(random.randint(0, 3))
        soup = bs.BeautifulSoup(data, "html.parser")
        for i in soup.find_all("a", {"class": "article__link"})[:5]:
            title = i.text
            link = i['href']
            all_data.append([title, link])
            
    return all_data


# # EMITEN

async def get_data_emiten(session):
    url = [
    "https://www.emitennews.com/category/makro",
    "https://www.emitennews.com/category/emiten"]
    all_data = []
    for i in url:
        async with session.get(i) as data:
            data = await data.text()
            await asyncio.sleep(random.randint(0, 3))
            soup = bs.BeautifulSoup(data, 'html.parser')
            all_data_2 = []
            for i in soup.find_all("a"):
                p = i.parent.attrs
                if bool(p):
                    if p['class'] == ['list-category'] or p['class'] == ["highlight-category"]:
                        title = i.find("h1").text
                        link = i['href']
                        all_data_2.append([title, link])        
            all_data = all_data + all_data_2[:5]
            
    return all_data

async def add_sleep():
    await asyncio.sleep(random.randint(0, 3))
