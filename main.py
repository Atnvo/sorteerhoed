def vragen_ophalen(conf):
    print(conf)

def main():
    while True:
        try:
            vragen_ophalen('test')
            break
        except (ValueError, FileNotFoundError):
            print("Oops! vragen bestand niet gevonden. Probeer opnieuw... (Vergeet niet de file type extensie)")

if __name__ == "__main__":
    main()
