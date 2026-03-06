import sys
import locale
import time
from google import genai

# --- CONFIGURATION ---
# Remplace par ta clé API réelle
API_KEY = "YOUR_API_KEY"

# Initialisation du nouveau client Google GenAI
client = genai.Client(api_key=API_KEY)

# --- TRADUCTIONS ---
TRANSLATIONS = {
    "fr": {
        "welcome": "Interface Terminal Gemini v1.0",
        "help": "Commandes : 'exit' (quitter), 'lang' (changer langue)",
        "prompt": "Vous",
        "ai_name": "Gemini",
        "wait": "Réflexion...",
        "error": "Erreur : ",
        "exit_msg": "Au revoir !",
        "lang_changed": "Langue : Français",
        "sys_instr": "Tu es un assistant utile. Réponds de manière concise en Français."
    },
    "en": {
        "welcome": "Gemini Terminal Interface v2.0",
        "help": "Commands: 'exit' (quit), 'lang' (change language)",
        "prompt": "You",
        "ai_name": "Gemini",
        "wait": "Thinking...",
        "error": "Error: ",
        "exit_msg": "Goodbye!",
        "lang_changed": "Language: English",
        "sys_instr": "You are a helpful assistant. Respond concisely in English."
    }
}

# --- COULEURS ET STYLE ---
BLUE, PURPLE, CYAN, RESET, BOLD, RED = "\033[94m", "\033[95m", "\033[96m", "\033[0m", "\033[1m", "\033[91m"

def get_system_lang():
    """Détecte la langue de manière compatible avec Python 3.15+."""
    try:
        # Utilisation de getlocale() pour éviter le DeprecationWarning
        lang = locale.getlocale()[0]
        if lang and lang.lower().startswith("fr"):
            return "fr"
    except:
        pass
    return "en"

def print_logo(lang_code):
    """Affiche le logo en Raw String pour éviter le SyntaxWarning."""
    logo = rf"""{BLUE}
  ____ _____ __  __ ___ _   _ ___ 
 / ___| ____|  \/  |_ _| \ | |_ _|
| |  _|  _| | |\/| || ||  \| || | 
| |_| | |___| |  | || || |\  || | 
 \____|_____|_|  |_|___|_| \_|___|{RESET}
{PURPLE}      > {TRANSLATIONS[lang_code]['welcome']}{RESET}
"""
    print(logo)

def main():
    current_lang = get_system_lang()
    print_logo(current_lang)
    print(f"{CYAN}{TRANSLATIONS[current_lang]['help']}{RESET}\n")

    # On utilise le modèle Flash 1.5 pour plus de rapidité
    model_id = "gemini-3-flash-preview"

    while True:
        t = TRANSLATIONS[current_lang]
        try:
            # Entrée utilisateur
            user_input = input(f"{BOLD}{t['prompt']} > {RESET}").strip()

            if user_input.lower() in ['exit', 'quit']:
                print(f"{PURPLE}{t['exit_msg']}{RESET}")
                break
            
            if user_input.lower() == 'lang':
                current_lang = "en" if current_lang == "fr" else "fr"
                print(f"{CYAN}{TRANSLATIONS[current_lang]['lang_changed']}{RESET}\n")
                continue

            if not user_input:
                continue

            # Petit indicateur de chargement
            print(f"{CYAN}{t['wait']}{RESET}", end="\r")

            # Appel API avec instruction système dynamique
            response = client.models.generate_content(
                model=model_id,
                contents=user_input,
                config={
                    'system_instruction': t['sys_instr'],
                    'temperature': 0.7,
                }
            )

            # Nettoyage de la ligne "Réflexion..." et affichage
            sys.stdout.write("\033[K") 
            print(f"{BLUE}{t['ai_name']} > {RESET}{response.text}")
            print(f"{BLUE}{'-'*40}{RESET}")

        except KeyboardInterrupt:
            print(f"\n{PURPLE}{t['exit_msg']}{RESET}")
            break
        except Exception as e:
            print(f"\n{RED}{t['error']}{e}{RESET}")

if __name__ == "__main__":
    main()