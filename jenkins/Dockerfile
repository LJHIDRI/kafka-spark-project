# On part de l'image officielle de Jenkins
FROM jenkins/jenkins:lts-jdk11

# On passe en root pour installer
USER root

# Installation des dépendances Docker
RUN apt-get update && apt-get install -y lsb-release && rm -rf /var/lib/apt/lists/*
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli

# Il n'est plus nécessaire de gérer les groupes ou de repasser à l'utilisateur jenkins,
# car docker-compose va forcer l'utilisateur 'root' à l'exécution.