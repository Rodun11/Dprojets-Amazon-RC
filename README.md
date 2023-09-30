# Dprojets-Amazon-RC
Bienvenue dans notre Repository Github, vous y trouverez 3 projets distiguables, tous sur le thème Amazon:

-Un projet de machine learning pour la prédiction de futurs prix, avec le script Projet ML wirtz.py


-Un projet d'automatisation d'alertes mails de mail qui comprend les deux scripts, "amazon_2access.py", et "machine_mail.py"

-Enfin, un projet d'automatisation de création de comptes Prime, usant du script "scriptamazon", voila une video de son usage:

https://youtu.be/hoX6xyMAdQM


# Requirements
pip install -r requirements.txt





Il faudra aussi pour le projet de création de compte prime installer firefox (version 117.0 à 118.0, au choix), et son driver geckodriver version 0.33.0
Voici le lien pour installer le geckodriver: https://github.com/mozilla/geckodriver/releases

# Projet de Machine Learning

Voici un résumé de mon projet de machine learning pour la prédiction des prix sur Amazon, en incluant les principales étapes que j'ai réalisées :

J'ai commencé par collecter un ensemble de données contenant des informations sur les produits vendus sur Amazon, notamment les caractéristiques des produits et leurs prix.

Après la collecte, j'ai effectué un processus de nettoyage des données pour éliminer les valeurs manquantes, supprimer les doublons et corriger les incohérences dans les données (colonne inutile, valeurs non numériques etc...). Cela m'a permis d'obtenir un ensemble de données propre et utilisable pour la suite.

J'ai réalisé une analyse exploratoire des données en utilisant des techniques de visualisation telles que des graphiques, des histogrammes etc. Cela m'a permis de mieux comprendre la distribution des données, les tendances, les corrélations entre les variables et d'identifier les caractéristiques importantes pour la prédiction des prix. 

Voici les techniques que j'ai pu génerer (Certains graphiques sont associés à une sous base que j'ai crée !)

![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/3d1c09e3-e874-47a2-a37d-03259919db48)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/e1278b6c-a260-47d1-a319-4e9e98e71a46)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/21ae4d26-55e5-47b0-80a5-6b1e18f80793)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/0b93e24f-2d5a-4e27-859d-ce70011fdf27)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/4442d43d-9f82-43ff-868e-c8e7b377d05a)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/33b89d9a-9b5f-4e89-a3ea-2ba2f98ee852)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/19724c9c-9124-4cd9-b6c2-83228fb83692)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/37284d34-f6fb-4c81-8b22-6ada52bb0dee)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/38b96d5e-db2a-43e0-a17e-6e80254cbca1)
![image](https://github.com/Rodun11/Dprojets-Amazon-RC/assets/122920318/90cef2d6-87c0-40e1-85f7-b34de523df3d)

J'ai créé de nouvelles caractéristiques (variable "ratings score") à partir des données existantes, par exemple en extrayant des informations à partir du texte des noms de produits.

J'ai divisé mon ensemble de données en deux parties : un ensemble d'entraînement pour former mon modèle de prédiction et un ensemble de test pour évaluer ses performances.

J'ai choisi un algorithme de machine learning approprié pour la régression, tel que la régression linéaire, la forêt aléatoire. Ensuite, j'ai entraîné mon modèle sur l'ensemble d'entraînement en utilisant les caractéristiques que j'ai extraites (les prix et les notes moyennes)

J'ai évalué les performances de mon modèle en utilisant des métriques telles que l'erreur quadratique moyenne (RMSE), l'erreur absolue moyenne (MAE), ou le coefficient de détermination (R²) sur l'ensemble de test. Cela m'a permis de mesurer à quel point mon modèle était capable de prédire avec précision les prix des produits.

Si les performances de mon modèle n'étaient pas satisfaisantes, j'ai ajusté les hyperparamètres (comme la bariable K dans le KNN) et essayé différents algorithmes.

# Projet d'automatisation d'alertes mails:

Il nous faudra ici, tout d'abord dans le premier script (amazon_2access.py) chercher des liens de produits à inserer dans la list nommée URLS que l'on voit au tout début.


Ensuite il faut mettre ses HEADERS personnels, dans headers.


Pour la partie de reglages de seuil, on peut choisir un seuil, qui si il est franchi par un produit donné, nous est alerté par mail.

Nous avons deux choix, soit une baisse de plus d'un certain pourcentage, soit une baisse du prix sous un certain prix fixé.


Exemple pour le pourcentage: Si le prix d'un des produits dans la liste chute de plus de 30% par rapport aux prix auquel il avait été enregistré la première fois qu'il a été run dans le code (liste URLS). Une alerte sera envoyée par mail.

Pour le seuil en euro c'est plus simple à comprendre, si un des produits passe sous la valeur seuil 50euros, un mail est envoyé.

Dans le cadre de choix de ces seuils, il faut saisir le pourcentage seuil dans prctsaisie, et le prix seuil dans set_price.

Si on ne veut pas utiliser de prix seuil, on met set_price = 0. 


Si on ne veut pas de pourcentage seuil, on met prctsaisie = 100.


<a href="https://zupimages.net/viewer.php?id=23/39/qv1g.png"><img src="https://zupimages.net/up/23/39/qv1g.png" alt="" /></a>




Enfin, dans machine_mail, il ne reste plus qu'à mettre ses information de mail dans le script (de "x" à "y"), et les informations de connexion de x.


L'adresse mail x a étée crée spécialement pour l'occasion, et je conseille son usage. Donc il ne faut modifier que le destinataire en mettant son adresse mail. À la place de rboadrian@icloud.com

<a href="https://zupimages.net/viewer.php?id=23/39/ve3u.png"><img src="https://zupimages.net/up/23/39/ve3u.png" alt="" /></a>



Pour faire run le script il faut simplement run le fichier amazon2access.py, qui fera lui-même appel au second.


Si on veut que le script se lance automatiquement toutes les semaines, pour consulter les prix, sur mac et linux, nous pouvons saisir la commande suivante dans le terminal shell:     crontab -e    puis  0 0 * * 0 /path/to/your/script

Sur windows c'est plus difficile, il faut le programmer dans le planificateur de tâches.(Nous pensions au départ que les commandes étaient les mêmes que pour mac).

# Projet de création de comptes primes automatiques:

Vidéo de l'usage: https://youtu.be/hoX6xyMAdQM

Requis: Firefox verision 118.0, et son driver geckodriver version 0.33.0

ATTENTION: L'utilisation de ce script et de ses méthodes paraîssent largement plus risquées, qu'elles ne le sont. Cependant je ne vous oblige à rien, et si vous ne faites confiance à cette méthode, c'est tout à fait votre droit. Surtout qu'il y a peu de chances que le processus fonctionne sous VPN, il faut donc le faire en "découvert".

Le script en quesion contenu dans scriptamazon.py à été optimisé dans le but d'offrir des résultats sûrs à chacune des run dudit code. 

Parfois pendant les créations de comptes amazon et d'abonnement à prime, les temps d'attentes semblerons longs. Nous tenons à vous prévenir, que c'est volontaire, en effet si la saisie d'information se fait trop rapidement, amazon demande une confirmation par numero de téléphone (blocage).

Si vous voyez apparaître cette page "sans bannière" dans la marionette, vous pouvez quitter le driver et relancer le script:
<a href="https://zupimages.net/viewer.php?id=23/39/7nfk.png"><img src="https://zupimages.net/up/23/39/7nfk.png" alt="" /></a>
