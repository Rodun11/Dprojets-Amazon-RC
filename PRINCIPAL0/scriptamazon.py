#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: rodibaran
"""

import random
import string


"NOMS: UTILISÉS DURANT TOUT LE PROCESSUS"


#Les noms de personnages sont utilisés pour la création d'adresses mail et de mots de passes simples, et réalistes.
nompersonnages = [
    "aragorn",
    "boromir",
    "frodo",
    "gandalf",
    "gimli",
    "legolas",
    "merry",
    "pippin",
    "sam",
    "saruman",
    "sauron",
    "theoden",
    "cyruslegrand",
    "cambyseii",
    "bardiya",
    "smerdis",
    "dariusier",
    "xerxesier",
    "artaxerxesier",
    "dariusier",
    "boratsagdiyev",
    "azamatbagatov",
    "tutarsagdiyev",
    "nursultantulyakbay",
    "pamelaanderson",
    "rudygiuliani",
    "kendavitian",
    "sachabaroncohen",
    "mariabakalova",
    "jeanisejones",
]


prenoms0 = ["Nicolas", "Sébastien", "Julien", "David", "Christophe", "Guillaume", "Alexandre", "Laurent", "JeanBaptiste", "Olivier", "Thomas", "Maxime", "Charles", "Mathieu", "Pierre", "Anthony", "Jonathan", "Romain", "Benjamin", "Alexis", "Antoine", "Kevin", "Maximilien", "Sylvain", "Stephane", "Loic", "Damien", "Jeremy", "Gregory", "Stephane", "Florian", "Sebastien", "Arnaud", "Benjamin", "Julien", "Alexandre", "Vincent", "Adrien", "Mathieu", "Maxime", "Nicolas", "Thomas", "Sylvain", "Kevin", "Anthony", "Yann", "Romain", "Jonathan", "Florian", "Julien", "Sébastien", "Alexandre", "Maxime", "Loic", "Thomas", "Gregory", "Benjamin", "Nicolas", "Antoine", "Damien", "Stephane", "Pierre", "Laurent", "Vincent", "Christophe", "Romain", "Alexandre", "Jonathan", "Kevin", "Thomas", "Maxime", "Nicolas", "Sylvain", "Bastien", "Julien", "Gregory", "David", "Christophe", "Anthony", "Loic", "Mathieu", "Stephane", "Vincent", "Pierre", "Laurent", "Benjamin", "Jerome"]
prenom0 = random.choice(prenoms0)
print(prenom0)

noms0 = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Dupont", "Durand", "Leroy", "Blanc", "Moreau", "Garcia", "Martinez", "Dubois", "Lambert", "Pereira", "Simon", "Roussel", "Lefebvre", "Girard", "Caron", "Lebrun", "David", "Laroche", "Roux", "Duval", "Leroux", "Gauthier", "Mayer", "Leclerc", "Morel", "Leconte", "Laurent", "Martineau", "Germain", "Rivière", "Colin", "Lemaire", "Lavigne", "Gabin", "Bonnet", "Fontaine", "Duval", "Garnier", "Aubert", "Rousseau", "Leclercq", "Legrand", "Barbier", "Guillaume", "Hubert", "Guérin", "Lambert", "Dumas", "Leroux", "Dumoulin", "Delahaye", "Leroy", "Lambert", "Dupont", "Martin", "Martinez", "Garcia", "Dubois", "Pereira", "Simon", "Lefebvre", "Roussel", "Girard", "Caron", "Lebrun", "David", "Laroche", "Roux", "Duval", "Leroux", "Gauthier", "Mayer", "Leclerc", "Morel", "Leconte", "Laurent", "Martineau", "Germain"]
nom0 = random.choice(noms0)
print(nom0)

lesdeux0 = (prenom0+" "+nom0)
print(lesdeux0)

"DATE: UTILISÉ POUR LA CRÉATION DU COMPTE OUTLOOK"


annee0 = random.randint(1946, 2000)
print (annee0)

#Pour les jours de naissance, on prend jusqu'au 27, pour ne pas avoir à prévoir des années bisextiles.
jours0 = [str(i) for i in range(1, 27)]
jour0 = random.choice(jours0)
print(jour0)

#Un mois en text
months0 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month0 = random.choice(months0)
print(month0)

#Un mois en chiffre
months1 = [str(i) for i in range(1, 12)]
month1 = random.choice(months1)
print(month1)

"mdpppppppppppp utilisé durant tout le processus"

#Dans cette partie on règle le "tirage" du mot de passe pour qu'il soit dans les règles nb. de caractères, maj., min., etc.

special_characters = ["@", "#", "$", "%", "&", "*", "(", ")", "_", "+", "?"]


characters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
characters.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
characters.extend(special_characters)
characters.extend([str(i) for i in range(0, 10)])


def generate_mdp():
    
    random_prenom = ''.join(random.choice(prenoms0))
    random_popc = ''.join(random.choice(nompersonnages))
    random_carac = ''.join(random.choice(special_characters))
    random_nmr = ''.join(random.choice(string.digits) for _ in range(2))
    
    mdp = random_prenom + random_popc + random_carac + random_nmr
    return mdp

mdp0 = generate_mdp()
print(mdp0)

"MAIL UTILISÉ DURANT TOUT LE PROCESSUS"

#Pareil que pour le mot de passe, ici toutes les conditions de génération d'un nouvel ID mail sont mises en places

liste_mail = ["@hotmail.com", "@outlook.fr", "@outlook.com"]

#Pour la création de l'ID, ce sera simplement une combinaison de la liste  nomspersonnages, avec
#la liste mois_persan (les mois de l'année en persan), avec deux chiffres à la fin.

mois_persan = [
    "Farvardin",
    "Ordibehesht",
    "Khordad",
    "Tir",
    "Mordad",
    "Shahrivar",
    "Mehr",
    "Aban",
    "Azar",
    "Dey",
    "Bahman",
    "Esfand",
]


#Voilà exactement la fonction combinaison de listes, nécessaire au mot de passe:
def generate_random_string():
    # Génère une séquence aléatoire de lettres (4 à 10 caractères)
    random_prenom = ''.join(random.choice(prenoms0))
    
    random_mois = ''.join(random.choice(mois_persan))
    
    random_nom = ''.join(random.choice(noms0))
    
    random_perso = ''.join(random.choice(nompersonnages))
    
    # Génère deux chiffres aléatoires
    random_digits = ''.join(random.choice(string.digits) for _ in range(2))
    
    # Combine les lettres et les chiffres pour former la chaîne finale
    random_string = random_mois + random_perso + random_digits
    
    random_terminaison = random.choice(liste_mail)
    
    e_mail = random_string + "@hotmail.com"
    
    return e_mail


e_mail0 = generate_random_string()
print(e_mail0)



"INFORMATIONS PRIME: TIRAGES SPÉCIFIQUES À PRIME"

#Enfin, derniers tirages faits ici pour la partie compte courant de l'inscription à l'abonnement prime.

BICS0 = ["FONAFRP1", "LVMHFRPP", "ATELFRPP", "GPBAFRPP", "CEPAFRPP", "AUCHFR22", "SOAPFR22", "BOUSFRPP", "CMCIFR2A", "CRLYFRPP"]
BIC0 = random.choice(BICS0)
print(BIC0)

rues = ["avenue des champs élysées", "place vendôme", "rue croix des petits champs", "rue du louvre", "boulevard poissonière", "rue bergère", "rue richer", "rue du faubourg poissonière", "rue la fayette", "rue maubeuge", "boulevard de clichy", "avenue de saint-ouen", "avenue de l'opera", "rue tronchet"]
rue = random.choice(rues)

adresse = jour0+" "+rue
print(adresse)

huit_chiffres_aleatoires = str(random.randint(10000000, 99999999))
z6s = ["06", "07"]
z6 = random.choice(z6s)
numero = z6+huit_chiffres_aleatoires
print(numero)

#Nous importons ici les packages qui nous seront utiles

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import webbrowser
from selenium.common.exceptions import TimeoutException as SETimeoutException

#Sur mac M1, avec Firefox 118.0, et geckodriver 0.33.0, voici les commandes que j'ai pour utiliser le navigateur Firefox dans cette section ####

#Ici, il faut coller son propre chemin d'accès 
driver_path = '/opt/homebrew/bin/geckodriver'
# Créez un service Geckodriver
service = Service(executable_path=driver_path)

#options pour le pilote Firefox
options = Options()

#options.add_argument('--headless')  

driver = webdriver.Firefox(service=service, options=options)


#Fin de section ####

#Definitions des 3 URLs principaux dont nous userons:
url1 = 'https://signup.live.com/?lic=1'
url2 = 'https://www.amazon.fr/'
url3 = 'https://outlook.live.com/mail/'


#Definition des noms d'objets:
#CDS = champ de saisie (textbox)
#MDP = mot de passe


#Nous commençons par la création de notre adresse mail outlook:    

driver.get(url1)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
try:
    
    driver.implicitly_wait(10)
    

    
    email_input = driver.find_element(By.ID, 'MemberName')
    
    
    email_input.clear()
    
    
    new_email = e_mail0
    
    email_input.send_keys(new_email)
    
    bouton_poursuivre_mail = driver.find_element(By.ID, 'iSignupAction')
    
    bouton_poursuivre_mail.click()
    
    #Passage à la page suivante
    
    time.sleep(2)    
    
    deselectionner_spams = driver.find_element(By.ID, 'iOptinEmail')
    
    time.sleep(2.4)
    
    CDS_MDP = driver.find_element(By.ID, 'PasswordInput')
    
    MDP_prevu = mdp0
    
    CDS_MDP.send_keys(MDP_prevu)
    
    bouton_poursuivre_MDP = driver.find_element(By.ID, 'iSignupAction')
    
    bouton_poursuivre_MDP.click()
    
    time.sleep(0.4)
    
    CDS_prenom = driver.find_element(By.ID, 'FirstName')
    
    prenom_prevu = prenom0
    
    CDS_prenom.send_keys(prenom_prevu)
    
    CDS_nom = driver.find_element(By.ID, 'LastName')
    
    nom_prevu = nom0
    
    CDS_nom.send_keys(nom_prevu)
    
    bouton_poursuivre_nom = driver.find_element(By.ID, 'iSignupAction')
    
    bouton_poursuivre_nom.click()
    
    time.sleep(2)
    
    #Le code qui suit est quelque peu différent des simples driver.find précedents, en effets, nous aurons affaire ici
    #à des "menus déroulants"
    

    choix_pays = driver.find_element(by=By.ID, value="Country")


    options = choix_pays.find_elements(by=By.TAG_NAME, value="option")
    for option in options:
        if option.text == "France":
            option.click()
            break
    time.sleep(1)
    
    choix_mois = driver.find_element(by=By.ID, value="BirthMonth")
    
    
    for option in choix_mois.find_elements(by=By.TAG_NAME, value="option"):
        if option.get_attribute("value") == month1:
            option.click()
            break
    
    choix_jour = driver.find_element(by=By.ID, value="BirthDay")
    
    options = choix_jour.find_elements(by=By.TAG_NAME, value="option")
    for option in options:
        if option.text == jour0:
            option.click()
            break

        
    CDS_ADN = driver.find_element(By.ID, 'BirthYear')
    CDS_ADN.send_keys(annee0)
    
    bouton_poursuivre_date = driver.find_element(By.ID, 'iSignupAction')
    bouton_poursuivre_date.click()
    
    time.sleep(2)
    
    "CAPTCHA" #ICI, à cet emplacement précis se trouve un captcha à résoudre en moins de 120 secondes. 
    
    try:
        onspr = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ms-Button.ms-Button--primary')))
        time.sleep(2)
        onspr.click()
        time.sleep(1)
    except: pass

    try:
        nprco = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".win-button.button-secondary.button.ext-button.secondary.ext-secondary")))
        nprco.click()
    except: pass
    

except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")
    
#L'adresse mail Outlook a étée crée, il faut maintenant passer à la création du compte Amazon, en accédant à sa page:

time.sleep(1)
driver.execute_script("window.open('https://www.amazon.fr/');")

time.sleep(2)

first_tab = driver.window_handles[0]

driver.switch_to.window(first_tab)

driver.close()

driver.switch_to.window(driver.window_handles[0])


try:
    
    driver.implicitly_wait(10)
    
    time.sleep(5)
    try:
        cookies = driver.find_element(By.ID, 'sp-cc-accept')
        cookies.click()
    except: pass
    
    time.sleep(3)
    
    clic_prime = driver.find_element(By.ID, 'nav-link-amazonprime')
    time.sleep(2)
    clic_prime.click()
    
    bouton_30j = driver.find_element(By.ID, "prime-header-CTA")
    time.sleep(5)
    bouton_30j.click()
    
    bouton_sinscrire = driver.find_element(By.ID, 'createAccountSubmit')
    time.sleep(6)
    bouton_sinscrire.click()
    
    CDS_NOMS = driver.find_element(By.ID, 'ap_customer_name')
    time.sleep(2)
    CDS_NOMS.send_keys(lesdeux0)
    
    CDS_mail = driver.find_element(By.ID, 'ap_email')
    time.sleep(7)
    CDS_mail.send_keys(e_mail0)
    time.sleep(4)
    CDS_motdp = driver.find_element(By.ID, 'ap_password')
    time.sleep(8)
    CDS_motdp.send_keys(mdp0)
    
    time.sleep(4)
    
    CDS_motdpc = driver.find_element(By.ID, 'ap_password_check')
    time.sleep(6)
    CDS_motdpc.send_keys(mdp0)
    
    time.sleep(5)
    
    bouton_inscript = driver.find_element(By.ID, 'continue')
    
    bouton_inscript.click()
    
    "Possible CAPTCHA" #Il y a des possibilités de rencontrer un captcha ici. Souvent si on crée des comptes amazon à la suite.
    #50 secondes sont données pour résoudre ce captcha
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, 'cvf-input-code')))
    
except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        
#Un mail avec un code de vérification Amazon a été envoyé à notre adresse Outlook, nous allons le récupérer pour finaliser la création du compte:

driver.execute_script("window.open('https://go.microsoft.com/fwlink/p/?linkid=2125442&clcid=0x409&culture=en-us&country=us');")

time.sleep(2)


driver.switch_to.window(driver.window_handles[1])


time.sleep(2)

#Ici pour récuperer le code de verifications, nous avons mis en place un try/except, car selon la vitesse
#de connecion, des objets(des messages de configuration du mail)  viennent se placer sur l'écran et empêchent d'accéder
#au HTML du mail, que l'on veut scrapper avec BS4. Le except est fait pour les fermer, puis retourner chercher le code.

try:
    WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.ID, 'loadingScreen')))
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Vérifiez votre nouveau compte Amazon')]")))
    element.click()
    
    WebDriverWait(driver, 50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value='.x_otp'))
    
    html = driver.page_source  
       
    soup = BeautifulSoup(html, 'html.parser')
  
    otp_element = soup.find('p', class_='x_otp')
    
    if otp_element:
    
        otp_code = otp_element.text
        print(f"Code de vérification : {otp_code}")
    
    else:
        print("Élément de code de vérification non trouvé dans le HTML de l'e-mail.")
    
except:

    
    time.sleep(1)
    jspr = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ms-Button.ms-Button--primary.Yl7JD')))
    time.sleep(3)
    jspr.click()
    time.sleep(1)
    
    mbx = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ms-Button.ms-Button--primary.E8L0k")))
    time.sleep(3)
    
    mbx.click()
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Vérifiez votre nouveau compte Amazon')]")))
    element.click()
    
    WebDriverWait(driver, 50).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value='.x_otp'))

    html = driver.page_source  
       
    soup = BeautifulSoup(html, 'html.parser')
    
    otp_element = soup.find('p', class_='x_otp')

    if otp_element:

        otp_code = otp_element.text
        print(f"Code de vérification : {otp_code}")

    else:
        print("Élément de code de vérification non trouvé dans le HTML de l'e-mail.")
    
    
    
driver.close()

driver.switch_to.window(driver.window_handles[0])

#Nous revenons sur l'onglet Amazon pour coller le code de verification que nous avons récupéré dans l'objet otp_code:

    
time.sleep(1)

cds_verif = driver.find_element(By.ID, 'cvf-input-code')

cds_verif.send_keys(otp_code)

time.sleep(1)


creercmptama = driver.find_element("xpath", "//input[@class='a-button-input' and @type='submit' and @aria-labelledby='cvf-submit-otp-button-announce']")
creercmptama.click()

time.sleep(4)
try:
    cookies = driver.find_element(By.ID, 'sp-cc-accept')
    cookies.click()
except: pass

#Nous nous dirigeons à présent vers la page pour souscrir à un abonnement Prime:

try:
    time.sleep(1)
    
    driver.execute_script("window.scrollBy(0, 450);")
    
    entreecmptcour = driver.find_element(By.XPATH, "//a[contains(text(),'Ajouter un compte courant')]")
    time.sleep(1)
    entreecmptcour.click()
    time.sleep(3)
except:
    
    time.sleep(3)
    
    driver.find_element(By.ID, 'nav-link-amazonprime').click()
    
    time.sleep(1)
    
    driver.find_element(By.ID, 'prime-header-CTA').click()
    
    time.sleep(1)
    try:
        driver.find_element(By.ID, 'pp-bVm0ev-80').click()
        time.sleep(2)
    except: pass
    try:
        driver.execute_script("window.scrollBy(0, 450);")
    except: pass
    
    entreecmptcour = driver.find_element(By.XPATH, "//a[contains(text(),'Ajouter un compte courant')]")
    time.sleep(1)
    entreecmptcour.click()
    time.sleep(3)
        
    

#Une fois sur la page de souscription à prime nous ouvrons un onglet avec le site randomiban pour y récuperer 
#des numeros IBAN plus tard dans la boucle:

driver.execute_script("window.open('http://randomiban.com/?country=France')")


#À partir de la boucle suivante, et plus tard, la plupart des objets (champs de saisie, boutons, etc.)
#se trouvent dans un #document contenu lui-même dans un iframe, il faudra y accéder avec des commandes spécifiques
#qui sautent à l'oeil en bas. Cepednant pour pouvoir scroller, il faut sortir de ce iframe, donc cela crée beaucoup
#de lignes de code supplémentaires.

#La boucle BIC/IBAN se répète tant que l'IBAN récupéré sur le site IBAN GEN. n'est pas juste (message d'erreur), ce qui arrive souvent.
#Il est important de noter qu'au bout d'un grand nombre de tentatives (>20), il vaut peut-être mieux relancer le code.

while True:
    
    #Ici, pour ne pas utiliser de time.sleep fixes en termes d'attente, (round(random.uniform(2, 4), 1) sera utilisé à
    #la place, pour générer des temps aléatoires afin que cette boucle qui peut être amenée à se répeter ne soit pas 
    #trop "monotone", et que le temps soit différent pour chaque time.sleep.

    error_message = None
    
    driver.switch_to.window(driver.window_handles[1])
    
    IBANhasard = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'gen_button')))
    IBANhasard.click()
    time.sleep(round(random.uniform(2, 4), 1))
    
    iban_element = driver.find_element("xpath", "//p[@id='demo' and @class='ibandisplay']")
    iban = iban_element.text
    time.sleep(round(random.uniform(2, 4), 1))
    
    print(iban)
    
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(round(random.uniform(2, 4), 1))
    iframe_element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id$='81']")))
    
    driver.switch_to.frame(iframe_element)
    
    
    
    cds_bic = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='9']")))
    cds_bic.send_keys(BIC0)
    time.sleep(round(random.uniform(2, 4), 1))
    
    cds_IBAN = driver.find_element(By.CSS_SELECTOR, "input[id$='10']")
    cds_IBAN.send_keys(iban)
    time.sleep(round(random.uniform(2, 4), 1))
    cds_nomsetpren = driver.find_element(By.CSS_SELECTOR, "input[id$='11']")
    cds_nomsetpren.send_keys(lesdeux0)
    
    driver.switch_to.default_content()
    
    time.sleep(round(random.uniform(2, 4), 1))
    
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(round(random.uniform(2, 4), 1))
    driver.switch_to.frame(iframe_element)
    
    suivantbic = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[id$='13']")))
    time.sleep(round(random.uniform(2, 4), 1))
    suivantbic.click()

    time.sleep(round(random.uniform(2, 4), 1))
    
    
    # Vérifier si un message d'erreur est présent
    try:
        error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='a-box a-alert a-alert-error']//span[@class='a-list-item']")))
    except: pass
    #pagesuivante = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//label[@class='a-form-label' and contains(text(), 'Ligne d'adresse&nbsp;1')]")))
    
    driver.switch_to.default_content()
    if not error_message:
        # Si un message d'erreur est présent, répétez le code
        break
    error_message = None
    # Si aucun message d'erreur n'est présent, sortez de la boucle
    

#Nous passons ici à la dernière partie du code, donner ses informations personnelles, nous donnerons donc celles
#générées automatiquement, adresse, numero, noms, pays.


try:
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    driver.switch_to.frame(iframe_element)

    cds_nomsepa = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='13']")))
    cds_nomsepa.send_keys(lesdeux0)
    time.sleep(0.9)
    driver.switch_to.default_content()
    time.sleep(1.5)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    driver.switch_to.frame(iframe_element)
    
    cds_adresse = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='14']")))
    cds_adresse.send_keys(adresse)
    time.sleep(2)
    
    driver.switch_to.default_content()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(0.5)
    driver.switch_to.frame(iframe_element)
    time.sleep(1)
    
    cds_ville =  WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='16']")))
    cds_ville.send_keys("Paris")
    time.sleep(2)
    
    driver.switch_to.default_content()
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)
    driver.switch_to.frame(iframe_element)
    time.sleep(2.1)
    
    cds_pays = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='17']")))
    cds_pays.send_keys("France")
    time.sleep(4)
    
    driver.switch_to.default_content()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(0.5)
    driver.switch_to.frame(iframe_element)
    time.sleep(1.4)
    
    cds_codepostal = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='18']")))
    cds_codepostal.send_keys("75000")
    time.sleep(2)
    
    driver.switch_to.default_content()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(0.5)
    driver.switch_to.frame(iframe_element)
    time.sleep(1.2)
    
    cds_numero = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id$='21']")))
    cds_numero.send_keys(numero)
    time.sleep(3)
    
    driver.switch_to.default_content()
    time.sleep(1.3)
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(0.4)
    driver.switch_to.frame(iframe_element)
    time.sleep(1.6)
    
    suivantbic = driver.find_element("xpath", "//span[@class='a-button-inner']/input[@name='ppw-widgetEvent:AddAddressEvent']")
    suivantbic.click()
    time.sleep(3)
    
    fin = driver.find_element("xpath", "//span[@class='a-button-inner']/input[@name='ppw-widgetEvent:UseSuggestedAddressEvent']")
    fin.click()
    #ici, amazon nous corrige sur le code postal dans tous les cas, car 75000 n'existe pas.
    time.sleep(2.2)
    
    
    #Nous validons bien les données saisies
    driver.switch_to.default_content()
    time.sleep(1.8)
    driver.execute_script("window.scrollTo(0, 0);")
    toute_fin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-button-inner']/input[@name='ppw-widgetEvent:PreferencePaymentOptionSelectionEvent']")))
    toute_fin.click()
    time.sleep(3)
    
    #Voici enfin le bouton de souscription final:
    findujeu = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'wlp-join-prime-button'))).click()

except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")



driver.quit()

#Fin de la création de compte.


#Création d'une fenêtre avec les informations cruciales à récupérer (ID, et MDP)

import tkinter as tk


def copier_email():
    fenetre.clipboard_clear()  
    fenetre.clipboard_append(e_mail0)  
    fenetre.update()  


def copier_mot_de_passe():
    fenetre.clipboard_clear()  
    fenetre.clipboard_append(mdp0)  
    fenetre.update()  

fenetre = tk.Tk()
fenetre.title("Informations d'accès")


fenetre.geometry("400x200")

label_email = tk.Label(fenetre, text="Adresse électronique:", font=("Arial", 16))
label_email.grid(row=0, column=0, padx=20, pady=5, sticky="w")

entry_email = tk.Entry(fenetre, font=("Arial", 16), width=30)
entry_email.insert(0, e_mail0)
entry_email.grid(row=0, column=1, padx=20, pady=5)

label_mot_de_passe = tk.Label(fenetre, text="Mot de passe:", font=("Arial", 16))
label_mot_de_passe.grid(row=1, column=0, padx=20, pady=5, sticky="w")

entry_mot_de_passe = tk.Entry(fenetre, font=("Arial", 16), width=30)
entry_mot_de_passe.insert(0, mdp0)
entry_mot_de_passe.grid(row=1, column=1, padx=20, pady=5)

#Boutons pour copier les ID et MDP
bouton_copier_email = tk.Button(fenetre, text="Copier l'adresse électronique", command=copier_email)
bouton_copier_email.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

bouton_copier_mot_de_passe = tk.Button(fenetre, text="Copier le mot de passe", command=copier_mot_de_passe)
bouton_copier_mot_de_passe.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

fenetre.mainloop()


#FIN.
