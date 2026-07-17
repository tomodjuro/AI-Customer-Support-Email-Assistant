import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Uvozimo Hugging Face klijent
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

# ==================== KONFIGURACIJA ====================
HF_TOKEN = os.getenv("HF_TOKEN")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
# =======================================================

# Inicijalizacija Hugging Face klijenta s Llama 3.1 modelom
client = InferenceClient(
    model="meta-llama/Llama-3.3-70B-Instruct", 
    token=HF_TOKEN
)

incoming_email = """
Poštovani,
Kupio sam vaš proizvod prije dva dana, ali sustav mi stalno javlja grešku 404 kada se pokušam prijaviti. 
Jako sam frustriran jer mi hitno treba za posao. Molim vas za pomoć ili povrat novca.
Pozdrav, Ivan Horvat (ivan.horvat@example.com)
"""

def analyze_and_respond_to_email(email_content):
    print("🤖 Analiziram e-mail uz pomoć Hugging Face (Llama 3.1)...")
    
    prompt = f"""
    Analiziraj sljedeći e-mail upit korisnika. 
    Odredi sentiment (Pozitivan/Neutralan/Negativan) i kategoriju upita.
    Nakon toga, napiši profesionalan, empatičan odgovor na hrvatskom jeziku u ime korisničke podrške.
    Ako je korisnik frustriran, ponudi ispriku.

    E-mail korisnika:
    {email_content}

    Odgovori striktno u sljedećem formatu:
    SENTIMENT: [Ovdje upiši sentiment]
    KATEGORIJA: [Ovdje upiši kategoriju]
    ODGOVOR:
    [Ovdje upiši generirani odgovor]
    """

    # Pozivamo model kroz chat completion API
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat_completion(
        messages=messages,
        max_tokens=500
    )
    
    return response.choices[0].message.content



def send_email(to_email, subject, body):
    print(f"📧 Šaljem automatizirani odgovor na {to_email}...")
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Spajanje na Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        server.send_message(msg)
        server.quit()
        print("✅ E-mail je uspješno poslan!")
    except Exception as e:
        print(f"❌ Pogreška pri slanju e-maila: {e}")

# ==================== GLAVNI PROCES ====================
# ==================== GLAVNI PROCES ====================
if __name__ == "__main__":
    # 1. Pokreni AI analizu
    ai_output = analyze_and_respond_to_email(incoming_email)
    print("\n--- REZULTAT AI ANALIZE ---")
    print(ai_output)
    print("---------------------------\n")
    
    # 2. Parsiranje odgovora (izvlačimo samo tekst odgovora)
    if "ODGOVOR:" in ai_output:
        ai_response_body = ai_output.split("ODGOVOR:")[1].strip()
        
        # 3. SPAJANJE ODGOVORA I ORIGINALNE PORUKE
        # Dodajemo vizualnu liniju i tekst originalne poruke na dno
        full_email_body = f"""{ai_response_body}

--------------------------------------------------
Vaš izvorni upit:
{incoming_email.strip()}"""
        
        # 4. Pošalji e-mail (sada šaljemo 'full_email_body')
        test_recipient = SENDER_EMAIL 
        send_email(test_recipient, "Re: Podrška - Tehnički problem", full_email_body)
    else:
        print("Format odgovora nije ispravan.")
