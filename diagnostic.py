# 1. Variables de présentation et de choix du service
nom_client = "Hadji"
type_service = "diagnostic"  # Options possibles : "diagnostic", "entretien", "recherche_panne"

# 2. Calcul du tarif avec des conditions (if / elif / else)
if type_service == "diagnostic":
    prix = 50
    description = "Diagnostic électronique complet"
elif type_service == "entretien":
    prix = 80
    description = "Entretien courant et vidange"
elif type_service == "recherche_panne":
    prix = 70
    description = "Recherche de panne électrique"
else:
    prix = 0
    description = "Service inconnu"

# 3. Affichage du résultat avec une f-string
print(f"Client : {nom_client}")
print(f"Prestation sélectionnée : {description}")
print(f"Tarif estimé 2H-DIAG HM : {prix} €")