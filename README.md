# README - Script d'Exécution de Commandes via SSH

Ce fichier README fournit des informations sur l'utilisation du script Python pour exécuter des commandes via SSH sur un équipement réseau à l'aide de la bibliothèque Paramiko.

**Créateur :** @Xavito

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir installé la bibliothèque Paramiko. Vous pouvez l'installer à l'aide de pip :

```bash
pip install paramiko
```

## Configuration du Script

Le script nécessite plusieurs informations d'authentification pour se connecter à l'appareil distant. Vous devez remplir les informations suivantes dans le script :

- `hostname`: L'adresse IP ou le nom d'hôte de l'appareil distant auquel vous souhaitez vous connecter.
- `port`: Le port SSH à utiliser (par défaut, le port 22 est généralement utilisé pour SSH).
- `username`: Votre nom d'utilisateur SSH pour l'appareil distant.
- `password`: Votre mot de passe SSH pour l'appareil distant.
- `enable_password`: Le mot de passe d'activation (si nécessaire) pour accéder au mode d'exécution privilégié (enable).

## Commandes à Exécuter

Vous devez spécifier les commandes que vous souhaitez exécuter sur l'appareil distant dans la liste `commands`. Par exemple, les commandes suivantes sont fournies en exemple :

```python
commands = [
    'enable',
    'conf t',
    'interface FastEthernet0/1',
    'switchport access vlan 20',
    'end'
]
```

Assurez-vous d'adapter ces commandes en fonction de vos besoins. Chaque élément de la liste correspond à une commande à exécuter, et elles seront exécutées séquentiellement.

## Utilisation du Script

Une fois que vous avez configuré les informations d'authentification et les commandes, vous pouvez exécuter le script en utilisant Python. Assurez-vous que le script est dans le même répertoire que votre projet ou spécifiez le chemin absolu vers le script. Exécutez le script de la manière suivante :

```bash
python nom_du_script.py
```

Le script se connectera à l'appareil distant, exécutera les commandes spécifiées, attendra une seconde entre chaque commande pour permettre au commutateur de répondre, récupérera la sortie de l'exécution des commandes, puis l'affichera.

## Note

Assurez-vous de respecter les règles de sécurité et d'obtenir les autorisations nécessaires pour exécuter ce script sur des équipements réseau. La mauvaise utilisation de ce script peut causer des problèmes et perturber le réseau. Utilisez-le avec précaution.

N'hésitez pas à personnaliser ce script en fonction de vos besoins spécifiques en matière de configuration d'appareils réseau via SSH.

**@Xavito**
