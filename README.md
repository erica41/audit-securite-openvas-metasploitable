Audit de sécurité automatisé — OpenVAS/GVM sur Metasploitable

Projet de substitution au stage — Formation Réseaux & Cybersécurité, ECE Paris (B3, année 2025-2026)
Contexte

Ce projet a pour objectif d'automatiser un audit de sécurité sur un site web à l'aide de la suite open source OpenVAS/GVM (Greenbone Vulnerability Management), en s'appuyant sur son API GMP et la bibliothèque Python python-gvm.

L'environnement de test est composé de :

Kali Linux — hébergeant l'installation OpenVAS/GVM (scanner)
Metasploitable 2 — machine virtuelle volontairement vulnérable, utilisée comme cible, hébergeant plusieurs applications web faillibles (TWiki, phpMyAdmin, DVWA...)
Technologies utilisées
Kali Linux — Système hôte du scanner
OpenVAS / GVM — Scanner de vulnérabilités
VirtualBox — Virtualisation de l'environnement de test
Metasploitable 2 — Cible du scan
Python 3 / python-gvm — Automatisation via l'API GMP
Contenu du dépôt
test_connexion.py — Vérifie l'authentification et la connexion à l'API GMP
test_targets.py — Liste les cibles existantes via l'API
test_configs.py — Liste les scan configs disponibles
creer_lancer_scan.py — Crée automatiquement une tâche de scan et la lance
report-*.pdf — Rapport complet du scan exporté depuis OpenVAS (résultats détaillés)
Comment exécuter les scripts

Prérequis :

OpenVAS/GVM installé et configuré sur une machine Kali Linux (ou équivalent Debian)
Bibliothèque python-gvm installée : pip install python-gvm
Une cible de scan déjà créée dans OpenVAS (voir section suivante pour l'ID à renseigner)

Étapes :

python3 test_connexion.py
python3 test_targets.py
python3 creer_lancer_scan.py

Les scripts se connectent à GVM via le socket Unix local (/run/gvmd/gvmd.sock), ils doivent donc être exécutés directement sur la machine hébergeant l'installation GVM.

Résultats obtenu

Le scan a identifié 632 résultats bruts, dont 68 jugés pertinents après filtrage par qualité de détection (QoD ≥ 70%), incluant plusieurs vulnérabilités critiques telles que :

Backdoor Ingreslock (10.0 Critical)
TWiki — exécution de commande à distance (10.0 Critical)
Apache Tomcat AJP RCE / Ghostcat (9.8 Critical)
MySQL/MariaDB — identifiants par défaut (9.8 Critical)

Le rapport complet est disponible dans ce dépôt au format PDF.
