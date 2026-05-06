# 🤖 iCub Humanoid Project - ROS 2 Jazzy

![ROS 2](https://img.shields.io/badge/ROS-2%20Jazzy-blue)
![Robotics](https://img.shields.io/badge/Specialty-Robotics%20%26%20Intelligent%20Systems-red)

Ce projet contient la modélisation URDF complète et le système de contrôle du robot humanoïde **iCub**.

## 🌟 Caractéristiques Principales
- **URDF Haute-Fidélité** : Incluant la base, le torse, le cou, la tête et les mains détaillées.
- **Cinématique Corrigée** : Articulations du cou et des doigts optimisées pour éviter les collisions fantômes.
- **Visualisation Dynamique** : Support complet pour RViz2 avec contrôle des joints en temps réel.

## 📁 Nouveaux Fichiers Ajoutés
- `launch/display.launch.py` : Automatisation complète du démarrage.
- `scripts/move_icub.py` : Script Python pour tester les servomoteurs simulés.
- `meshes/` : Fichiers géométriques .dae (non inclus dans le git par défaut).

## 🚀 Guide Rapide
### 1. Compilation
```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

### 2. Lancement
```bash
ros2 launch humanoid_robot display.launch.py
```

### 3. Test de Mouvement
```bash
ros2 run humanoid_robot move_icub.py
```

---
**Développeur :** Maria Lagab  
**Environnement :** Ubuntu 24.04 | Dell Latitude 7400
