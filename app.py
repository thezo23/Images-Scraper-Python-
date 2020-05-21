from bs4 import BeautifulSoup
import requests
import cfscrape
from time import sleep
import random
import string
import os
from config import *
from start import *
import urllib.request
import shutil
from tqdm import tqdm



class scrapper:


    while analysed != total:

            try:

                def url():  # Generating url

                    global link
                    global randoml

                    if case == 'l':
                        randoml = ''.join(random.choices(
                            string.ascii_lowercase, k=letters))
                        randoml = list(randoml)

                    if case == 'b':
                        randoml = ''.join(random.choices(
                            string.ascii_lowercase + string.ascii_uppercase, k=letters))
                        randoml = list(randoml)

                    if case == 'u':
                        randoml = ''.join(random.choices(
                            string.ascii_uppercase, k=letters))
                        randoml = list(randoml)

                    for i in range(numbers):
                        randoml.append(str(random.randint(0, 9)))
                    if randomcheck == 'y':
                        random.shuffle(randoml)
                        randoml = ''.join(randoml)
                        link = "{}{}".format(thelink, randoml)
                        return link
                    else:
                        randoml = ''.join(randoml)
                        link = "{}{}".format(thelink, randoml)
                        return link
                def display(valid, analysed, duplicate):  # Displaying some stats
                    os.system('clear')
                    print("{}/{} analysed -- {} valid -- {} duplicate".format(analysed, total, valid, duplicate))
                    ratio = ("{:.2f}".format(round((valid/analysed)*100, 2)))
                    print("Ratio: {}%".format(ratio))


                # Writing the link in logs to avoid duplicates in the program.
                def logs(link):

                    logs = open('{}.txt'.format(logs_name), 'a')
                    logs.write('\n{}'.format(link))
                    logs.close()
                
                def working_links(link):

                    working_link = open('wotking_links.txt', 'a')
                    working_link.write('\n{}'.format(link))
                    working_link.close()

                scraper = cfscrape.create_scraper()

                html_content = scraper.get(url()).content

                soup = BeautifulSoup(html_content, 'html.parser')

                if tag_scan == 1:
                    linked = soup.find('img', src='//st.prntscr.com/2020/05/14/1716/img/0_173a7b_211be8ff.png')
                if tag_scan == 3:
                    linked = soup.find('img', src='/images/404-spiral.svg')
                if tag_scan == 4:
                    linked = soup.find('div', id='giraffe')

                if linked == None:

                    with open('{}.txt'.format(logs_name)) as myfile:  # Scanning if they is alreay the link in logs
                        s = set(myfile.read().splitlines())
                        if link in s:  # if yes do nothing but addinf 1 to duplicates.
                            duplicate += 1
                            analysed += 1
                            display(valid, analysed, duplicate)

                        else:
                            
                            if save_img == 'y':
                                images = soup.findAll('img')[img_position]
                                dl_img = images['src']
                                
                                opener = urllib.request.build_opener()
                                opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                                urllib.request.install_opener(opener)

                                url = dl_img
                                local = '{}{}.png'.format(file,randoml)
                                urllib.request.urlretrieve(url, local)
                        
                                logs(link)
                                analysed += 1
                                valid += 1
                                display(valid, analysed, duplicate)

                            else:

                                working_links(link)
                                logs(link)
                                analysed += 1
                                valid += 1
                                display(valid, analysed, duplicate)

                else:

                    logs(link)
                    analysed += 1
                    display(valid, analysed, duplicate)


            except ValueError:
                continue
            except AttributeError:
                continue



