import csv
def carica_da_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print('Il file è stato trovato')
            righe = file.readlines()
            if not righe:
                return none
            biblioteca = []
            for riga in righe[1:]:  # skippo prima riga perche è il num sezioni
                dati = riga.strip().split(',')
                libro = {
                    'sezione': int(dati[4]),
                    'titolo': dati[0],
                    'autore': dati[1],
                    'anno': int(dati[2]),
                    'pagine': int(dati[3]),
                }                                   #lista di dizionari
                biblioteca.append(libro)

            return biblioteca

    except FileNotFoundError:                   #nel caso non venga trovato il file
        print("File non trovato!")
        return None
def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    nuovo_libro = {
        'sezione': sezione,
        'titolo': titolo,
        'autore': autore,
        'anno': anno,
        'pagine': pagine
    }
    biblioteca.append(nuovo_libro)                  # lo aggiungo
    return biblioteca

def cerca_libro(biblioteca, titolo):
    risultato= False
    for libro in biblioteca:
        if libro['titolo'] == titolo:
            risultato =True
    return risultato

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    titoli_non_ord= []
    for libro in biblioteca:
        if libro['sezione'] == sezione:
            titoli_non_ord.append(libro['titolo'])
    titoli= sorted(titoli_non_ord)
    return titoli

def main():
    biblioteca = []
    file_path = "biblioteca.csv"
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)  #risputa titoli riordinati della sez
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
