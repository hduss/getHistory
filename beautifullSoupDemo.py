# coding: utf-8
import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

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

# @totdo: Create one folder per page

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


    createFolders = True

    if createFolders:

        try:

            chemin = "uploads/" + encodedTitle
            os.mkdir(chemin)

            try:
                fichier = open(chemin + "/contenu.txt", "a")
                fichier.write("test")
                """try:
                    fichier.write(str(fullArticle[1][1].text))
                except:
                    print(os.strerror(e.errno))"""

                fichier.close()


            except Exception as e:
                print(os.strerror(e.errno))

            if len(fullArticle[2]['Images']) > 0:
                print('Images ici')

                for img in fullArticle[2]['Images']:
                    image = img.get('src')
                    imageName = image.split('/').pop()
                    print(imageName)

                    response = requests.get(image).content

                    with open(imageName, "wb+") as f:
                        f.write(response)

                    """image_bytes = BytesIO(response.content)
                    img = Image.open(image_bytes)
                    # img.show()
                    Image.save(chemin + '/' + imageName)"""


        except Exception as e:
            print(os.strerror(e.errno))

        #break

        allPageArticle.append(fullArticle)

while page < pageMax:
    urls.append(url + str(page) + ".html")
    page += 1
