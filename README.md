# 🤖 Projet iCub Humanoid - ROS 2 Jazzy
## Développement & Simulation Avancée

Ce dépôt contient le modèle cinématique complet du robot humanoïde **iCub**, conçu pour la recherche en robotique et systèmes intelligents.

---

### 📋 Cahier des Charges & Spécifications
- **Base Mobile & Torse** : Support du bassin (root_link) avec 3 degrés de liberté pour le torse (pitch, roll, yaw).
- **Système de Vision** : Intégration de deux caméras simulées (l_eye, r_eye) positionnées anatomiquement.
- **Manipulation Fine** : Modélisation complète des mains avec 5 doigts (phalanges proximales et distales).

### 🔧 Corrections Techniques Appliquées
- **Ajustement du Cou** : Correction de l'origine sur l'axe Z pour le `neck_pitch`, plaçant le cou au-dessus du chest et non à l'intérieur.
- **Géométrie des Doigts** : Réalignement des axes de rotation des pouces et des index pour une préhension réaliste.
- **Rendu Visuel** : Utilisation de matériaux spécifiques (`skin`, `dark`, `red`) pour une distinction claire des composants mécaniques.

### 🚀 Utilisation
1. **Compilation** :
   ```bash
   cd ~/ros2_ws && colcon build --symlink-install
   source install/setup.bash
   ```
2. **Lancement de la Visualisation (RViz2)** :
   ```bash
   ros2 launch humanoid_robot display.launch.py
   ```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent  
**Laboratoire :** Algiers Robotics Lab  
**Hardware :** Dell Latitude 7400
