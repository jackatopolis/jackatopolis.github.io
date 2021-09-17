def scrape():
    from bs4 import BeautifulSoup as bs
    import matplotlib.pyplot as plt
    import requests as req
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager

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

    dataset = {
        'current_crew_names':current_crew_names,
        'current_crew_links':current_crew_links,
        'apod':apod,
        'eonet_data':eonet_data
    }

    return dataset
