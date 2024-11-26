from fpdf import FPDF

# Tworzenie dokumentu PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Nagłówek oferty
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, "OFERTA NA PRZEGLĄD PRZEMYSŁOWEJ SZAFY STEROWNICZEJ", ln=True, align="C")
pdf.ln(10)

# Dane podstawowe
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "Dla: (nazwa Klienta)\nOd: PowerALL - Kompleksowe Usługi Inżynierskie\nData sporządzenia oferty: (data)\n")
pdf.ln(5)

# Zakres prac
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Zakres prac:", ln=True)
pdf.set_font("Arial", size=12)
zakres_prac = [
    "1. Kontrola wizualna połączeń elektrycznych – sprawdzenie stanu technicznego elementów i połączeń w szafie sterowniczej.",
    "2. Dokręcenie połączeń śrubowych – weryfikacja i ewentualne dokręcenie połączeń w celu zapewnienia bezpiecznego funkcjonowania.",
    "3. Weryfikacja połączeń wyrównawczych – sprawdzenie poprawności podłączenia systemów uziemienia i wyrównania potencjałów.",
    "4. Analiza termowizyjna – wykonanie zdjęć termowizyjnych i analiza ich wyników w celu identyfikacji potencjalnych miejsc przegrzewania.",
    "5. Raport końcowy – sporządzenie raportu z przeglądu, zawierającego zalecenia dotyczące dalszego użytkowania lub koniecznych napraw."
]
for item in zakres_prac:
    pdf.multi_cell(0, 10, item)
pdf.ln(5)

# Szczegóły dotyczące przeglądu
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Szczegóły dotyczące przeglądu:", ln=True)
pdf.set_font("Arial", size=12)
szczegoly = (
    "- Na podstawie zdjęć szaf sterowniczych dostarczonych w korespondencji mailowej.",
    "- Elementy zabudowy: falowniki, sterownik PLC, styczniki, przekaźniki, listwy łączeniowe oraz zabezpieczenia nadprądowe.",
    "- Prace wykonywane przez dwie osoby."
)
for line in szczegoly:
    pdf.multi_cell(0, 10, line)
pdf.ln(5)

# Kosztorys
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Kosztorys:", ln=True)
pdf.set_font("Arial", size=12)
kosztorys = [
    "- Średnia stawka za roboczogodzinę: 120 zł netto/osoba",
    "- Szacowany czas pracy dwóch osób: 6 godzin",
    "- Łączny koszt usługi: 1440 zł netto",
    "(koszt należy dostosować, jeśli czas pracy ulegnie zmianie)"
]
for item in kosztorys:
    pdf.multi_cell(0, 10, item)
pdf.ln(5)

# Uwagi
pdf.set_font("Arial", style="B", size=12)
pdf.cell(0, 10, "Uwagi:", ln=True)
pdf.set_font("Arial", size=12)
uwagi = [
    "1. Oferta nie obejmuje kosztów ewentualnych materiałów potrzebnych do naprawy.",
    "2. Termin wykonania prac zostanie ustalony po akceptacji oferty."
]
for item in uwagi:
    pdf.multi_cell(0, 10, item)
pdf.ln(5)

# Podpis
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Z poważaniem,", ln=True)
pdf.cell(0, 10, "(Imię i nazwisko osoby reprezentującej firmę)", ln=True)
pdf.cell(0, 10, "PowerALL – Kompleksowe Usługi Inżynierskie", ln=True)

# Zapisanie pliku PDF
file_path = "./Oferta_PowerALL.pdf".encode('latin-1')
pdf.output()


