def scrape():
    from bs4 import BeautifulSoup as bs
    import matplotlib.pyplot as plt
    import requests as req
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd
    from datetime import date, datetime
    from dateutil import parser
    from datetime import timedelta

    # Extract Current ISS Crew and Links to Bio


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://www.nasa.gov/astronauts"
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('p')
    astro = results[0].find_all('a')

    current_crew_names = []
    current_crew_links = []
    for naut in astro:
        current_crew_names.append(naut.text)
        current_crew_links.append(naut['href'])

    browser.quit()

    # Get Astronomy Picture of the Day

    api_key = 'JzHhdRNv1ybunnDN1ng9mCa6ylTXHbwgufkGcMe1'
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    apod = req.get(url).json()


    # EONET Events (Earth Observatory Natural Event Tracker)

    url = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'
    eonet = req.get(url).json()

    id = []
    title = []
    description = []
    link = []
    categories = []
    sources = []
    geometries = []

    for x in eonet['events']:
        for y in list(x.keys()):
            exec("%s.append(x[y])" % (y))

    source_info = {}
    for index, i in enumerate(sources):
        sor = {}
        for x in i:
            sor[x['id']] = x['url']
        source_info[index] = sor
    
    category_info = {}
    for index, i in enumerate(categories):
        category_info[index] = i[0]['title']

    eonet_data = {
        'id':id,
        'title':title,
        'description':description,
        'link':link,
        'categories':categories,
        'geometries':geometries,
        'sources':sources
    }

    url = 'https://www.timeanddate.com/holidays/us/'
    tables = pd.read_html(url)
    holidays = tables[0]
    holidays_new = pd.DataFrame(data = [holidays['Date']['Date'],
                            holidays['Unnamed: 1_level_0']['Unnamed: 1_level_1'],
                            holidays['Name']['Name'],
                            holidays['Type']['Type'],
                            holidays['Details']['Details']])
    holidays_new = holidays_new.T
    holidays_new.rename(columns={'Unnamed: 1_level_1':'Day'},inplace=True)
    holidays_new.drop(index=511,inplace=True)
    holidays_new.dropna(subset=['Date'],inplace=True)

    dt = []
    for x in holidays_new['Date']:
        tmp = parser.parse(x).date()
        dt.append(tmp)
    holidays_new['Date'] = dt
    
    hol = holidays_new.loc[(holidays_new['Date']==date.today())|
                (holidays_new['Date']==(date.today()+timedelta(days=1)))|
                (holidays_new['Date']==(date.today()+timedelta(days=2)))|
                (holidays_new['Date']==(date.today()+timedelta(days=3)))|
                (holidays_new['Date']==(date.today()+timedelta(days=4)))|
                (holidays_new['Date']==(date.today()+timedelta(days=5)))]
    results = hol.to_json(orient="index")



    # Save final Dataset for export
    dataset = {
        'current_crew_names':current_crew_names,
        'current_crew_links':current_crew_links,
        'apod':apod,
        'eonet_data':eonet_data,
        'holidays':results
    }

    return dataset