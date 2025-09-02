# Strict Health Assistant

Ky është një asistent shëndetësor i rreptë në Python që dërgon njoftime strikte dhe rregulla ditore për detyrat që duhet të kryesh për të arritur qëllimet e tua. Ai përfshin plane ushqimore dhe gjimnastike strikte për rikthimin e trupit dhe shëndetit mendor, duke marrë parasysh mungesën e vitaminave, mungesën e oreksit, hidratimin e ulët, dhimbjet e muskujve, heqjen e kafesë dhe sheqerit, dhe migrenën.

## Karakteristikat

- **Njoftime strikte**: Dërgon plane ushqimore, gjimnastike, detyra ditore dhe mesazhe motivuese në gjuhën shqipe.
- **Plan ushqimor**: Përfshin vitamina, rritjen e oreksit dhe heqjen e kafesë dhe sheqerit.
- **Plan gjimnastike**: Ushtrime strikte për trupin e plotë, stretching për dhimbje muskujsh dhe relaksim për migrenë.
- **Detyra ditore**: Hidratim, suplemente, meditimi dhe pushim.
- **Telegram Bot**: Dërgon njoftime përmes Telegram bot.

## Instalimi

1. Klono ose shkarko këtë projekt.
2. Instaloni varësitë:
   ```
   pip install -r requirements.txt
   ```
3. Krijoni një bot Telegram:
   - Shkoni te @BotFather në Telegram dhe krijoni një bot të ri.
   - Merrni token-in e botit.
4. Merrni Chat ID-në tuaj:
   - Dërgoni një mesazh te boti juaj dhe vizitoni `https://api.telegram.org/bot<TOKEN>/getUpdates` për të marrë Chat ID-në.
5. Redaktoni `main.py` dhe zëvendësoni:
   - `YOUR_TELEGRAM_BOT_TOKEN` me token-in tuaj.
   - `YOUR_TELEGRAM_CHAT_ID` me Chat ID-në tuaj.

## Përdorimi

Drejto skriptin:
```
python main.py
```

Skripti do të dërgojë njoftime sipas orarit:
- Plane ushqimore: 8:00, 13:00, 19:00
- Plane gjimnastike: 7:00, 15:00, 20:00
- Detyra ditore: 9:00
- Mesazhe motivuese: 12:00, 18:00

## Rregulla Strikte

- Nuk ka përjashtime! Ndjek planin çdo ditë.
- Hidratimi: Pi 3 litra ujë çdo ditë.
- Hiq kafe dhe sheqer gradualisht.
- Për migrenë: Pusho, relakso dhe shmang stresin.
- Për dhimbje muskujsh: Bëj stretching dhe relakso.

## Kujdes

Ky asistent është për qëllime informative. Konsultohu me një mjek për këshilla personale shëndetësore.
