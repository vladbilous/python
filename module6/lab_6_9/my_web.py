#! coding: utf-8
import requests  # import requests module

url = "http://www.i.ua/"  # Set curl for parse
print(url)  # Print url


def news_links(url):
    __news_links = []
    try:
        r = requests.get(url)  # Connect to web page ang get data
        content = r.content  # Get list of bytes from web page source
        content = str(content)  # Convert bytes to string
        try:

            content = content.split('class="news"')[1]  # Get part from class="news" till the end of page
            content.split("</div>")[0]  # Get part till news <div> block end

            href_lines = content.split('href="')  # Split line by link start

            for line in href_lines:
                if "http:" in line and "click" in line:  # Check that http in line and click marker present
                    link = line.split('"')[0]
                    print(link)  # print link
                    __news_links.append(link)  # Add link to link list
        except IndexError:
            "Data not found"
    except requests.exceptions.ConnectionError:
        print("Page not found!")
    return __news_links


news_links(url)
