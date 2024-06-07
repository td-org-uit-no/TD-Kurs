---
marp: true

theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')


---

# Introduction

The terminal is an incredible tool, when you unlock its secrets.

---

# Hva er en terminal?

En terminal er et program som lar deg bruke datamaskinen ved hjelp av et tekstbasert grensesnitt.
* Fra før av er du vant med å bruke andre grensesnitt, såkalte grafiske grensesnitt.
* Kanskje er du kun vant til å bla gjennom apper på en telefon.

En god grunn til å bruke tekstbaserte grensesnitt er at det blir enklere å *automatisere* arbeidsprosesser som du gjentar ofte.

---

Andre grunner til å bruke tekstbaserte grensesnitt.

* det er lettere å lage tekstbaserte grensesnitt, og de bruker mindre ressurser enn grafiske grensesnitt.
* På grunn av dette vil du møte på tekstbaserte grensesnitt i mange ulike datamaskinsystemer du møter på studiet og senere i arbeidslivet som informatiker.


Moderne shell som for eksempel `fish` kan ofte gjette hva du skal gjøre og komme med gode forslag.
I dette kurset skal vi starte med `bash`, som er litt mer gammeldags.
Bytt gjerne til `fish` straks du har gjort kurset og lært deg det grunnleggende. Et annet godt alternativ er `zsh`.

---

## Hva du trenger for å følge med her

Du kan bruke det du lærer her på mac, linux og windows subsystem for linux.
Du bør ha åpnet en terminal.

---

## Hva er en fil, og hva er en mappe?

Du kan tenke på filer og mapper som
* En fil er en mengde informasjon lagret et spesielt sted på disk (eller annet lagringsmedium)
* En mappe er en spesiell fil som kan inneholde andre filer, og andre mapper.


---

## Hvor lagres filer?

Informasjonen blir (for eksempel) lagret på disk som en rekke magnetisk opp/ned, altså binært. På maskinen har du et operativsystem (slik som windows, mac OSX eller linux), 
som kan lese, tolke og presentere informasjonen for deg, samt skrive informasjon tilbake til disk. Her skal du blant annet lære å bruke filsystemet gjennom terminalen.

På engelsk kalles en mappe (i UNIX-systemer) for en *directory*. På windows kalles det også en *folder*.

I nyere tid kan filer også lagres "i skyen" og lignende, det vil si på disk i et datasenter et eller annet sted.

---

## Filsystemet i unix-baserte systemer.

Du kan navigere i filystemet på unix-baserte systemer som i et tre, med en mappe kalt `/` ved roten av treet.
Treet tegnes ofte snudd opp ned, med roten på toppen. Dette er ganske vanlig i informatikk.

---

#### Filsystem

For eksempel har brukeren *eika* i systemet under en mappe på hjemmeområdet sitt `home` som vist i figuren under:

```
/home/
└── eika
    ├── bin
    ├── Desktop
    ├── Documents
    ├── Downloads
    ├── Pictures
    ├── Public
    ├── repos
    ├── src
    └── Videos
    └── tinkering
```

---

Når *eika* logger inn, står han i mappen `/home/eika`. Hvis du bruker linux eller windows subsystem for linux (WSL), har du også en slik mappe.

Videre kan du se at på hjemmeområdet sitt har han flere mapper, slik som `bin` for binære filer, `Pictures` for bilder og så videre.
Inni disse mappene kan han ha flere mapper, som inneholder flere mapper etc. etc.

---

### Kommandoen `pwd`


Finn ut hvilken mappe du står i. Kommandoen `pwd` er en forkortelse for *print working directory*.

```
❯ pwd
/home/eika/tinkering/markdown-slides-termkurs
```
Kommandoen gir deg *stien* fra rotmappen `/` til mappen du står i. Dette kalles ofte en *absolutt sti* eller en *absolute path*.


TODO: mulighet for misforståelse: 'absolutt sti er noe du får med pwd' etc.

---


### Vis innholdet i en mappe

Kommandoen `ls` forteller deg hva som er inni en mappe. Hvis du kun skriver `ls` i terminalen som vist under,
får du vite hvilke filer mappen du står i inneholder.
Mappen du står i får du som nevnt vite med kommandoen `pwd`.

```
❯ ls
node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testout.html
```

---

Hvis du gir `ls` en mappe som *input*, kan du få se innholdet i den mappen, f.eks

```
❯ ls
node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testout.html

 ~/tinkering/markdown-slides-termkurs ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
❯ ls node_modules/
 accepts/             cliui/                  escodegen/           import-fresh/                   '@marp-team'/       path-type/                 socks-proxy-agent/    unbzip2-stream/
 agent-base/          color-convert/          esm/                 inherits/                        mathjax-full/      pend/                      source-map/           undici-types/
 ansi-regex/          color-name/             esprima/             ip-address/                      mdurl/             picocolors/                source-map-js/        universalify/
 ...
```
Her har vi ikke tatt med alle mappene som dukker opp, siden det er veldig mange av dem.

---

#### Skjulte filer og mapper
Kommandoen `ls` kan vise skjulte filer og mapper hvis man gir den et argument `-a`.

```
❯ ls -a
./  ../  node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testout.html  testout.pdf
```

Som du ser har denne mappen to skjulte mapper, nemlig `.` og `..`. Skråstreken etterpå indikerer at det er en mappe. På noen systemer vil du ikke se skråstreken, men mappen vil ha en annen farge enn filer.

Mappen `.` er mappen mappen selv, noe som er nyttig av og til.
Mappen `..` er foreldremappen til `.`, altså ett steg opp i filtreet. Dette er nyttig når du skal tilbake i treet.

Hvis du står på hjemmeområdet og skriver `ls -a`, vil du se mange skjulte filer.

---

#### Åpne en mappe i filutforskeren fra terminalen

Hvis du vil åpne mappen du står i, kan du skrive `open .`, eller `xdg-open .` hvis du sitter på linux eller mac.

Du får da opp et grafisk vindu slik du er vant med fra vanlig bruk av mac eller windows.

Hvis du bruker WSL skriver du `explorer.exe .` for å åpne mappen du står i.

---

### Kommandoene `cd`, `mkdir`, `touch` og `rmdir`

Du kan lage en ny mappe med kommandoen `mkdir`.
* Skriv `ls` i terminalen din.
* Skriv så `mkdir testmappe`
* Skriv `ls` på nytt. Du skal nå se en mappe med navn `testmappe/`.
* Skriv `pwd`
* Skriv `cd testmappe`
* Skriv `pwd`

Du bør nå se at stien du fikk med kommandoen `pwd` har forandret seg.

---

 ```
❯ ls
node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testout.html  testout.pdf

❯ mkdir testmappe

❯ ls
node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testmappe/  testout.html  testout.pdf
 ```

---

### Navigere tilbake

* Skriv `pwd`
* Skriv `cd ..`
* Skriv `pwd`
Du ser nå at du står i mappen over. Skriv `ls`, og du bør se mappen du navigerte tilbake fra.

---

### Lage nøstede mapper med én kommando

Skriv nå `mkdir -p informatikk/semester1/terminalkurs/dokumenter/intro`.
Bruk så kommandoen `cd` til å navigere deg til mappen `intro` i mappen for terminalkurset.

*HINT:* Du kan bruke tab-completion til å gjøre dette med noen få tastetrykk.

---

```
❯ mkdir -p informatikk/semester1/terminalkurs/intro
❯ cd informatikk/semester1/terminalkurs/intro/
❯ pwd
/home/eika/informatikk/semester1/terminalkurs/intro
```

---

### Bruk kommandoen `touch` for å lage filer

```
❯ pwd
/home/eika/informatikk/semester1/terminalkurs/intro
❯ ls
❯ touch terminalkurs-notes.txt
❯ ls
terminalkurs-notes.txt
```

---

### Hvordan åpne filer

Du kan åpne filen med favoritt-editoren din.
Her er det mange valg, f.eks vscode, zed, vim, eller emacs.

Akkurat nå kan du også skrive `xdg-open .`
og dobbeltklikke på filen du akkurat laget.
Merk bruken av mappen `.` som input.

`xdg-open` kan åpne forskjellige filtyper med standardprogrammet for disse filtypene. Den kan også åpne nettsider:
`xdg-open https://td-uit.no` åpner nettsiden til Tromsøstudentens Dataforening i standardnettleseren din.

---

### Skriv noe til filen

Skriv noe til filen din. For eksempel `terminal er moro`. (Eller ikke moro...)

---

### Bruk kommandoen `cat` for å vise innhold i en fil

Du kan vise innholdet i filen med kommandoen `cat`.

```
❯ cat terminalkurs-notes.txt 
terminal er moro
```

Du kan også skrive `less terminalkurs-notes.txt`. Trykk  `q` for å komme deg tilbake til terminalen

---


### Bruk kommandoen `cp` for å kopiere filen

```
❯ cp terminalkurs-notes.txt kopi-notes-terminal.txt
```
Som du ser tar programmet `cp` to argumenter, nemlig kilden `terminalkurs-notes.txt` som skal blir kopier,
og navn på output-filen `kopi-notes-terminal.txt`. 

Pass på! Hvis `kopi-notes-terminal.txt` finnes fra før, blir den overskrevet!

---

### Bruk kommandoen `mv` for å flytte filen til en annen mappe

La oss først lage en mappe 
```
❯ cp terminalkurs-notes.txt kopi-notes-terminal.txt
❯ ls
kopi-notes-terminal.txt  notatmappe/  terminalkurs-notes.txt
```
Vi kan nå flytte  filen:

```
❯ mv terminalkurs-notes.txt notatmappe/
```

Bruk `ls` til å sjekke at filen har blitt flyttet.

---

### Bruk kommandoen `mv` for å gi filen nytt navn
Du kan endre navnet på kopien til `kopi-notater-terminal.txt' med kommandoen

`mv kopi-notes-terminal.txt kopi-notater-terminal.txt`


---


### Slett kopien med kommandoen `rm`

Du kan slette kopien med kommandoen `rm kopi-notater-terminal-txt`.
Her må du igjen være forsiktig. Når du sletter en fil, er det ikke lett å gjenopprette den som på f.eks windows hvor du har en papirkurv. 
Merk likevel at `rm` ikke gir sikker sletting av filer hvis en angriper ønsker å finne ut hvilke statshemmeligheter du har hatt på disken din.

---

```
❯ ls
kopi-notes-terminal.txt  notatmappe/
❯ rm kopi-notes-terminal.txt
❯ ls
notatmappe/
```


---

<!-- Skummelt - dårlig ide for newbies.

#### Slett mappen og filen inni med `rm -rf`
Du kan slette en hel mappestruktur med `rm -rf`
Vær forsiktig, det som er inni mappen får du ikke tilbake!

```
❯ ls
notatmappe/
❯ rm -rf notatmappe/
❯ ls

```
---

-->


#### Kommandoen `rmdir`
En tryggere versjon for å slette mapper er å bruke `rmdir`.
Den fungerer bare på tomme mapper.

---

```
❯ mkdir mappe2                                                 # lag en mappe
❯ touch mappe2/teksthilsen.txt                                 # opprett en fil inni mappa
❯ echo "hallo der" > mappe2/teksthilsen.txt                    # skriv en tekst til filen
❯ cat mappe2/teksthilsen.txt                                   # sjekk at filen inneholder teksten
hallo der
❯ rmdir mappe2                                                 # prøv å slette mappen med rmdir
rmdir: failed to remove 'mappe2': Directory not empty          # feilmelding
❯ rm mappe2/teksthilsen.txt                                    # slett filen inni mappa
❯ rmdir mappe2/                                                # slett mappa
```

---

