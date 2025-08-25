# On part de l'image officielle de Jenkins
FROM jenkins/jenkins:lts-jdk11

# --- LA CORRECTION EST ICI ---
# On définit le répertoire de travail pour l'utilisateur root
ENV JENKINS_HOME /var/jenkins_home
USER root
WORKDIR /var/jenkins_home

# Installation des dépendances
RUN apt-get update && apt-get install -y lsb-release && rm -rf /var/lib/apt/lists/*
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli

# Création du groupe docker et ajout de l'utilisateur jenkins
RUN groupadd -f docker
RUN usermod -aG docker jenkins

# On reste en 'root' pour l'exécution, mais le répertoire de travail est bien défini
# La ligne USER jenkins n'est plus nécessaire ici car on force l'utilisateur root dans docker-compose