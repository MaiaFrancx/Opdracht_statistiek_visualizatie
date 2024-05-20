# Opdracht_statistiek_visualizatie

Kurt Farasyn, Maia Francx De Gelder, Adinda De Coster


Beste Tim,

Hierbij de instructies on de GitHub https://github.com/MaiaFrancx/Opdracht_statistiek_visualizatie te gebruiken.

## Te installeren

De .yaml-file staat rechtstreeks in de root-directory van dit project.


## Deel 1 : Productieproces modeleren

Voor dit deel moet slechts 1 Notebook <b>"xxxxx.ipynb"</b> worden uitgevoerd.
Die Notebook verwijst naar het <b>Tools.py</b> bestand (ondergebracht in Scripts) waarin imports, plot styles, en functies worden gedefinieerd.

Er werd geopteerd om zowel het Prodcutieproces van Brussel (BRU) als van Stockholm (STO) te analyseren en te modeleren. <br>
De visualisaties voor beide steden worden telkens naast elkaar getoond. <br>


### Data Analyse

- Een eerste visualisatie toont de productie over de voorbije jaren. <br>
Hierbij valt op dat de maximale productie (rode lijn) nooit wordt bereikt en dat er behoorlijk wat dagen met nul-productie zijn. <br>
Zoals aangegeven in de opgave, worden de dagen met nul-productie wegens maintenance uit de dataset verwijderd. <br>

- Het histogram voor de productie in <u>Brussel</u> toont een aanzienlijk aantal nul-dagen, met daarnaast een productie die normaal verdeeld lijkt en nauwelijks outliers kent.

- Het histogram voor de productie in <u>Stockholm</u> toont minder nul-dagen, met daarnaast een productie die iets minder normaal verdeeld lijkt door de aanwezigheid van toch wel wat outliers.


### Modeleren van 1 Productiedag

Het modeleren van een productiedag bestaat uit het bepalen van <br>
- enerzijds het percentage nul-dagen (18% voor BRU, 7% voor STO), en <br>
- anderzijds de parameters van de normaalverdeling die de niet-nul-dagen het best fit. <br>

Aangezien de niet-nul-producties meer normaalverdeeld zijn voor BRU dan voor STO, <br>
wordt er verwacht dat de "normaal-fitting" beter zal zijn voor BRU dan voor STO. <br>


### Simuleren van 1 Productiedag

Op basis van het model, wordt een BRU/STO dagproductie 2000 keer gesimuleerd. <br>
Daarna wordt het density histogram van de simulaties vergeleken met het densitiy histogram van de oorspronkelijke observaties. <br>
De simulatie is uitstekend voor BRU, en meer dan behoorlijk voor STO. <br>


### Simuleren van n Productiedagen

Een gesimuleerde productie voor een periode van n dagen is de <b>som</b> van n gesimuleerde dagproducties. <br>
Op basis van het model, wordt de BRU/STO productie voor een periode van n dagen 2000 keer gesimuleerd. <br>
De 2000 gesimuleerde producties voor een periode van n dagen worden gevisualiseerd in een histogram.

Met n = 7, merken we dat de BRU/STO weekproductie al neigt naar een normale verdeling.
De BRU weekproductie toont nog wat "gaten" die te wijten zijn aan de grote kans (18%) op nul-productie.


### Centrale Limietstelling

(...)




## Deel 2 : Verkoop tweedehands Volvo's

Voor dit deel moet slechts 1 Notebook <b>"yyyyyyy.ipynb"</b> worden uitgevoerd.
Die Notebook bevat zowel de code om de data te manipuleren en te visualiseren, alsook de antwoorden op de vragen.

