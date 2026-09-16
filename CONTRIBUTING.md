# Contribuire al Progetto App Ricerca Cellulare

## Come Iniziare

1. Fai un fork del repository
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit i tuoi cambiamenti (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## Linee Guida di Sviluppo

### Codice
- Segui il PEP 8 per il codice Python
- Usa type hints dove possibile
- Mantieni il codice pulito e leggibile
- Lunghezza massima linea: 88 caratteri (Black formatter)

### Testing
- Aggiungi test per nuove funzionalità
- Mantieni la copertura dei test > 80%
- Esegui: `pytest tests/` prima di fare un commit

### Documentazione
- Aggiorna il README.md se necessario
- Documenta le funzioni pubbliche con docstrings
- Mantieni il ROADMAP.md aggiornato

### Commit
- Usa messaggi di commit chiari e descrittivi
- Segui il formato: `[TYPE] Descrizione`
  - feat: nuova funzionalità
  - fix: correzione bug
  - docs: aggiornamento documentazione
  - style: formatting, missing semicolons, ecc.
  - refactor: rifattorizzazione codice
  - test: aggiunta/modifica test

## Segnalazione Bug

Se trovi un bug, per favore:
1. Controlla se è già stato segnalato in Issues
2. Crea un nuovo issue con:
   - Titolo descrittivo
   - Descrizione dettagliata
   - Step per riprodurre il problema
   - Output atteso vs output effettivo
   - Versione Python e OS

## Richieste di Feature

Per suggerire nuove funzionalità:
1. Crea un issue con label "enhancement"
2. Descrivi la feature che vorresti
3. Spiega il caso d'uso
4. Discuti con il team prima di iniziare lo sviluppo

## Standard di Qualità

Prima di fare una PR, assicurati che:
- ✅ Il codice passa tutti i test
- ✅ Non ci sono errori di linting (`flake8`)
- ✅ Il codice è formattato con `black`
- ✅ I test coverage è mantenuto
- ✅ La documentazione è aggiornata

## Domande?

Sentiti libero di aprire un discussion o un issue per domande!
