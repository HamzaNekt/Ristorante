import sqlite3
import hashlib

# Connexion à la base de données
connection = sqlite3.connect("restaurant.db")
cursor = connection.cursor()

# Création des tables
cursor.execute("create table employe (employe_id integer, nom text, prenom text, adresse text, telephone text, email text, role text, constraint pk_employe primary key (employe_id))")
cursor.execute("create table users (user_id integer, username text, mdps text, employe_id integer, constraint pk_users primary key (user_id), constraint fk_users foreign key (employe_id) references employe(employe_id))")
cursor.execute("create table tables (numero_de_table integer, capacite integer, constraint pk_table primary key (numero_de_table))")
cursor.execute("create table menu (menu_id integer, nom text, description text, prix real, constraint pk_menu primary key (menu_id))")
cursor.execute("create table commande (commande_id integer, date_commande date, employe_id integer, numero_de_table integer,menu_id integer, constraint fk_commande1 foreign key (employe_id) references employe(employe_id), constraint fk_commande2 foreign key (numero_de_table) references tables(numero_de_table), constraint fk_commande3 foreign key (menu_id) references menu(menu_id))")
cursor.execute("create table paiement (paiement_id integer, montant_total real, mode_paiement text, commande_id integer, constraint fk_paiement foreign key (commande_id) references commande(commande_id))")
cursor.execute("create table fruit (fruit_id integer, nom text, quantite integer, constraint pk_fruit primary key (fruit_id))")
cursor.execute("create table legume (legume_id integer, nom text, quantite integer, constraint pk_legume primary key (legume_id))")
cursor.execute("create table produit_hygiene (produit_hygiene_id integer, nom text, quantite integer, constraint pk_produit_hygiene primary key (produit_hygiene_id))")
cursor.execute ("create table viande (viande_id integer, type_viande text, quantite integer, constraint pk_viande primary key (viande_id))")
cursor.execute ("create table produit_laitier (pl_id integer, type_pl text, quantite integer, constraint pk_produit_laitier primary key (pl_id))")
cursor.execute("create table depense (depense_id integer, nom text, prix_achat real, date_achat date, constraint pk_depense primary key (depense_id))")

# Les informations concernant les tables

# Table employe
employe_records = [
    (1, 'El Amrani', 'Youssef', '28 Rue Ibnou Rochd, Casablanca', '+212652134789', 'youssef.elamrani@email.com', 'Serveur'),
    (2, 'Benjelloun', 'Fatima', '14 Avenue Mohammed V, Rabat', '+212674239812', 'fatima.benjelloun@email.com', 'Cuisinier'),
    (3, 'El Khattabi', 'Omar', '5 Rue Ahmed El Brihi, Marrakech', '+212654987321', 'omar.elkhattabi@email.com', 'Caissier'),
    (4, 'Hassani', 'Nadia', '22 Rue Omar Ibn Al Khattab, Fes', '+212622348907', 'nadia.hassani@email.com', 'Manager'),
    (5, 'Berrada', 'Mounir', '9 Boulevard Mohamed VI, Agadir', '+212690123456', 'mounir.berrada@email.com', 'Serveur'),
    (6, 'El Mahjoubi', 'Amina', '17 Avenue Hassan II, Tanger', '+212698765432', 'amina.elmahjoubi@email.com', 'Cuisinier'),
    (7, 'Chakir', 'Hicham', '12 Rue Abdelkrim El Khattabi, Essaouira', '+212621987654', 'hicham.chakir@email.com', 'Serveur')
]

# Table users

users_records = [
        (1, 'Youssef', hashlib.md5('1111'.encode()).hexdigest()),
        (2, 'Fatima', hashlib.md5('2222'.encode()).hexdigest()),
        (3, 'Omar', hashlib.md5('3333'.encode()).hexdigest()),
        (4, 'Nadia', hashlib.md5('4444'.encode()).hexdigest()),
        (5, 'Mounir', hashlib.md5('5555'.encode()).hexdigest()),
        (6, 'Amina', hashlib.md5('6666'.encode()).hexdigest()),
        (7, 'Hicham', hashlib.md5('7777'.encode()).hexdigest())
    ]


# Table tables
tables_records = [
    (1, 4),
    (2, 6),
    (3, 2),
    (4, 8),
    (5, 4),
    (6, 6),
    (7, 3),
    (8, 5),
    (9, 10),
    (10, 2)
]

# Table fruit
fruit_records = [
    (1, 'Pomme', 13, 50),
    (2, 'Banane', 10, 40),
    (3, 'Orange', 5, 120),
    (4, 'Fraise', 12, 50),
    (5, 'Kiwi', 17, 50),
    (6, 'Ananas', 20, 40),
    (7, 'Mangue', 10, 30),
    (8, 'Raisin', 7, 70),
    (9, 'Poire', 8, 50),
    (10, 'Cerise', 10, 40)
]

# Table legume
legume_records = [
    (1, 'Tomate', 8, 200),
    (2, 'Carotte', 6, 150),
    (3, 'Courgette', 7, 120),
    (4, 'Poivron', 7, 100),
    (5, 'Aubergine', 7, 80),
    (6, 'Haricot vert', 6, 150),
    (7, 'Chou-fleur', 5, 60),
    (8, 'Brocoli', 14, 70),
    (9, 'Radis', 12, 180),
    (10, 'Pomme de terre', 7, 200)
]

# Table produit_d'hygiene
produit_hygiene_records = [
    (1, 'Savon liquide', 12, 50),
    (2, 'Degraissant cuisine', 15, 20),
    (3, 'Nettoyant pour vitres', 13, 30),
    (4, 'Papier toilette', 48, 20),
    (5, 'Lessive', 80, 20),
    (6, 'Desinfectant multi-surfaces', 35, 30),
    (7, 'Serviettes en papier', 22, 100),
    (8, 'Éponge', 10, 80),
    (9, 'Essuie-tout', 19, 30),
    (10, 'Desodorisant pour toilettes', 20, 10)
]


# Table menu
menu_records = [
    # Pizzas
    (1, 'Pizza Margherita', 'Tomate, mozzarella, basilic', 50),
    (2, 'Pizza viande hachée', 'Tomate, mozzarella, viande hachée', 40),
    (3, 'Pizza Quatre fromages', 'Tomate, mozzarella, gorgonzola, emmental, parmesan', 45),
    (4, 'Pizza Végétarienne', 'Tomate, mozzarella, légumes grillés', 40),

    # Paninis
    (5, 'Panini Classique', 'Poulet, fromage, tomate', 30),
    (6, 'Panini Végétarien', 'Légumes grillés, fromage de chèvre', 25),
    (7, 'Panini Thon', 'Thon, mayonnaise, salade', 25),
    (8, 'Panini viande hachée', 'viande hachée, fromage, salade', 20),

    # Tacos
    (9, 'Tacos Poulet', 'Poulet grillé, frites, fromage, sauce au choix', 35),
    (10, 'Tacos Bœuf', 'Viande de bœuf, frites, cheddar, sauce piquante',  30),
    (11, 'Tacos Végétarien', 'Légumes grillés, frites, fromage, sauce blanche', 25),
    (12, 'Tacos Mixte', 'Poulet, bœuf, frites, fromage, sauce au choix', 30),

    # Boissons
    (13, 'Boisson Coca-Cola', '33cl', 10),
    (14, 'Boisson Eau minérale', '50cl', 8),
    (15, 'Boisson Jus d\'orange', '25cl', 13),
    (16, 'Boisson Thé glacé', '33cl', 12),

    # Desserts
    (17, 'milk shake Fraise', 'Fraise, lait', 30),
    (18, 'milk shake Mangue', 'Mangue, lait', 35),
    (19, 'milk shak Banane', 'Banane, lait',  20),
    (20, 'milk shake Cerise', 'Cerise, lait', 25)
]


# Table viande
viande_records = [
    (1, 'Viande hachée', 10.0, 50),
    (2, 'Poulet', 8.0, 40),
    (3, 'Bœuf', 12.0, 30)
]


# Table produit_laitier
produit_laitier_records = [
    (1, 'Lait', 2.5, 100),
    (2, 'Mozzarella', 7.0, 20),
    (3, 'Fromage', 8.5, 30)
]


# Insertion des enregistrements dans les tables

# Table employe
cursor.executemany("INSERT INTO employe VALUES (?, ?, ?, ?, ?, ?, ?)", employe_records)

# TAble users
cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users_records)

# Table tables
cursor.executemany("INSERT INTO tables VALUES (?, ?)", tables_records)

# Table fruit
cursor.executemany("INSERT INTO fruit VALUES (?, ?, ?)", fruit_records)

# Table legume
cursor.executemany("INSERT INTO legume VALUES (?, ?, ?)", legume_records)

# Table produit_hygiene
cursor.executemany("INSERT INTO produit_hygiene VALUES (?, ?, ?)", produit_hygiene_records)

# Table menu
cursor.executemany("INSERT INTO menu VALUES (?, ?, ?, ?)", menu_records)

# Table viande
cursor.executemany("INSERT INTO viande VALUES (?, ?, ?)", viande_records)

# Table produit_laitier
cursor.executemany("INSERT INTO produit_laitier VALUES (?, ?, ?)", produit_laitier_records)


# Validation des modifications et fermeture de la connexion
connection.commit()
connection.close()
