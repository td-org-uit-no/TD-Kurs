# Oppgaver for introkurs til terminalen

## Oppgave: Navigering og flytting av filer

### a)
Bruk terminalen til å navigere inn i mappen `foldersystem`,
og finn ut hvilke filer og mapper den inneholder.
Bruk kommandoen `ls` med ulike `options` som f.eks `ls -l`.

Hvordan finner du skjulte filer og mapper med `ls`?
Les litt ved å skrive `man ls` i terminalen

### b)
* Hva heter tekstfilene i mappa `foldersystem/documents`?

Les om programmene `head` og `tail` ved å lese manual-siden (`man head` etc.)

* Hvordan kan du lese ut de 20 første linjene i filen `book-excerpt.txt?
* Hvordan kan du lese ut de 20 siste linjene?
* Hva inneholder filen?

Skriv `man wc` i terminalen din. Du skal nå få en `manual page` for et program som
heter `wc`, en forkortelse for *word-count*.

* Hvor mange ord er det i teksten?
* Hvor mange linjer er det i teksten?
* Kan du finne ut hvilken bok denne teksten er hentet fra?

### c)
Få datamaskinen din til å lese de 5 første linjene høyt.
Hint, bruk `head`, pipes (`|`) og `espeak`

* Hvis du ikke har `espeak` installert kan du prøve å installere den med 
`sudo apt install espeak`

### d)
Bruk kommandoene `mv` og `mkdir` til å flytte boka inn i mappen `books/mysteries/whats-this-book/mysterybook-excerpt`.


## Oppgave: Sletting av mapper

Lag en mappe `tmp-dir`.
Slett mappen `tmp-dir` med å bruke `rmdir`.


Lag en ny mappe `tmp-dir-nonempty`.
Legg inn en hilsen i mappen. Du kan for eksempel lage en tom fil med å bruke `touch`.

Hva skjer hvis du nå prøver å slette mappen med `rmdir` ?

## Oppgave: Slett en mappe med masse innhold

Mappen `foldersystem/documents/lots-of-unneccessary-files/` inneholder
masse filer som bare inneholder tull og tøys.
Slett alle filene med én kommando.
Slett deretter mappen med `rmdir`

## Oppgave: Undersøk Shakespeares samlede verker.

Berømte dramatikere som William Shakespeare og Henrik Ibsen siteres ofte.
I mappen `foldersystem/documents/books/gutenberg/shakespeare/` er
det et script `getbook.sh` som laster ned shakespeares samlede verker.


b) Bruk scriptet til å laste ned Shakespeares samlede verker.
a) Gi filen `famous-book.txt` et nytt navn `shakespeare-collected-works.txt`.

c)
* Hvor mange linjer er det i tekstfilen?
* Hvor mange ord er det i tekstfilen?
* Hva står på de 2 første og de 2 siste linjene?
* Kan du få datamaskinen din til å lese de 5 siste linjene høyt?

### Utfordring: Finn sitater.
Et shakespeare-sitat sier følgende:

```
The fault, dear Brutus, is not in our stars, but in ourselves
```

Finn hvilket linjenummer dette sitatet står på.
Hint (bruk `cat`, pipes (`|`) og filtrer med `grep -nEi`)

Hva skjer hvis du i stedet skriver
* Hva gjør `grep -nE` ?
* Hva gjør `grep -E` ?


### c)
På siden [goodreads](https://www.goodreads.com/author/quotes/947.William_Shakespeare)
kan du finne flere Shakespeare-sitater. Finn ut hvilken linje disse står på i de 
samlede verkene.


## Oppgave: Kopier en fil og finn flere sitater

På [project gutenberg](https://www.gutenberg.org/cache/epub/13041/pg13041.txt)
finner du boken "Vildanden" av Henrik Ibsen. 

a) Kopier scriptet i forrige oppgave inn i en ny mappe 
`foldersystem/documents/books/gutenberg/ibsen-vildanden`

b) Modifiser scriptet slik at det laster ned boken til Ibsen i stedet for boken til Shakespeare,
og at boken lagres i en tekstfil 'vildanden.txt'

c) Anslå hvor mange prosent av linjene i teksten som inneholder navnet til 
karakteren Gina.


### Utfordring:
Noen synes det er kult med Ibsen-sitater. Kan du finne ut hvor noen 
på nettet som er fra Vildanden og sjekke om de finnes i teksten, og hvilke
linjer de står på?



## Lagre standard-output fra programmer til fil
Mange programmer skriver bare rett ut til terminalen. Da sier 
vi ofte at de skriver til standard-output. 
I mappen `foldersystem/scripts/weather/yr/weather-logs/`
finner du et script som laster ned temperaturer fra et API til
meteorologisk institutt.

Du vil gjerne logge disse dataene. I mappen finner du også 
en fil `temperatures.txt`.

* Kjør scriptet
* Kan du omdirigere output fra terminalen til `temperatures.txt`?
