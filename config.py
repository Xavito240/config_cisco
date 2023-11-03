import paramiko
import time

# Informations d'authentification SSH
hostname = ' '
port = 22
username = ' '
password = ' '
enable_password = ' '

# Commandes à exécuter pour modifier la configuration du port 1
commands = [
    'enable',
    'conf t',
    'interface FastEthernet0/1',
    'switchport access vlan 20',
    'end'
]

# Connexion SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)

# Exécution des commandes
shell = client.invoke_shell()
for command in commands:
    shell.send(command + '\n')
    time.sleep(1)  # Attente d'une seconde pour laisser le temps au commutateur de répondre

# Récupération de la sortie de l'exécution des commandes
output = shell.recv(4096).decode('utf-8')

# Affichage de la sortie de l'exécution des commandes
print(output)

# Fermeture de la connexion SSH
client.close()
