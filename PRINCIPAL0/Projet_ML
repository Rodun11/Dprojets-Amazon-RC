# In[ ]: Data loading
import pandas as pd
import numpy as np


# Lien de la base : https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset
# Charger  la base de données depuis le fichier CSV exporté
df = pd.read_csv("C:/Users/chafi/OneDrive/Bureau/M2 DS2E/projet wirtz/Amazon-Products.csv")
df.head()

#visualization libraries
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
sns.set_theme(style="darkgrid")


# In[ ]: Data cleaning

df.duplicated().any()

#supprimer la colonne unnamed inutile
df = df.drop('Unnamed: 0',axis=1)

#On garde que des valeurs numériques pour la colonne ratings
df['ratings'].unique()
dirty_value = ['Get', 'FREE', '₹68.99', '₹65', '₹70','₹100','₹99', '₹2.99']
df['ratings'] = df['ratings'].replace(dirty_value, '0')

#change the column type
df['ratings'] = df['ratings'].astype('float')
df['ratings'].dtypes

#comme c'est des valeurs en milliers, on change la , par rien.
df['no_of_ratings'].unique()
df['no_of_ratings'] = df['no_of_ratings'].replace(',','', regex = True)
df['no_of_ratings'].unique()

#trouver les valeurs non numérique pour ensuite les transformer en 0
non_numeric_values = df.loc[~pd.to_numeric(df['no_of_ratings'], errors='coerce').notna(), 'no_of_ratings']
non_numeric_values.unique()

df['no_of_ratings'] = pd.to_numeric(df['no_of_ratings'], errors='coerce').fillna('0')

df['no_of_ratings'] = df['no_of_ratings'].astype('float')
df['no_of_ratings'].dtypes

#changements necessaire sur la variable discount price.
df.loc[df['discount_price'].str.contains('₹')==True, 'discount_price'] = df.loc[df['discount_price'].str.contains('₹')==True, 'discount_price'].apply(lambda x:x.strip('₹'))

df.loc[df['discount_price'].str.contains(',')==True,'discount_price'] = df.loc[df['discount_price'].str.contains(',')==True,'discount_price'].apply(lambda x:x.replace(',',''))
df['discount_price'].unique()

#chercher les valeurs non numériques
non_numeric_values = df.loc[~pd.to_numeric(df['discount_price'], errors='coerce').notna(), 'discount_price']
non_numeric_values.unique()

df['discount_price'] = df['discount_price'].astype('float')
df['discount_price'].dtypes

#changements necessaire sur la variable actual price.
df.loc[df['actual_price'].str.contains('₹')==True, 'actual_price'] = df.loc[df['actual_price'].str.contains('₹')==True, 'actual_price'].apply(lambda x:x.strip('₹'))
df['actual_price'].unique()

df.loc[df['actual_price'].str.contains(',')==True,'actual_price'] = df.loc[df['actual_price'].str.contains(',')==True,'actual_price'].apply(lambda x:x.replace(',',''))
df['actual_price'].unique()

#chercher les valeurs non numériques
non_numeric_values = df.loc[~pd.to_numeric(df['actual_price'], errors='coerce').notna(), 'actual_price']
non_numeric_values.unique()

df['actual_price'] = df['actual_price'].astype('float')
df['actual_price'].dtypes

#Créer une variable "marque"
df.insert(1, 'manufacturer', df['name'].apply(lambda x:x.split(' ')[0]))#split the rows in the name column on the ' ' space to get the manufacturer names
df.head()

#création d'une nouvelle variable dans notre sous base : discount percentage
df['discount_percentage'] = np.where(df['actual_price']!=0,round((df['actual_price']-df['discount_price'])/df['actual_price'],2),0)
df.head()

#supprimer toute les lignes avec NA
df.isna().sum()
df = df.dropna(subset = ['ratings', 'actual_price', 'discount_price', 'discount_percentage']).reset_index(drop=True)
df.shape

# In[ ]: Data Viz (sur une sous base)

    
#histogramme : Les marques les plus populaires dans df
top_manu = df.groupby('manufacturer',as_index=False).size().sort_values('size',ascending=False)
top_manu

plt.figure(figsize=(12,6))
sns.barplot(data=top_manu[:10], x='manufacturer', y='size',palette='Reds')
plt.title('Popular manufacturer', fontdict={'fontsize':18})
plt.xlabel('manufacturer')
plt.ylabel('size')
plt.show()

# Création de la sous base de donnée + boite à moustache des notes.
ten_manufact = top_manu.iloc[:10]['manufacturer'].to_list() 
top = df[df['manufacturer'].isin(ten_manufact)]

plt.figure(figsize=(8,5))
sns.violinplot(data=top, x='ratings',bins=30)

#Nouvelle variable : discount percentage + batons

top['discount_percentage'] = np.where(top['actual_price']!=0,round((top['actual_price']-top['discount_price'])/top['actual_price'],2),0)
top.head(3)

sns.histplot(data= top,x='discount_percentage')
plt.show()

cat_lst = ('stores', 'accessories','sports & fitness')
ddf = df[df['main_category'].isin(cat_lst)]
sns.displot(data=ddf, x='discount_percentage', col='main_category', kind='hist', kde=True, palette='viridis')

#Histogramme : les catégories les plus populaire dans la sous base
popular_category = top.groupby('main_category',as_index=False).size().sort_values('size',ascending=False)
popular_category

plt.figure(figsize=(10,8))
sns.barplot(data=popular_category, y='main_category', x='size',palette='Blues')
plt.title('Popular category', fontdict={'fontsize':18})
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()
# In[ ]: Data viz sur df

#Nouvelle variable : rating score
rating_score = []
for i in df['ratings']:
    if i < 2.0: rating_score.append('Very unsatified')
    elif i < 3.0: rating_score.append('Unsatified')
    elif i < 4.0: rating_score.append('Neutral')
    elif i < 5.0: rating_score.append('Satified')
    elif i == 5.0: rating_score.append('Very satified')
    
df['rating_score'] = rating_score
df['rating_score'] = df['rating_score'].astype('category')
# Reorder cateories
df['rating_score'] = df['rating_score'].cat.reorder_categories(['Unsatified', 'Neutral', 'Satified','Very satified'], ordered=True)
df.head()

#distributions des notes
plt.figure(figsize=(8,5))
sns.violinplot(data=df, x='ratings',bins=30)


#distribution du pourcentage de reduction
sns.histplot(data= df,x='discount_percentage')
plt.show()


#Histogramme : les catégories les plus populaire dans df 
popular_category = df.groupby('main_category',as_index=False).size().sort_values('size',ascending=False)
popular_category

plt.figure(figsize=(10,8))
sns.barplot(data=popular_category, y='main_category', x='size',palette='Blues')

plt.title('Popular category', fontdict={'fontsize':18})
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()

#plot : quelle catégorie comportent des produits avec le plus de demande ? (df)
plt.figure(figsize=(40,5))
sns.stripplot(data=df, x='main_category', y='no_of_ratings', jitter=0.3)

#Histogramme : les produits sont -ils appréciée par les consommateurs ? (df)
rating_score_pct = df['rating_score'].value_counts(normalize=True).rename_axis('score').reset_index(name='score_pct')
rating_score_pct['score_pct'] = rating_score_pct['score_pct'].round(3)
fig, ax = plt.subplots(1,2, figsize = (15,7))
sns.countplot(ax=ax[0], data=df, x='rating_score')
sns.barplot(ax=ax[1],data = rating_score_pct, x='score', y='score_pct')

ax[0].set_title('Amount of products by Rating Score', fontweight = 'bold')
ax[1].set_title('Percentage of product by Rating Score', fontweight = 'bold')

ax[0].set_xlabel('Rating Score', fontweight = 'bold')
ax[1].set_xlabel('Rating Score', fontweight = 'bold')

ax[0].set_ylabel('Amount', fontweight = 'bold')
ax[1].set_ylabel('Percentage', fontweight = 'bold')

ax[0].bar_label(ax[0].containers[0])
ax[1].bar_label(ax[1].containers[0])
plt.show()



# In[ ]: Machine Learning (price prediction) KNN
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

df.isnull().sum()
X = df[['ratings', 'no_of_ratings', 'actual_price']]
y = df['discount_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Instantiate the model
knnreg = KNeighborsRegressor(n_neighbors=20)

# Fit the model on the training set 
knnreg.fit(X_train, y_train)


# Make prediction on the test set
knnreg.predict(X_test)
y_pred = knnreg.predict(X_test)

# Check the performance of the model
print('R2 score (training): %.2f' % r2_score(y_train, knnreg.predict(X_train)),
      'R2 score (test) %.2f' % r2_score(y_test, y_pred),
      'MSE (test): %.2f' % mean_squared_error(y_test, y_pred), sep='\n')


#####*** Selecting the optimal value of K ****########
training_accuracy = []
test_accuracy = []


# Set n_neighbors from 1 to 20
neighbors_settings = range(1, 20)

for n_neighbors in neighbors_settings:
    # fit the model
    knnreg = KNeighborsRegressor(n_neighbors=n_neighbors)
    knnreg.fit(X_train, y_train)
    # record training set accuracy
    training_accuracy.append(knnreg.score(X_train, y_train))
    # record generalization accuracy
    test_accuracy.append(knnreg.score(X_test, y_test))
    
plt.plot(neighbors_settings, training_accuracy, label='Training')
plt.plot(neighbors_settings, test_accuracy, label='Test')
plt.ylabel('Accuracy [R2]')
plt.xlabel('n-neighbors [K]')
plt.xticks(np.arange(1, 21), labels=[str(i) for i in range(1, 21)])
plt.legend()

# In[ ]: Machine Learning (price prediction) RF

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


# Sélectionner les caractéristiques et la variable cible (sans les variables binaires de catégorie)
X = df[['ratings', 'no_of_ratings', 'actual_price']]
y = df['discount_price']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Créer un modèle de forêts aléatoires (Random Forest)
rf_model = RandomForestRegressor(n_estimators=10, random_state=0)  # Vous pouvez ajuster le nombre d'estimateurs selon vos besoins

# Entraîner le modèle
rf_model.fit(X_train, y_train)

# Faire des prédictions
y_pred = rf_model.predict(X_test)

# Calculez les métriques de performance
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Calcul du pourcentage de bonnes prédictions 
tolerance = 0.05  
correct_predictions = abs(y_pred - y_test) <= tolerance
accuracy = sum(correct_predictions) / len(correct_predictions) * 100

print('R2 score (test): %.2f' % r2_score(y_test, y_pred))
print('MSE (test): %.2f' % mean_squared_error(y_test, y_pred))
print(f'Pourcentage de bonnes prédictions (tolérance {tolerance}): {accuracy:.2f}%')

# In[ ]: Machine Learning (price prediction) SVR

from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Créez un modèle de SVM pour la régression
svm_regressor = SVR(kernel='linear')  # Vous pouvez choisir un noyau (linear, rbf, poly, etc.) approprié

# Entraînez le modèle sur vos données d'entraînement
svm_regressor.fit(X_train, y_train)

# Prédisez les valeurs sur votre jeu de données de test
y_pred = svm_regressor.predict(X_test)

# Calculez le Mean Squared Error (MSE) pour évaluer la performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# Définir les valeurs de n_estimators que vous souhaitez tester
n_estimators_values = [10, 50, 100, 150, 200]  # Vous pouvez ajuster cette liste en fonction de vos besoins

# Initialiser une liste pour stocker les scores R2
r2_scores = []

# Parcourir les différentes valeurs de n_estimators
for n_estimators in n_estimators_values:
    # Créer un modèle de forêts aléatoires avec le nombre d'estimateurs actuel
    rf_model = RandomForestRegressor(n_estimators=n_estimators, oob_score=True, random_state=0)
    
    # Entraîner le modèle
    rf_model.fit(X, y)
    
    # Obtenir l'OOB error (Erreur hors échantillon)
    oob_error = 1 - rf_model.oob_score_
    
    # Ajouter l'OOB error à la liste des scores R2 inversés
    r2_scores.append(1 - oob_error)

# Tracer les résultats
plt.figure(figsize=(10, 6))
plt.plot(n_estimators_values, r2_scores, marker='o', linestyle='-', color='b')
plt.xlabel('Nombre d\'estimateurs (n_estimators)')
plt.ylabel('Score R2 (OOB Error)')
plt.title('Sélection du nombre optimal d\'estimateurs')
plt.grid(True)
plt.show()


# In[ ]: Machine Learning (price prediction) SVM

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

X = df[['ratings', 'no_of_ratings', 'actual_price']]
y = df['discount_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Normaliser les caractéristiques avec StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Créer un modèle SVM de régression
svm_model = SVR(kernel='linear')  # Vous pouvez essayer différents noyaux (linéaire, RBF, polynomial) en fonction de votre tâche

# Entraîner le modèle
svm_model.fit(X_train, y_train)

# Faire des prédictions
y_pred = svm_model.predict(X_test)

# Calculez les métriques de performance
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print('R2 score (test): %.2f' % r2)
print('MSE (test): %.2f' % mse)
print('MAE (test): %.2f' % mae)

import matplotlib.pyplot as plt
import pandas as pd
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.scatter(df['ratings'], df['discount_price'], alpha=0.5)
plt.title('Corrélation entre Ratings et Discount Price')

plt.subplot(132)
plt.scatter(df['no_of_ratings'], df['discount_price'], alpha=0.5)
plt.title('Corrélation entre No. of Ratings et Discount Price')

plt.subplot(133)
plt.scatter(df['actual_price'], df['discount_price'], alpha=0.5)
plt.title('Corrélation entre Actual Price et Discount Price')

plt.tight_layout()
plt.show()

correlation_ratings = df['ratings'].corr(df['discount_price'])
correlation_no_of_ratings = df['no_of_ratings'].corr(df['discount_price'])
correlation_actual_price = df['actual_price'].corr(df['discount_price'])

print(f"Corrélation Ratings vs. Discount Price : {correlation_ratings:.2f}")
print(f"Corrélation No. of Ratings vs. Discount Price : {correlation_no_of_ratings:.2f}")
print(f"Corrélation Actual Price vs. Discount Price : {correlation_actual_price:.2f}")

















