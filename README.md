# AI-Customer-Support-Email-Assistant


Jednostavna i učinkovita Python automatizacija koja simulira sustav korisničke podrške. Skripta analizira dolazne e-mailove upita korisnika pomoću **Hugging Face Inference API-ja (Llama-3.3-70B-Instruct)**, automatski prepoznaje sentiment i kategoriju problema te generira i šalje personalizirani, empatični odgovor na hrvatskom jeziku putem **SMTP protokola**.

Projekt je razvijen s naglaskom na sigurnost (skrivanje API ključeva) i pripremljen je za laku integraciju u veće CRM ili ticket sustave.

##  Ključne funkcionalnosti
- **LLM Analiza (NLP):** Integracija s Hugging Face API-jem za naprednu analizu teksta.
- **Sentiment & Kategorizacija:** Automatsko prepoznavanje tona korisnika (Pozitivan/Neutralan/Negativan) i tipa upita (Tehnički problem, račun, pohvala).
- **Automatsko slanje:** Generiranje profesionalnog odgovora i slanje korisniku u realnom vremenu preko zaštićenog SMTP klijenta (Google App Passwords).
- **Sigurnost na prvom mjestu:** Korištenje `.env` okolišnih varijabli za potpunu izolaciju osjetljivih podataka od Git repozitorija.

##  Tehnologije
- **Jezik:** Python 3.11
- **AI Integracija:** `huggingface_hub` (Inference API)
- **Model:** Meta Llama-3.3-70B-Instruct
- **Automatizacija & Protokoli:** `smtplib`, `email.mime`, `python-dotenv`



## Plan za produkciju i skaliranje (Production Roadmap)

U produkcijskom okruženju, sustav bi se nadogradio na sljedeći način:

   - IMAP Integracija: Umjesto simuliranog stringa, uvođenje imaplib biblioteke za aktivno slušanje i povlačenje nepročitanih e-mailova s poslužitelja u realnom vremenu (Webhook / Cron job).

   - Baza podataka (SQL/DevOps): Integracija s PostgreSQL/SQLite bazom za logiranje svakog upita, prepoznatog tona i generiranog odgovora. Ovo omogućuje analitiku, QA praćenje i analizu "halucinacija" AI modela.

   - Asinkroni procesi: Prelazak na asinkrono izvršavanje (asyncio / Celery) kako bi sustav mogao paralelno obrađivati stotine zahtjeva bez blokiranja niti.
