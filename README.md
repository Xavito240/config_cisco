# config_cisco
Bien sûr, voici le modèle complet de fichier "README.md" que vous pouvez copier-coller :

```markdown
# Script Python d'exécution de commandes SSH avec Paramiko

Ce script Python permet d'établir une connexion SSH avec un appareil réseau et d'exécuter des commandes SSH sur cet appareil. Il utilise la bibliothèque Paramiko pour gérer la connexion SSH.

## Utilisation

Avant d'utiliser ce script, assurez-vous d'avoir installé la bibliothèque Paramiko en utilisant la commande suivante :

```bash
pip install paramiko
```

Assurez-vous également de remplir correctement les informations d'authentification et d'adapter les commandes à celles que vous souhaitez exécuter sur votre appareil réseau. Les étapes suivantes décrivent comment utiliser le script :

1. Remplissez les informations d'authentification SSH dans le script en modifiant les valeurs des variables suivantes :

```python
hostname = ''
port = 22
username = ''
password = ''
enable_password = ''
```

2. Spécifiez les commandes que vous souhaitez exécuter en les ajoutant à la liste `commands`. Par exemple, vous pouvez ajouter des commandes de configuration réseau spécifiques.

```python
commands = [
    'enable',
    'conf t',
    'interface FastEthernet0/1',
    'switchport access vlan 20',
    'end'
]
```

3. Exécutez le script en utilisant la commande suivante :

```bash
python ssh_script.py
```

Le script se connectera à l'appareil réseau, exécutera les commandes spécifiées et affichera la sortie.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce script ou corriger des erreurs, n'hésitez pas à créer une demande de tirage (pull request) ou à signaler des problèmes (issues) sur GitHub.

## Licence

Ce projet est sous licence [insérez la licence de votre choix, par exemple, MIT, Apache, GNU, etc.].

---
[© Votre nom ou nom de l'organisation] - [Lien vers votre site web ou profil GitHub]
```

Vous pouvez copier-coller ce modèle dans un fichier "README.md" sur GitHub, en veillant à personnaliser les informations spécifiques à votre projet.
