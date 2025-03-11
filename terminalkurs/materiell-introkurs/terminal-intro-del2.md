---
marp: true

theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')

---

# Del 2 av intro til terminalen

---

## Kommandoer med flere programmer

Du kan kjøre mange programmer i en enkelt kommando, samt
bruke resultatene fra ett program som input til et annet program, i samme kommando.

Dette gjør at du kan "lime" sammen programmer og operasjoner.

---

## Kjøring av flere programmer

Du kan kjøre flere programmer i en kommando på flere måter.
Dersom du ikke skal bruke resultatet fra en som input i neste, er det to måter å gjøre dette på.
Du kan enten velge å kjøre programmene slik at hvis ett program feiler, avbrytes kommandoen din.
Det andre alternativet kjører alle programmene i kommandoen uavhengig av om et
enkeltprogram feiler underveis.

---

### Lag flere mapper og filer i en kommando

Vi kan lage en mappe med noen filer inni med å kombinere flere kommandoer til én.
Etterpå bruker vi kommandoen `tree` for å vise mappestrukturen.
Du skal senere lære hvordan du kan installere programmer som `tree`.

---

```
❯ mkdir oppgaver && touch oppgaver/heiverden.txt
tree .
❯ tree .
.
├── hei.txt
├── oppgaver
│   └── heiverden.txt
└── verden.txt

1 directory, 3 files
```

---


Vanligvis er det lurt å bruke `&&` for å kombinere kommandoer, slik vi gjorde i sted.
Hvis en av delkommandoene feiler, avbrytes kjøringen. Dette er fornuftig hvis kommandoer
etterpå avhenger av noe de forrige kommandoene har gjort, som f.eks å lage en mappe eller
installere et program.


---

### Sett sammen flere 'urelaterte' kommandoer.

anta nå at vi forsøker følgende:

```
❯ mkdir oppgaver/kap1/kompletthetsprinsippet; touch readme-please.md
mkdir: cannot create directory ‘oppgaver/kap1/kompletthetsprinsippet’: No such file or directory
❯ ls
readme-please.md
```

Som du ser feilet den første kommandoen (hvorfor?), men den andre ble likevel kjørt.
Hvis du hadde brukt `&&` hadde ikke den andre kommandoen blitt kjørt når den første feilet.
Prøv selv!

---

## Bruk av pipes og redirects

I én fil `tomatoes.txt` ligger det følgende tekst

```
To tomater gikk over veien. Så ble den ene påkjørt
Da ropte den andre: "Come on! Catch up!"
```

I en annen fil `walljoke.txt` ligger 

```
Hva sa den ene veggen til den andre veggen?
Vi møtes på hjørnet!
```

Vi ønsker å kombinere disse til en fil `jokes.txt`.

Hvordan?

---

```
cat tomatoes.txt walljoke.txt > jokes.txt
```


## Bruk av `>>`
Åge har lært seg å programmere i python.
