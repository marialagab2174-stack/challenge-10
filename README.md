# 🤖 iCub Humanoid Robot - ROS 2 Jazzy

Ce projet présente un modèle URDF haute fidélité du robot humanoïde **iCub**, optimisé pour la visualisation et la simulation cinématique sous ROS 2.

## 🛠 Spécifications Techniques
- **Modèle** : iCub (Humanoid Robot)
- **Degrés de Liberté (DoF)** : Tête, Cou, Torse, Bras complets et Doigts détaillés.
- **Corrections Appliquées** : 
  - Alignement précis du `neck_pitch` au-dessus du chest.
  - Positionnement anatomique des phalanges des doigts (Thumb, Index, Middle, etc.).
  - Matériaux réalistes (`skin`, `dark`, `red`).

## 📁 Structure du Projet
- `urdf/` : Fichiers de description du robot.
- `meshes/` : Fichiers .dae pour le rendu visuel.
- `launch/` : Scripts de lancement pour RViz2.
- `scripts/` : Contrôleurs de démonstration pour les articulations.

## 🚀 Installation et Visualisation
```bash
# Compilation
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash

# Lancement de la visualisation
ros2 launch humanoid_robot display.launch.py
```

## 🧠 Démo de Mouvement
Pour faire bouger la tête de l'iCub automatiquement :
```bash
ros2 run humanoid_robot head_demo.py
```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent  
**Plateforme :** Ubuntu 24.04 | Dell Latitude 7400
