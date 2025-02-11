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
/
└── home/
    └── eika
        ├── bin
        ├── Desktop
        ├── Documents
        ├── Downloads
        ├── Pictures
        ├── repos
        ├── src
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

Kommandoen gir deg *stien* fra rotmappen `/` til mappen du står i. Dette kalles ofte en *absolutt sti* eller en *absolute path*,
som vil si at stien beskriver en vei fra rotmappen `/` og frem til målet.

---

### Angi hvor man finner en fil
Man kan angi posisjon til en fil på to ulike måter

* Absolutt sti
* Relativ sti

Absolutt sti angis med utgangspunkt i roten `/` av filsystemet 

Relativ sti angis typisk relativt til mappen du står i (altså working directory).
Hvis du står i mappen `musikk` kan dette for eksempel være

```
metall/satyricon/mother-north.mp3
```
---


### Vis innholdet i en mappe

Kommandoen `ls` forteller deg hva som er inni en mappe. Hvis du kun skriver `ls` i terminalen som vist under,
får du vite hvilke filer mappen du står i inneholder.

```
❯ ls
node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testout.html
```

---

Hvis du gir `ls` en mappe som *input*, kan du få se innholdet i den mappen, f.eks

```
❯ ls
node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testout.html

❯ ls node_modules/
 accepts/             cliui/                  escodegen/           import-fresh/                   '@marp-team'/       path-type/                 socks-proxy-agent/    unbzip2-stream/
 agent-base/          color-convert/          esm/                 inherits/                        mathjax-full/      pend/                      source-map/           undici-types/
 ansi-regex/          color-name/             esprima/             ip-address/                      mdurl/             picocolors/                source-map-js/        universalify/
 ...
```
Her har vi ikke tatt med alt innholdet i mappen som dukker opp, siden det er veldig mye.

---

#### Skjulte filer og mapper
Kommandoen `ls` kan vise skjulte filer og mapper hvis man gir den et argument `-a`.

```
❯ ls -a
./  ../  node_modules/  package.json  package-lock.json  terminal-intro.html  terminal-intro.jpeg  terminal-intro.md  terminal-intro.pdf  terminal-intro.png  testout.html  testout.pdf
```

Som du ser har denne mappen to skjulte mapper, nemlig `.` og `..`. Skråstreken etterpå indikerer at det er en mappe. På noen systemer vil du ikke se skråstreken, men mappen vil ha en annen farge enn filer.

Mappen `.` er mappen selv, som vi skal se er nyttig.
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
Du ser nå at du står i mappen over. Skriv `ls`, og du bør se innholdet i mappen du navigerte tilbake fra.

---

### Lage nøstede mapper med én kommando

Skriv nå `mkdir -p informatikk/semester1/terminalkurs/dokumenter/intro`.
Bruk så kommandoen `cd` til å navigere deg til mappen `intro` i mappen for terminalkurset.

*HINT:* Du kan bruke tab-completion for å spare tastetrykk for mapper du allerede har laget.

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

Mange linux-distribusjoner har programmet `evince` for å åpne pdf-filer.

Prøv å åpne en pdf-fil med `evince`, f.eks

`evince oppgaver-intro.pdf`

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

Du kan også skrive `less terminalkurs-notes.txt`. Trykk  `q` for å komme deg tilbake til terminalen.
Prøv også `more terminalkurs-notes.txt`. Disse to kommandoene lar deg bla gjennom store filer.

---

Du kan også bruke kommandoen `head -20 tekstfil.txt` for å lese de 20 første linjene i `tekstfil.txt`.
På samme måte kan du lese de 25 siste linjene med
`tail -25 tekstfil.txt`

---


### Bruk kommandoen `cp` for å kopiere filen

```
❯ cp terminalkurs-notes.txt kopi-notes-terminal.txt
```
Som du ser tar programmet `cp` to argumenter, nemlig kilden `terminalkurs-notes.txt` som skal bli kopiert,
og navn på output-filen `kopi-notes-terminal.txt`. 

Pass på! Hvis `kopi-notes-terminal.txt` finnes fra før, blir den overskrevet!

---

### Typisk bruk av `cp`

Du har laget en mappe for et prosjekt, og trenger noen konfigurasjonsfiler. I et annet prosjet har du lignende konfigurasjonsfiler
du tenker å tilpasse litt, så du kopierer dem til mappen du står i.

Du kan gjøre dette med

```
cp ~/sti/til/gammelt/prosjekt/gammel-config-fil .
```

---

#### Eksempel

Eindride har operativsystemkurs og alle obligene har helt lik fil for hva som skal ignoreres av versjonskontrollen, kalt `.gitignore`
Når en ny oblig kommer og han har opprettet mappen for ny oblig, gjør han følgende:

```
cp ~/repos/inf2201/project3/inf2201-P3/.gitignore .
```


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

# Pass på!

`mv` overskriver også filen hvis den finens fra før. Hvis `kopi-notater-terminal.txt` finnes fra før, blir den overskrevet!

---

---

### Slett kopien med kommandoen `rm`

Du kan slette kopien med kommandoen `rm kopi-notater-terminal-txt`.

---

```
❯ ls
kopi-notes-terminal.txt  notatmappe/
❯ rm kopi-notes-terminal.txt
❯ ls
notatmappe/
```

---

### Advarsel
Når du sletter en fil med `rm` er den i praksis borte for alltid! Linux har ikke en søppelbøtte du kan hente den tilbake fra.

Vær også forsiktig med sensitive data. Når du sletter en fil, er det ikke lett å gjenopprette den som på f.eks windows hvor du har en papirkurv. 
Merk likevel at `rm` ikke gir sikker sletting av filer hvis en angriper ønsker å finne ut hvilke statshemmeligheter du har hatt på disken din.

---


* Du lærer mer om dette og den indre organiseringen av filsystemet i blant annet operativsystemkurset.
* For å slette filer fullstendig finnes det likevel nyttige verktøy du kan gjøre deg kjent med.

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
For å slette en mappe kan du bruke `rmdir`.
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

I snutten over skriver vi en tekst `"hallo der"` til filen inni den nye mappen `mappe2/teksthilsen.txt`.
Når vi har gjort det kan vi ikke bruke rmdir før vi sletter filen.

---


#### Flagg til kommandoen `rm`
Det kan ta lang tid å slette en og en fil.
Du kan gå inn i en mappe du skal slette og skrive `rm *`.
Da sletter du alt innholdet i mappen, utenom skjulte mapper og filer, dvs mapper og filer som starter med `.`.
For eksempel:

---

```
❯ mkdir burkek
❯ cd burkek/
❯ mkdir .whatlol
❯ ls
❯ 
❯ rm *
fish: No matches for wildcard '*'. See `help wildcards-globbing`.
rm *
   ^
❯ ls
❯ ls -al
total 12
drwxrwxr-x  3 eindride eindride 4096 Jul 28 22:11 ./
drwxrwxr-x 11 eindride eindride 4096 Jul 28 22:11 ../
drwxrwxr-x  2 eindride eindride 4096 Jul 28 22:11 .whatlol/
❯ touch .whatkek.txt
❯ rm *
fish: No matches for wildcard '*'. See `help wildcards-globbing`.
rm *
   ^
❯ ls -al
total 12
drwxrwxr-x  3 eindride eindride 4096 Jul 28 22:12 ./
drwxrwxr-x 11 eindride eindride 4096 Jul 28 22:11 ../
drwxrwxr-x  2 eindride eindride 4096 Jul 28 22:11 .whatlol/
-rw-rw-r--  1 eindride eindride    0 Jul 28 22:12 .whatkek.txt
```

---

Nyttig for å

* Ikke slette config-filer osv med uhell
* Ikke slette **versjonskontrollen** din hvis du er uheldig og skriver `rm *` med uhell!

* I tillegg kan man også gi flagg til å slette hele mappestrukturer med `rm`, men vi behandler ikke det her. Søk det opp hvis du trenger det, og vær forsiktig med kommandoen!
