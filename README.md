# Script de post traitement données jPerf
## Le besoin : récupérer des données issues d'une session de transfert UDP sur jPerf. 

Le script est à lancer dans le même dir que le fichier jperf. Pour que ce soit utilisable dans la version actuelle, le fichier est à enregistrer depuis le jPerf Server en rajoutant l'extension *.log

1. Les arguments à l'exécution :
----------------------------------
Le seul argument à passer est le nom du fichier log jperf sans son extension. 

2. Les données de sorties :
----------------------------------

Le script produira un fichier .csv avec une synthèse des paramètres principaux :
- Jitter max
- Bandwidth min
- Bandwidth moyenne
- Paquets perdus
- Ecart type jitter et bandwidth

Il affichera également des courbes de bandwidth et jitter. 

---------------------------------

Ce script est à vocation pédagogique et pourra être optimisé dans le futur. 
