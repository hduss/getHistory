# coding: utf-8
import requests
import os
from bs4 import BeautifulSoup
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style

colorama.init()

"""" == Colorama example ==

print(Fore.BLUE + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
print(Fore.GREEN + "This is the color of grass" + Style.RESET_ALL)
print(Fore.BLUE + Style.DIM + "This is a dimmer version of the sky" + Style.RESET_ALL)
print(Fore.YELLOW + "This is the color of the sun" + Style.RESET_ALL)"""

# exemple param => http://laceliah.cowblog.fr/2.html
url = "http://laceliah.cowblog.fr/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Création du fichier upload
if not os.path.isdir('uploads'):
    os.mkdir('uploads')

page = 2
pageMax = 4
urls = ["http://laceliah.cowblog.fr/"]

# Get alla rticles in page
articles = soup.find_all('div', class_='article')
allPageArticle = []

# todo: create main loop
# todo: Create one folder per page (page1, page2 ...)

for article in articles:

    fullArticle = []

    """" == Détails == 
    
    id = article.get('id')
    title = article.find('div', class_='article-top').text
    articleContent = article.find('div', class_='article-body')
    img = article.find_all('img')"""


    articleTitle = article.find('p', class_='left-1').text
    # Solve encode problem on special caracteres
    encodedTitle = articleTitle.encode('latin1').decode('utf8')

    fullArticle.append({'Titre': encodedTitle})
    fullArticle.append({'Contenu': article.find('div', class_='article-body')})
    fullArticle.append({'Images': article.find_all('img')})

    # For DEBUG
    createFolders = True
    if createFolders:

        try:
            chemin = "uploads/" + encodedTitle
            os.mkdir(chemin)
            print(Fore.GREEN + Style.NORMAL + "== Dossier " + encodedTitle + " crée" + Style.RESET_ALL)

            try:
                fichier = open(chemin + "/contenu.txt", "a")

                try:
                    fichier.write(str(fullArticle[1]['Contenu'].text))
                    print("==== Fichier de contenu crée")
                except Exception as e:

                    print(os.strerror(e.errno))

                fichier.close()

            except Exception as e:

                print(os.strerror(e.errno))

            if len(fullArticle[2]['Images']) > 0:
                for img in fullArticle[2]['Images']:

                    image = img.get('src')
                    imageName = image.split('/').pop()
                    response = requests.get(image).content

                    with open(chemin + '/' + imageName, "wb+") as f:
                        f.write(response)
                        print("====== Image " + imageName + " sauvegardé")

        except Exception as e:
            print(Fore.RED + Style.BRIGHT + ' Dossier ' + encodedTitle + " existe deja" + Style.RESET_ALL)


        #break
        #allPageArticle.append(fullArticle)



while page < pageMax:
    urls.append(url + str(page) + ".html")
    page += 1
