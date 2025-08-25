# On part de l'image officielle de Jenkins
FROM jenkins/jenkins:lts-jdk11

# On passe en utilisateur "root" pour avoir le droit d'installer des logiciels
USER root

# On met à jour la liste des paquets et on installe les dépendances nécessaires pour Docker
RUN apt-get update && apt-get install -y lsb-release && rm -rf /var/lib/apt/lists/*
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli

# Important : On donne à l'utilisateur "jenkins" le droit d'utiliser Docker
RUN usermod -aG docker jenkins

# On repasse à l'utilisateur "jenkins" pour la sécurité
USER jenkins