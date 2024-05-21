# Opdracht Statistiek Visualisaties

Kurt Farasyn, Maia Francx De Gelder, Adinda De Coster <br>
Mei 2024
<br>
<br>

Beste Tim,

Hierbij de instructies om de GitHub https://github.com/MaiaFrancx/Opdracht_statistiek_visualizatie te gebruiken.

## Te installeren

De .yaml-file staat rechtstreeks in de root-directory van dit project. <br>
<br>


## Deel 1 : Productieproces modeleren

Voor dit deel moet slechts 1 Notebook <b>"productieproces-kf.ipynb"</b> worden uitgevoerd. <br>
Die Notebook verwijst naar het <b>Tools.py</b> bestand (ondergebracht in Scripts) waarin imports, plot styles, en functies worden gedefinieerd.

Er werd geopteerd om zowel het Prodcutieproces van Brussel (BRU) als van Stockholm (STO) te analyseren en te modelleren. <br>
De visualisaties voor beide steden worden telkens naast elkaar getoond. <br>


### Data Analyse

- Een eerste visualisatie toont de productie over de voorbije jaren. <br>
Hierbij valt op dat de maximale productie (rode lijn) nooit wordt bereikt en dat er behoorlijk wat dagen met nul-productie zijn. <br>
Zoals aangegeven in de opgave, worden de dagen met <b>nul-productie wegens maintenance</b> uit de dataset <b>verwijderd</b>. <br>
<br>
- Het histogram voor de productie in <b>Brussel</b> toont een aanzienlijk aantal nul-dagen, <br>
met daarnaast een productie die normaalverdeeld lijkt en nauwelijks outliers kent. <br>
<br>
- Het histogram voor de productie in <b>Stockholm</b> toont minder nul-dagen, <br>
met daarnaast een productie die iets minder normaalverdeeld lijkt door de aanwezigheid van toch wel wat outliers. <br>


### Modeleren van 1 Productiedag

Het modeleren van een productiedag bestaat uit het bepalen van <br>
- enerzijds het percentage nul-dagen (18% voor BRU, 7% voor STO), en <br>
- anderzijds de parameters van de normaalverdeling die de niet-nul-dagen het best fit. <br>

Aangezien de niet-nul-producties meer normaalverdeeld zijn voor BRU dan voor STO, <br>
wordt er verwacht dat de "normaal-fitting" beter zal zijn voor BRU dan voor STO. <br>


### Simuleren van 1 Productiedag

Op basis van het model, wordt een BRU/STO dagproductie 2000 keer gesimuleerd. <br>
Daarna wordt het density histogram van de simulaties vergeleken met het densitiy histogram van de oorspronkelijke observaties. <br>
De overeenkomst is uitstekend voor BRU, en meer dan behoorlijk voor STO. <br>


### Simuleren van n Productiedagen

Een gesimuleerde productie voor een periode van n dagen is de <b>som</b> van n gesimuleerde dagproducties. <br>
Op basis van het model, wordt de BRU/STO productie voor een periode van n dagen 2000 keer gesimuleerd. <br>
De 2000 gesimuleerde BRU/STO producties voor een periode van n dagen worden gevisualiseerd in een histogram en in een empirische cumulatieve distributiefunctie (ecdf).

Met n = 7, merken we dat de BRU/STO weekproductie neigt naar een normale verdeling. <br>
De BRU weekproductie toont nog wat "gaten" die te wijten zijn aan de grote kans (18%) op nul-productie. <br>
<font color="blue"> Merk op dat je de waarde van n in de Notebook zelf kan wijzigen. <br>
    
Rode vertikale lijnen zijn toegevoegd aan de ecdf visualisaties. <br>
Die lijnen markeren de kans dat de productie voor een periode van n dagen respectievelijk lager ligt dan 25%, 50% en 75% van de theoretisch maximale productie voor een periode van n dagen.


### Centrale Limietstelling    

De Centrale Limietstelling zegt dat de <b>som_n</b> van een willekeurig variabele, hier de BRU/STO dagproductie, <br>
meer en meer normaalverdeeld wordt, naarmate n toeneemt. <br>
Die vaststelling was al zichtbaar in bovenstaande histogrammen en ecdf's voor n = 7. <br>
De laatste visualisatie verduidelijkt die toenemende normalisatie voor respectievelijk n = 2, 5, 10 en 20. <br>
<font color="blue"> Merk op dat je de waarden van n in de Notebook zelf kan wijzigen. <br>
<br>    


## Deel 2 : Verkoop tweedehands Volvo's

Voor dit deel moet slechts 1 Notebook <b>"autoproductie.ipynb"</b> worden uitgevoerd. <br>
Die Notebook bevat zowel de code om de data te manipuleren en te visualiseren, alsook de antwoorden op de vragen. <br>
<br>
