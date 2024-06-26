import hashlib
import sqlite3

# Fonction pour hacher le mot de passe
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Fonction pour vérifier le mot de passe
def verify_password(username, password):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()

    cursor.execute("SELECT mdps FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        hashed_password = result[0]
        input_hashed = hashlib.md5(password.encode()).hexdigest()
        return hashed_password == input_hashed
    else:
        return False
    
    connection.close()

















if __name__ == "__main__":
    # Demander à l'utilisateur de saisir le nom d'utilisateur et le mot de passe
    username = input("Entrez votre nom d'utilisateur : ")
    password = input("Entrez votre mot de passe : ")

    # Vérifier le mot de passe
    if verify_password(username, password):
        print(f"Connexion réussie pour l'utilisateur {username}.")
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")







employe_id =  'HAD' 
nom =        'LES'
prenom =      'VARIABLES'
adresse =     'RANJIBOHOM'
telephone =   'MN'
email =      'L FRONT'
role =        'MN L interface'
password =    'dial OWNER'





# Fonction pour ajouter un employé
def add_employee(employe_id, nom, prenom, adresse, telephone, email, role, password):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()

    try:
        # Insertion dans la table employe
        cursor.execute("INSERT INTO employe VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (employe_id, nom, prenom, adresse, telephone, email, role))

        # Hachage du mot de passe
        hashed_password = hash_password(password)

        # Insertion dans la table users
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)",
                       (employe_id, username, hashed_password))

        connection.commit()
        print(f"L'employé {nom} {prenom} a été ajouté avec succès.")
    except sqlite3.Error as error:
        print(f"Erreur lors de l'ajout de l'employé : {error}")
    finally:
        connection.close()





nom =       'NFS'
password =  'L7AJA HNA'



# Fonction pour supprimer un employé
def delete_employee(nom, password):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()

    try:
        # Vérifier le mot de passe haché
        hashed_password = hash_password(password)

        # Suppression dans la table employe et users
        cursor.execute("DELETE FROM employe, users WHERE employe.employe_id = users.employe_id AND nom = ? AND mdps = ?",
                       (nom, hashed_password))

        if cursor.rowcount > 0:
            connection.commit()
            print(f"L'employé {nom} a été supprimé avec succès.")
        else:
            print(f"Aucun employé trouvé avec le nom {nom} et le mot de passe fourni.")
    except sqlite3.Error as error:
        print(f"Erreur lors de la suppression de l'employé : {error}")
    finally:
        connection.close()








nom = 'mn l''interface'
quantite = 'mn l fournisseur'

# Actualiser la quantité dans la table fruit
def update_fruit_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE fruit SET quantite = quantite + ? WHERE nom = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès.")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table fruit : {error}")
    finally:
        connection.close()









nom = 'mn l''interface'
quantite = 'mn l fournisseur'

# Actualiser la quantité dans la table legume
def update_legume_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE legume SET quantite = quantite + ? WHERE nom = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès.")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table legume : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l fournisseur'

# Actualiser la quantité dans la table produit_hygiene
def update_produit_hygiene_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE produit_hygiene SET quantite = quantite + ? WHERE nom = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès.")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table produit_hygiene : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l fournisseur'

# Actualiser la quantité dans la table viande
def update_viande_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE viande SET quantite = quantite + ? WHERE type_viande = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès.")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table viande : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l fournisseur'

# Actualiser la quantité dans la table produit_laitier
def update_produit_laitier_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE produit_laitier SET quantite = quantite + ? WHERE type_pl = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès.")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table produit_laitier : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l manager'

        # Fonction pour actualiser la quantité dans la table fruit
def subtract_fruit_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE fruit SET quantite = quantite - ? WHERE nom = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès (soustraction de {quantite}).")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table fruit : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l manager'

# Fonction pour actualiser la quantité dans la table legume
def subtract_legume_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE legume SET quantite = quantite - ? WHERE nom = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès (soustraction de {quantite}).")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table legume : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l manager'

# Fonction pour actualiser la quantité dans la table produit_hygiene
def subtract_produit_hygiene_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE produit_hygiene SET quantite = quantite - ? WHERE nom = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès (soustraction de {quantite}).")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table produit_hygiene : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l manager'

# Fonction pour actualiser la quantité dans la table viande
def subtract_viande_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE viande SET quantite = quantite - ? WHERE type_viande = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès (soustraction de {quantite}).")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table viande : {error}")
    finally:
        connection.close()







nom = 'mn l''interface'
quantite = 'mn l manager'

# Fonction pour actualiser la quantité dans la table produit_laitier
def subtract_produit_laitier_quantity(nom, quantite):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE produit_laitier SET quantite = quantite - ? WHERE type_pl = ?", (quantite, nom))
        connection.commit()
        print(f"Quantité de {nom} mise à jour avec succès (soustraction de {quantite}).")
    except sqlite3.Error as error:
        print(f"Erreur lors de la mise à jour de la quantité dans la table produit_laitier : {error}")
    finally:
        connection.close()