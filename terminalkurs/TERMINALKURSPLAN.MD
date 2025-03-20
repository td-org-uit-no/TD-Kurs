
# TD-terminal:

## Problemet: selge det inn til studentene

### usecases:
    * Lag flere lag av mapper i en enkel kommando
    * Reproduserbare handlinger og eksperimenter
    * Sette sammen kjøring av flere programmer(pipes, scripts, makefiles)
    * Senere på uit og i arbeidslivet MÅ dere bruke terminal; innlogging på servere via ssh etc.

Nyttig krydder:
    * pushd (push directory) og popd (pop directory)

    * ncal -w : se hvilken dato det er og hvilken uke man er i
    * lag en snakkende kalkulator (oneliner)



### Ønsket tilstand hos studenter etter å ha tatt introkurs og øvet litt på oppgaver

#### Ferdigheter
* Studenten kan navigere i terminalen ved hjelp av cd, ls, pwd, pushd, popd
* Studenten kan lage nye filer og mapper ved hjelp av touch og mkdir
* Studenten kan lage nøstede mappestrukturer ved hjelp av mkdir -p
* Studenten kan flytte filer og gi filer nytt navn ved hjelp av mv
* Studenten kan kopiere filer ved hjelp av cp
* Studenten kan slette hele mapper ved hjelp av rm -rf og tomme mapper ved hjelp av rmdir

* Studenten kan kombinere kommandoer i terminalen ved hjelp av &&
* Studenten kan binde sammen output fra ett program til input til et annet ved hjelp av pipes |
* Studenten kan bruke cat, more, less head og tail til inspisere filer
* Studenten kan bruke redirects (> og >>) for å skrive standard output til fil.

* Kunne kjøre programmer i terminalen (executables og f.eks python-programmer)
* Bruke pakkemanager (som apt-get) sammen med sudo for å installere programmer


#### Kunnskap
* Studenten vet hva en terminal og gi eksempler på hva den kan brukes til
* Studenten kan forklare forskjellen mellom grafiske brukergrensesnitt (GUI) og kommandolinjegrensesnitt (CLI)
* Studenten kan gjøre rede for filsystemets trestruktur
* Studenten kjenner til at det finnes ulike måter å kommunisere med maskinen i en terminal ved
  hjelp av shell-språk som f.eks bash, zsh og fish
* Kjenne til verktøy som IPython
* Studenten kjenner til tekstbehandlingsverktøy som nano, vi/vim, og kan også komme seg tilbake til terminalen fra disse.


#### Kompetanse
* Studenten kan forstå enkle shell-scripts
* Studenten kan slå opp informasjon om hvordan man gjør ulike operasjoner


### Ønsket tilstand hos studenter etter å ha tatt et oppfølgingskurs og øvet litt på oppgaver

#### Ferdigheter 
* Studenten kan bruke enkle regexer ved hjelp av grep til å filtrere output fra cat, head, tail
* Studenten kan bruke verktøy som wc, cloq og uniq for å telle antall unike ord i en fil, antall linjer kode etc
* Studenten kan skrive enkle shell-scripts med variabler, løkker og betingelser for å automatisere oppgaver og forstå gangen i mer avanserte AI-genererte shell-scripts
* Studenten kan lage enkle makefiles for å kompilere C-kode, Latex-dokumenter etc. og kombinere dette med enkle shell-scipts.
* Studenten kan endre PATH-variabelen i sitt eget miljø slik at man enklere kan forenkle sin egen arbeidsflyt ved hjelp av scripts.
* Studenten kan gjøre enkel bruk av teksteditorer som nano, vi/vim eller andre.
* Studenten kan bruke htop til enkel overvåking av systemressurser.
* Studenten kan bruke kommandoer som `ping`, `ssh` `scp`, `curl` og `wget` for grunnleggende nettverksoperasjoner
* Bruke pakkemanager (som apt-get) sammen med sudo for å installere programmer, fjerne programmer og oppdatere programmer.
* Studenten kan bruke `man` og `--help` for å forstå hvordan forskjellige kommandoer brukes.


#### Kunnskap
* Studenten forstår grunnleggende flytkontrollstruktur som løkker og betingelser
* Studenten forstår grunnleggende bruk av `.bash_profile`, `.bashrc` og andre konfigurasjonsfiler.


#### Kompetanse
* Studenten kan gjøre enkel bruk av man-pages




### Ønsket tilstand hos studenter etter å ha tatt et kurs i mer avansert terminalbruk


### Ferdigheter
* Overvåke systemressurser med og prosesser med `htop`, `ps`, `netstat`
* Anvende `bg`, `fg` `jobs` og signaler som `kill`.
* Bruke pakkemanager (som `apt`, `yum` eller `pacman`) sammen med sudo for å installere programmer, fjerne programmer, oppdatere programmer og legge til kilder for programmer som ikke følger som standard med systemet.
* Utføre enkel sikkerhetskopiering og gjennoppretting med kommandoer som `tar` og `rsync`


