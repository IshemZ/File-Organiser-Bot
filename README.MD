# File Organizer Bot

## Description

Ce projet automatise l'organisation des fichiers dans des répertoires spécifiques basés sur leurs extensions. Le script est configuré pour s'exécuter automatiquement à intervalles réguliers en utilisant `launchd` sur macOS.

## Configuration

### Environnement Virtuel

1. Créez et activez un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate
```  


2. Installez les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

3. Créez un fichier run_script.sh avec le contenu suivant :
```bash
source "/path/to/your/venv/bin/activate"
python "/path/to/your/script.py"
```

### Rendez le fichier exécutable :
```bash
chmod +x "/path/to/your/run_script.sh"
```

### Créez un fichier plist com.yourdomain.organizer.plist dans ~/Library/LaunchAgents avec le contenu suivant :
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>com.yourdomain.organizer</string>
    <key>ProgramArguments</key>
    <array>
      <string>/bin/zsh</string>
      <string>/path/to/your/run_script.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>86400</integer> <!-- 86400 seconds = 24 hours -->
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/path/to/your/logs/com.yourdomain.organizer.out</string>
    <key>StandardErrorPath</key>
    <string>/path/to/your/logs/com.yourdomain.organizer.err</string>
  </dict>
</plist>
```

## Utilisation :

### Chargez le fichier plist :
```bash
launchctl load ~/Library/LaunchAgents/com.yourdomain.organizer.plist
```

### Le script s'exécutera automatiquement toutes les 24 heures. Vous pouvez forcer l'exécution du job avec :
   ```bash
  launchctl start com.yourdomain.organizer
  ```
## Dépannage

### Vérification des Logs

#### Sortie standard :

```bash
cat ~/Library/Logs/com.yourdomain.organizer.out
```

#### Erreurs :

```bash
cat ~/Library/Logs/com.yourdomain.organizer.err
```

### Modification du Job:

#### Déchargez le job avant de le modifier :
```bash
launchctl unload ~/Library/LaunchAgents/com.yourdomain.organizer.plist
```

#### Rechargez le job après modifications :
```bash
launchctl load ~/Library/LaunchAgents/com.yourdomain.organizer.plist
```

## Contributions :

Les contributions sont les bienvenues. Veuillez soumettre un pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence:

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.


