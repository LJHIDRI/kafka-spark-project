# On part de l'image officielle de Jenkins
FROM jenkins/jenkins:lts-jdk11

# On passe en utilisateur "root" pour avoir le droit d'installer des logiciels
USER root

# On met à jour la liste des paquets et on installe les dépendances nécessaires pour Docker
# J'ai ajouté le nettoyage du cache apt avec 'rm -rf' pour optimiser la taille de l'image
RUN apt-get update && apt-get install -y lsb-release && rm -rf /var/lib/apt/lists/*

# Installation du client Docker
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli

# --- LA CORRECTION EST ICI ---
# 1. On crée le groupe 'docker' s'il n'existe pas.
#    Le groupe 'docker' n'est pas créé par l'installation de docker-ce-cli seul.
RUN groupadd -f docker

# 2. On ajoute l'utilisateur 'jenkins' à ce groupe maintenant qu'il existe.
RUN usermod -aG docker jenkins

# On repasse à l'utilisateur "jenkins" pour la sécurité
USER jenkins