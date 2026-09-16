# App Ricerca Cellulare - Configurazione Ambiente

## Setup Sviluppo

### 1. Clonare il Repository
```bash
git clone https://github.com/MATTEO55/app-ricerca-cellulare.git
cd app-ricerca-cellulare
```

### 2. Creare Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

### 3. Installare Dipendenze
```bash
pip install -r requirements.txt
```

### 4. Configurare Variabili Ambiente
```bash
cp .env.example .env
# Editare .env con i tuoi parametri
```

### 5. Avviare l'Applicazione
```bash
python app.py
```

## Struttura Progetto

```
app-ricerca-cellulare/
├── app.py                 # Entry point
├── requirements.txt       # Dipendenze Python
├── .gitignore            # Git ignore rules
├── README.md             # Documentazione principale
├── SETUP.md              # Questo file
├── ROADMAP.md            # Roadmap progetto
├── CONTRIBUTING.md       # Linee guida contributi
├── src/                  # Codice sorgente
│   ├── api/              # Endpoints API
│   ├── models/           # Modelli dati
│   ├── services/         # Logica di business
│   └── utils/            # Funzioni utili
├── tests/                # Test unitari
├── docs/                 # Documentazione
└── config/               # File configurazione
```

## Tools Consigliati

- **IDE**: VSCode o PyCharm
- **Database**: PostgreSQL
- **API Testing**: Postman o Insomnia
- **Version Control**: Git + GitHub Desktop

## Contatti

Per domande o problemi, crea un issue nel repository.
