def init():
    global words
    global games
    global debug
    global color
    global reaction_messages
    global number_emojis

    words = { 'paix', 'page', 'nez', 'carre', 'attention', 'humide', 'singe', 'cave', 'bassine', 'barbe', 'panneau', 'moins', 'moteur', 'barreau', 'cerf', 'manege', 'flamme', 'ouverture', 'seche', 'moto', 'gomme', 'coup', 'quartier', 'dur', 'ligne', 'coccinelle', 'vitesse', 'exterieur', 'serre', 'ville', 'alphabet', 'pullover', 'fontaine', 'ecriture', 'virage', 'noeud', 'mouche', 'verser', 'trouver', 'bretelle', 'soldat', 'mieux', 'garcon', 'conduite', 'poursuite', 'eglise', 'autour', 'boeuf', 'sortie', 'decollage', 'roue', 'pieds', 'inondation', 'atterrissage', 'vehicule', 'mine', 'serpent', 'sac', 'plastique', 'portemanteau', 'savon', 'couleur', 'conte', 'ours', 'promenade', 'crochet', 'fort', 'bain', 'etroit', 'sourire', 'parcours', 'corps', 'maillot', 'ensemble', 'sur', 'prenom', 'radiateur', 'tricot', 'bois', 'genou', 'fil', 'meme', 'cagoule', 'poche', 'elastique', 'ciseaux', 'musique', 'micro', 'ouvrier', 'dedans', 'tissu', 'chateau', 'bille', 'pneu', 'envers', 'ecole', 'tot', 'beurre', 'etagere', 'melange', 'enveloppe', 'aiguille', 'tabouret', 'faute', 'point', 'fonce', 'corde', 'poulet', 'nain', 'sauvetage', 'rangee', 'papier', 'lame', 'poisson', 'car', 'grand', 'soupe', 'fleuriste', 'tige', 'toujours', 'guepe', 'frein', 'porte', 'nu', 'trop', 'cinema', 'coude', 'dictionnaire', 'reine', 'pierre', 'rouge', 'cuvette', 'ressemblance', 'four', 'mixer', 'dix', 'suivre', 'appetit', 'boulanger', 'ferme', 'paire', 'vite', 'fou', 'faim', 'haut', 'feuille', 'bibliotheque', 'square', 'gentil', 'savoir', 'hippopotame', 'echelle', 'souvent', 'devant', 'arrosoir', 'film', 'cassette', 'naissance', 'chaud', 'vis', 'idee', 'echarpe', 'sole', 'pardon', 'difference', 'rape', 'coiffeur', 'cracher', 'camarade', 'handicape', 'nombre', 'petit', 'boue', 'crocodile', 'colere', 'cru', 'bourgeon', 'fusil', 'blanc', 'un', 'montagne', 'facile', 'poste', 'saut', 'fille', 'lezard', 'terrain', 'bassin', 'cage', 'mie', 'escargot', 'loup', 'trait', 'aile', 'aigle', 'lire', 'monde', 'graines', 'fleche', 'brun', 'chapeau', 'flaque', 'fusee', 'pion', 'bas', 'oreille', 'chanson', 'carrefour', 'ascenseur', 'sel', 'etude', 'helicoptere', 'dangereux', 'foin', 'appartement', 'meilleur', 'garage', 'travaux', 'gare', 'arret', 'cabane', 'encore', 'wagon', 'gymnastique', 'chemise', 'arrivee', 'chute', 'recette', 'interessant', 'boite', 'bonnet', 'noyau', 'robinet', 'terre', 'terrier', 'course', 'rugueux', 'destruction', 'toboggan', 'joli', 'large', 'ordre', 'jus', 'tortue', 'dauphin', 'bouton', 'accident', 'volet', 'groupe', 'clocher', 'croquer', 'coloriage', 'milieu', 'telephone', 'gros', 'animaux', 'montre', 'vide', 'chez', 'lettre', 'immobile', 'vetement', 'pot', 'cache', 'galette', 'train', 'usine', 'presque', 'travail', 'barbouille', 'col', 'frite', 'graine', 'trompette', 'tasse', 'histoire', 'important', 'liste', 'aller', 'casier', 'cheville', 'livre', 'fatigue', 'seau', 'mouton', 'pedale', 'bosser', 'carton', 'contraire', 'camion', 'sable', 'rampe', 'propre', 'mince', 'long', 'poignet', 'miel', 'fumer', 'cloche', 'metre', 'sonnette', 'lisse', 'arriere', 'muet', 'cravate', 'deux', 'moineau', 'telecommande', 'premier', 'crayon', 'rentree', 'zigzag', 'chaises', 'multicolore', 'disparition', 'jaloux', 'mouille', 'tunnel', 'herisson', 'assiette', 'mal', 'scie', 'suivant', 'hamster', 'toilette', 'tambour', 'cocotte', 'numero', 'mur', 'chuchotement', 'cochon', 'requin', 'croix', 'parc', 'brouette', 'panne', 'tete', 'arete', 'envie', 'lavabo', 'quatre', 'bureau', 'mot', 'caillou', 'jeu', 'bleu', 'pointu', 'manteau', 'monument', 'radio', 'fesse', 'puree', 'calme', 'linge', 'crapaud', 'cartable', 'avion', 'cuillere', 'allumer', 'foire', 'decoupage', 'construction', 'neuf', 'palais', 'paquet', 'eau', 'barre', 'lecture', 'matelas', 'tiroir', 'noir', 'ruban', 'cube', 'vivant', 'beaucoup', 'tranquille', 'croute', 'tournevis', 'chien', 'prudent', 'coquille', 'taupe', 'chaussure', 'botte', 'plafond', 'voiture', 'sommeil', 'perroquet', 'plume', 'collant', 'ecran', 'adroit', 'lit', 'poing', 'courrier', 'zoo', 'photographie', 'pain', 'dos', 'litre', 'venir', 'ver', 'panthere', 'magicien', 'malade', 'pharmacie', 'interieur', 'hopital', 'ampoule', 'cuit', 'cygne', 'habit', 'betes', 'obligation', 'curieux', 'moitie', 'tour', 'chouette', 'ceinture', 'enceinte', 'toit', 'crepes', 'calin', 'rond', 'passerelle', 'droit', 'rhinoceros', 'caravane', 'pharmacien', 'cheminee', 'domino', 'bicyclette', 'droite', 'hotel', 'enorme', 'rat', 'parking', 'pompier', 'trousse', 'armoire', 'uniforme', 'derriere', 'promesse', 'ordinateur', 'affaire', 'different', 'personne', 'fourmi', 'valise', 'oie', 'robe', 'bien', 'yeux', 'vache', 'effort', 'carnet', 'bricolage', 'passage', 'vers', 'manche', 'troisieme', 'rayon', 'feutre', 'part', 'mure', 'rayure', 'xylophone', 'pareil', 'nom', 'pinceau', 'marteau', 'escalade', 'moufle', 'salle', 'jouet', 'ami', 'allumette', 'etiquette', 'cinq', 'maladroit', 'cerceau', 'bruit', 'langue', 'patte', 'la', 'peur', 'voix', 'perle', 'changer', 'present', 'arc', 'veterinaire', 'essence', 'branche', 'recreation', 'gout', 'yaourt', 'moulin', 'champ', 'dessus', 'baguette', 'pied', 'morceau', 'impossible', 'ane', 'patisserie', 'piscine', 'chevre', 'roi', 'pigeon', 'meuble', 'danger', 'etang', 'doux', 'froid', 'gouttes', 'escalier', 'boulangerie', 'jouer', 'griffe', 'dessert', 'restaurant', 'classe', 'stylo', 'mains', 'gauche', 'pate', 'table', 'engin', 'moule', 'immense', 'renard', 'appel', 'plier', 'auto', 'gris', 'pamplemousse', 'carreau', 'paille', 'os', 'modele', 'instrument', 'poussin', 'intrus', 'immeuble', 'trois', 'acrobate', 'pelle', 'gouter', 'dossier', 'pomme', 'tapis', 'bande', 'insecte', 'voisin', 'dame', 'bout', 'jamais', 'grenouille', 'boucherie', 'casse', 'cabinet', 'separer', 'roux', 'balancoire', 'tracteur', 'cahier', 'rondelle', 'blond', 'cou', 'huit', 'bete', 'dessous', 'mort', 'levres', 'sol', 'catalogue', 'carte', 'eleve', 'sept', 'cote', 'riviere', 'glacon', 'partie', 'mare', 'court', 'bouteille', 'souligner', 'mensonge', 'assis', 'pouce', 'moyen', 'poule', 'bras', 'pas', 'solide', 'equipe', 'jambes', 'entree', 'campagne', 'caresse', 'sieste', 'six', 'prairie', 'copain', 'jaune', 'teter', 'coin', 'louche', 'prince', 'planche', 'oiseau', 'peluche', 'madame', 'place', 'pilote', 'doigts', 'mechant', 'directrice', 'contre', 'dessin', 'image', 'chiffre', 'maitresse', 'retard', 'doigt', 'souple', 'bouche', 'poli', 'pente', 'album', 'rouleau', 'depart', 'fumee', 'incendie', 'agneau', 'debout', 'chaine', 'platre', 'chenille', 'chaussette', 'silence', 'cle', 'boutique', 'poutre', 'village', 'peu', 'objet', 'chat', 'craie', 'ongle', 'nouveau', 'marionnette', 'peinture', 'soif', 'panda', 'chauffer', 'oeuf', 'puzzle', 'sifflet', 'tuyau', 'route', 'animal', 'serieux', 'lion', 'vitre', 'charger', 'chaise', 'photo', 'cadenas', 'difficile', 'tableau', 'bulles', 'amuser', 'dessiner', 'pont', 'sens', 'zero', 'semelle', 'face', 'bagarre', 'outil', 'rateau', 'odeur', 'jean', 'ventre', 'policier', 'pointe', 'culotte', 'cuisse', 'velo', 'plante', 'ficelle', 'maigre', 'hanche', 'coucher', 'demi', 'maison', 'assez', 'escabeau', 'abime', 'rideau', 'tranche', 'tordu', 'douche', 'embouteillage', 'casquette', 'saladier', 'pluie', 'invitation', 'sorciere', 'tard', 'appareil', 'grue', 'quai', 'seul', 'cour', 'police', 'siege', 'lunettes', 'plus', 'directeur', 'gobelet', 'facteur', 'fee', 'bouchon', 'bondir', 'maternelle', 'pyjama', 'marche', 'enerve', 'cigarette', 'utile', 'cheval', 'sous', 'enfant', 'mousse', 'herbe', 'apres', 'rose', 'tendre', 'roulade', 'egal', 'ballon', 'avant', 'use', 'coquelicot', 'maitre', 'endroit', 'tas', 'entier', 'salir', 'forme', 'feve', 'lacet', 'balcon', 'transparent', 'epaule', 'pantalon', 'lapin', 'sale', 'sport', 'fond', 'dejeuner', 'fermier', 'veste', 'colis', 'titre', 'vert', 'tigre', 'pliage', 'jambon', 'couche', 'voyage', 'bec', 'potage', 'magnetoscope', 'casque', 'jupe', 'pompe', 'abeille', 'abandonne', 'laisse', 'vouloir', 'autant', 'girafe', 'dehors', 'elephant', 'magazine', 'sourd', 'radis', 'loin', 'absent', 'fenetre', 'banc', 'coeur', 'ecureuil', 'couronne', 'mouchoir', 'clair', 'tulipe', 'couloir', 'chose', 'ancien', 'epluchure', 'caisse', 'gant', 'liquide', 'raquette', 'zebre', 'epais', 'poney', 'tarte', 'prises', 'bizarre', 'clou', 'rater', 'ici', 'legume', 'tache', 'cigogne', 'arbre', 'epee', 'araignee', 'cirque', 'mauvais', 'fois', 'equilibre', 'anniversaire', 'colline', 'amusant', 'consomme', 'timbre', 'tricycle', 'colle', 'aquarium', 'tampon', 'visiter', 'metal', 'hibou', 'jardin', 'fleur', 'clown', 'poubelle', 'bateau', 'signe', 'pli', 'placard', 'gardien', 'bouquet', 'affiche', 'serrure', 'chanteur', 'verre', 'adresse', 'grain', 'serviette', 'plongeoir', 'barque', 'casserole', 'angle', 'sec', 'dindon', 'bagage', 'talon', 'kiwi', 'canard', 'taille', 'danser', 'orchestre', 'muscle', 'profond', 'main', 'question', 'balle', 'laine', 'sage', 'coq', 'feu', 'dernier', 'bebe', 'trous', 'aeroport', 'medicament', 'bus', 'bord', 'gateau', 'magie', 'filet', 'entonnoir', 'chariot', 'pres', 'dans', 'jonquille', 'deuxieme', 'gourmand', 'magasin', 'souris', 'television', 'deltaplane' }
    games = {}
    debug = False
    color = 0x880088
    reaction_messages = []
    number_emojis = [ "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣" ,"🔟" ]
