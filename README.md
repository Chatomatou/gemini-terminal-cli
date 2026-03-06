# gemini-terminal-cli
🌌 Une interface terminal (CLI) élégante et multilingue pour Google Gemini. Rapidité Flash, gestion de l'historique et détection de langue intégrée.

# 🌌 Gemini Terminal CLI v1.0

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Model: Gemini 3 Flash](https://img.shields.io/badge/Model-Gemini%203%20Flash-purple.svg)](https://deepmind.google/technologies/gemini/)

Une interface en ligne de commande (CLI) élégante, rapide et multilingue pour discuter avec l'IA **Google Gemini**. Ce script utilise la dernière SDK `google-genai` pour une expérience fluide directement dans votre terminal.

---

## ✨ Fonctionnalités

* **🌍 Multilingue :** Détection automatique du système (FR/EN) et commande `lang` pour basculer à la volée.
* **🧠 Mémoire de session :** (Optionnel) Gestion de l'historique pour des conversations cohérentes.
* **⚡ Performance :** Optimisé pour le modèle `gemini-3-flash-preview` (basse latence).
* **🎨 Interface stylisée :** Couleurs ANSI, logo ASCII et indicateur de réflexion dynamique.
* **🛡️ Sécurité :** Support des variables d'environnement pour protéger votre clé API.

---

## 🚀 Installation rapide

### 1. Cloner le projet
```bash
git clone [https://github.com/Chatomatou/gemini-terminal-cli.git](https://github.com/Chatomatou/gemini-terminal-cli.git)
cd gemini-terminal-cli
python -m venv .venv
# Sur Windows (PowerShell) :
.\.venv\Scripts\Activate.ps1
# Sur Linux/macOS :
source .venv/bin/activate
pip install -r requirements.txt
```