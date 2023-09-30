# Dprojets-Amazon-RC
Bienvenue dans notre Repository Github, vous y trouverez 3 projets distiguables, tous sur le thème Amazon:
-Un projet de machine learning "..."
-Un projet d'automatisation d'alertes mails de mail qui comprend les deux scripts, "amazon_2access.py", et "machine_mail.py"
-Enfin, un projet d'automatisation de création de comptes Prime, usant du script "scriptamazon".


# Requirements
pip install -r requirements.txt





Il faudra aussi pour le projet de création de compte prime installer firefox (version 117.0 à 118.0, au choix), et son driver geckodriver version 0.33.0
Voici le lien pour installer le geckodriver: https://github.com/mozilla/geckodriver/releases

# Projet de Machine Learning
...




# Projet d'automatisation d'alertes mails:

Il nous faudra ici, tout d'abord chercher des liens de produits à inserer dans la list nommée URLS que l'on voit au tout début.


Ensuite il faut mettre ses HEADERS personnels, dans headers.


Pour la partie de reglages de seuil, on peut choisir un seuil, qui si il est franchi par un produit donné, nous est alerté par mail.

Nous avons deux choix, soit une baisse de plus d'un certain pourcentage, soit une baisse du prix sous un certain prix fixé.


Exemple pour le pourcentage: Si le prix d'un des produits dans la liste chute de plus de 30% par rapport aux prix auquel il avait été enregistré la première fois qu'il a été run dans le code (liste URLS). Une alerte sera envoyée par mail.

Pour le seuil en euro c'est plus simple à comprendre, si un des produits passe sous la valeur seuil 50euros, un mail est envoyé.

Dans le cadre de choix de ces seuils, il faut saisir le pourcentage seuil dans prctchoisi, et le prix seuil dans 


![imagealerte]([url=https://zupimages.net/viewer.php?id=23/39/qv1g.png][img]https://zupimages.net/up/23/39/qv1g.png[/img][/url])
