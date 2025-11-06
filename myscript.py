import os
import sys

print("--- Lancement du script Git Bisect ---")

good_commit = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bad_commit = "c1a4be04b972b6c17db242fc37752ad517c29402"

# installer les dépendances puis lancer les tests
test_command = "py -m pip install -r requirements.txt && py manage.py test"

# Démarrer git bisect
start_cmd = f"git bisect start {bad_commit} {good_commit}"
print(f"Exécution: {start_cmd}")
os.system(start_cmd)

# Lancer la recherche automatique
run_cmd = f"git bisect run {test_command}"
print(f"Exécution: {run_cmd}")
status = os.system(run_cmd)

# Réinitialiser
os.system("git bisect reset")

# Si git bisect a échoué, faire échouer le workflow
if status != 0:
    print("--- Git Bisect n'a pas pu trouver le commit ---")
    sys.exit(1)

print("--- Git Bisect terminé avec succès ---")