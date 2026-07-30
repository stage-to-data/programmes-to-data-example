<!-- Scored against ground truth commit c7fc5733. Corrected values for the
     Levenshtein/WER/CER-on-matches columns below are in ../../corrected-metrics.md
     Scatter plots omitted; regenerate them from scores.json. -->

# LLM Evaluation (prompt-3)

"_results/final-tests/prompt-3/transcriptions_" (**151 files**) was tested against _evaluation/ground-truth/md_ (**151 files**). Found **0 missing files**.

Evaluation word count : 37466 (2-798), character count: 256585 (15-5438)

## Full file-level analyses

- **Mean Levenshtein ratio (raw)** : 0.9584.
- **Mean Levenshtein ratio (parsed)** : 0.9718.
- **Mean Levenshtein ratio (raw, weighted by word)** : 0.9767.
- **Mean Levenshtein ratio (parsed, weighted by word)** : 0.9845.

### 10 worst Levenshtein ratios:

- 0.2703 : Bnf_fds_ChroniquesDuneFinDaprèsmidiMiseEnScèneDePierre _FDA1988_page_4.md
- 0.6262 : CommAvignon_fds_lesIdiots_FDA2015_page_1.md
- 0.7404 : CommAvignon_fds_dieEheDerMariaBraun_FDA2014_page_1.md
- 0.7651 : CommAvignon_fds_laMaisonDeThe_FDA2019_page_1.md
- 0.7913 : CommAvignon_fds_enAtendant_FDA2023_page_5.md
- 0.8308 : 349953_667c39485f230-1_page_1.md
- 0.8558 : Bnf_fds_Genesi FromTheMuseumOfSleepMiseEnScèneDeRomeoC_FDA2000_page_1.md
- 0.9059 : Bnf_fds_HommageÀLaArgentinaSpectacleDeKazuoOonoMaMère_FDA1982_page_1.md
- 0.9070 : 05_ Thyeste_FDS2018_page_1.md
- 0.9128 : CommAvignon_fds_laPrincesseMaleine_FDA2017_page_1.md


## Precision/recall

- **Mean precision** : 0.7630.
- **Mean recall** : 0.8209.

- **Mean WER on matches** : 0.3234.
- **Mean CER on matches** : 0.4335.
- **Mean Levenshtein on matches** : 0.8852.
---
- **Mean precision (word-weighted)** : 0.8001.
- **Mean recall (word-weighted)** : 0.8512.

- **Mean WER on matches (word-weighted)** : 0.2890.
- **Mean CER on matches (word-weighted)** : 0.3688.
- **Mean Levenshtein on matches (word-weighted)** : 0.9014.

## NER Precision/recall

- **Mean precision** : 0.9161.
- **Mean recall** : 0.8954.

- **Mean WER on matches** : 0.1107.
- **Mean CER on matches** : 0.0963.
- **Mean Levenshtein on matches** : 0.9432.
---
- **Mean precision (word weighted)** : 0.9444.
- **Mean recall (word weighted)** : 0.9087.

- **Mean WER on matches (word weighted)** : 0.1196.
- **Mean CER on matches (word weighted)** : 0.1088.
- **Mean Levenshtein on matches (word weighted)** : 0.9439.

### 10 Worst NER Precision scores:

349953_667c39485f230-1_page_2.md (mean NER precision: **0.9000**, mean CER on matches **1.305836390824136** :

|Prediction|Reference|
|---|---|
|Absalon|William Faulkner|
|Absalon !|France Séverine Chavrier|
|William Faulkner|JUIN|
|France Séverine Chavrier|AVEC|
|JUIN|COMPRIS Création Festival d'Avignon 2024|
|AVEC|In French|
|COMPRIS Création Festival d'Avignon 2024|English|
|In French|Les Palmiers sauvages|
|English|Séverine Chavrier|
|Les Palmiers sauvages|William Faulkner|
|Séverine Chavrier|Absalon|
|William Faulkner|Absalon ! Œuvre-monde|
|Absalon|David|
|Absalon ! L'œuvre-monde|Absalon !|
|David|Thomas Sutpen|
|Absalon|Mississipi|
|Thomas Sutpen|Séverine Chavrier|
|Mississippi|Faulkner|
|Séverine Chavrier|Hantés|
|Faulkner|The Wild Palms|
|Hantés|Séverine Chavrier|
|The Wild Palms|William Faulkner|
|Séverine Chavrier|Absalom|
|William Faulkner|Absalom|
|Absalom|America of the Civil War|
|Absalom|David|
|America of the Civil War|Absalom|
|David|Absalom|
|Thomas Sutpen|Thomas Sutpen|
|Mississippi|Mississippi|
|Greek|Greek|
|Faulkner|Faulkner|
|guerra de Secesión|guerra de Secesión|
|Faulkner|Faulkner|
|Spectacle|Spectacle|
|Festival d'Avignon|Festival d'Avignon|


CommAvignon_fds_dieEheDerMariaBraun_FDA2014_page_1.md (mean NER precision: **0.6667**, mean CER on matches **1.25** :

|Prediction|Reference|
|---|---|
|JUIL|France|
|France|JUIL|


CommAvignon_fds_lesIdiots_FDA2015_page_2.md (mean NER precision: **0.8070**, mean CER on matches **1.1481650567619628** :

|Prediction|Reference|
|---|---|
|Moscou|IDIOTS D'APRÈS LARS|
|IDIOTS D'APRÈS LARS|TRIER KIRILL SEREBRENNIKOV|
|TRIER KIRILL SEREBRENNIKOV|Madame Filipp Avdeev|
|France|La secrétaire au tribunal|
|Yulia Aug Madame Filipp Avdeev|La chef de la secrétaire|
|La secrétaire au tribunal|Olga Woof|
|La chef de la secrétaire|La juge Oksana Fandera|
|Olga Woof|Karina Sergey Galakhov|
|La juge Oksana Fandera|Le serveur|
|Karina Sergey Galakhov L'officier|L’agent|
|Le serveur|Le policier|
|L'agent|Le frère de Masha|
|Le policier|Un homme|
|Le frère de Masha|Le gestionnaire|
|Un homme|Le mari de|
|Le gestionnaire|L’acheteur|
|Le mari de|Le chef de Sergey|
|L'acheteur|Kachan|
|Le chef de Sergey|Un homme|
|Kachan|Le père de Karina|
|Un homme|Sergey Olga Naumenko|
|Le père de Karina|La femme au foyer|
|Sergey Olga Naumenko|La tante d’Elisey|
|La femme au foyer|La mère de Karina|
|La tante d'Elisey|Aleksandra Revenko|
|La mère de Karina|Mathieu Beaufort|
|Aleksandra Revenko Katya|Laura Deleaz|
|Mathieu Beaufort|Amandine Huynh|
|Laura Deleaz|Nedjma Ortiz|
|Amandine Huynh|Clément Paimpara Mise|
|Nedjma Ortiz|Kirill Serebrennikov|
|Clément Paimpara Mise|Kirill Serebrennikov|
|Kirill Serebrennikov|Vera Martynova Chorégraphie|
|Kirill Serebrennikov|Alevtina Rudina Lumière|
|Vera Martynova Chorégraphie|Igor Kapustin Traduction|
|Alevtina Rudina Lumière|Macha Zonina Production :|
|Igor Kapustin Traduction|Gogol Center|
|Macha Zonina Production :|Moscou|
|Gogol Center|de France|
|Moscou|Russie|
|Russie|Russie|
|Russie|Office national de diffusion artistique et de|
|l'Onda Office national de diffusion artistique|EN+ Group Spectacle|
|EN+ Group Spectacle|Gogol Center|
|Gogol Center|Moscou|
|Russie|Russie|


Bnf_fds_ChroniquesDuneFinDaprèsmidiMiseEnScèneDePierre _FDA1988_page_4.md (mean NER precision: **0.0000**, mean CER on matches **1** :

|Prediction|Reference|
|---|---|


Bnf_fds_LesAveugles FantasmagorieTechnologiqueConceptionEtR_FDA2002_page_2.md (mean NER precision: **0.9833**, mean CER on matches **0.9724105585597843** :

|Prediction|Reference|
|---|---|
|France|France|
|Chapelle|Chapelle|
|lycée St Joseph|lycée St Joseph|
|Les Aveugles|Maurice Maeterlinck|
|Maurice Maeterlinck|Denis Marleau|
|Denis Marleau|Céline Bonnier|
|Céline Bonnier|Paul Savoie|
|Paul Savoie|Jasmin|
|Jasmin|Pierre Laniel|
|Pierre Laniel|Nancy Tobin|
|Nancy Tobin|Yves Labelle|
|Yves Labelle|Michel Pétrin|
|Michel Pétrin|UBU|
|UBU|Gilbert Grondin|
|Gilbert Grondin|Pierre Bérubé|
|Pierre Bérubé|Claude Rodrigue|
|Claude Rodrigue|Pierre Laniel|
|Pierre Laniel|Angelo Barsetti|
|Angelo Barsetti|Élaine Hamel|
|Elaine Hamel|Valérie Delacroix|
|Valérie Delacroix|Mathieu Saint-Arnaud|
|Mathieu Saint-Arnaud|Mathieu Gallien|
|Mathieu Gatien|Solveig Hansen|
|Solveig Hansen|Guillerrnina Kerwin|
|Guillermina Kerwin|Productions Yves Nicol|
|Productions Yves Nicol|Boscus|
|Boscus|Annie Gélinas Coproduction|
|Annie Gélinas Coproduction UBU|Montréal|
|Montréal|Festival d'Avignon UBU|
|Festival d'Avignon UBU|Conseil des arts et des lettres du Québec|
|Conseil des arts et des lettres du Québec|Conseil des arts du Canada|
|Conseil des arts du Canada|Conseil des arts de Montréal|
|Conseil des arts de Montréal|Commerce international du Canada|
|Commerce international du Canada|ministère de la Culture|
|ministère de la Culture|Communications du Québec|
|Communications du Québec|Fonds de stabilisation|
|Fonds de stabilisation|Québec|
|Québec|Canada|
|Canada|Berlin|
|Berlin|Bruxelles|
|Bruxelles|Centre|
|Centre|Canada|
|Canada|Paris|
|Paris|Délégation générale du Québec|
|Délégation générale du Québec|Paris|
|Paris|Denis Marleau|
|Denis Marleau|Monde des rencontres|
|Monde des rencontres|Jardin de la rue de Mons|
|Jardin de la rue de Mons|Fnac d'Avignon|
|Fnac d'Avignon|Les Aveugles|
|Festival International d'Édimbourg|Festival International d'Édimbourg|
|Écosse|Écosse|
|Format 2002|Format 2002|
|Bruges|Bruges|
|Belgique|Belgique|
|Festival des arts technologiques|Festival des arts technologiques|
|Compiègne|Compiègne|
|Tessa Goulet|Tessa Goulet|
|tgoulet@theatreubu.ca|tgoulet@theatreubu.ca|


CommAvignon_fds_enAtendant_FDA2023_page_5.md (mean NER precision: **0.8966**, mean CER on matches **0.9199298200236287** :

|Prediction|Reference|
|---|---|
|XIVe|XIVe|
|En Attendant|En Atendant|
|l'importance|l'importance|
|d'En Attendant|d'En Atendant|
|XIVe|XIVe|
|Covid-19|Covid-19|
|EXIT ABOVE|EXIT ABOVE|
|En Attendant|En Atendant|
|Titanic|Titanic|
|Marc Blanchet|Marc Blanchet|
|En Attendant|En Atendant|
|Vertu|Vertu|
|Si|Si|
|Tant|Tant|
|Je nen puis aprocher|Je nen puis aprocher|
|Attendant|Atendant|
|English|Car|
|God|Dieu|
|Pity|Si Pitié|
|God|Je n’en|
|En Attendant|Je vivrais dans l’espoir du grand bonheur|
|Si Pitié|Atendant|
|Dieu|English|
|Car|God|
|Je n'en|Pity|
|Je vivrais dans l'espoir du grand bonheur|God|


CommAvignon_fds_lePetitChaperonRouge_FDA2022_page_2.md (mean NER precision: **0.9524**, mean CER on matches **0.8286361918656364** :

|Prediction|Reference|
|---|---|
|THÉÂTRE – JEUNE PUBLIC|THÉÂTRE – JEUNE PUBLIC|
|ROUGE|ROUGE|
|WILHELM GRIMM DAS|WILHELM GRIMM DAS|
|PLATEAU|PLATEAU|
|Paris|Paris|
|CRÉATION Durée|CRÉATION Durée|
|Antoine Oppenheim|Antoine Oppenheim|
|Maëlys Ricordeau|Maëlys Ricordeau|
|Jacob|Jacob|
|Wilhelm Grimm Traduction|Wilhelm Grimm Traduction|
|Natacha Rimasson-Fertin|Natacha Rimasson-Fertin|
|d'Olivier Cadiot Mise|d'Olivier Cadiot Mise|
|Céleste Germe Collaboration|Céleste Germe Collaboration|
|Maëlys Ricordeau Musique J. Stambach|Maëlys Ricordeau Musique|
|James Brandily Lumière|James Brandily Lumière|
|Sébastien Lefèvre|Sébastien Lefèvre Images|
|Flavie Trichet-Lespagnol Son|Flavie Trichet-Lespagnol Son|
|Jérôme Tuncer Costumes|Jérôme Tuncer Costumes|
|Mathilde Wind Sculptures|Mathilde Wind Sculptures|
|Julia Morlot|Julia Morlot|
|Jérémy Page Réalisation|Jérémy Page Réalisation|
|Pascale Dufray Construction|Pascale Dufray Construction|
|Benjamin Bertrand Régie|Benjamin Bertrand Régie|
|Pablo Simonet Régie|Pablo Simonet Régie|
|Emile Denize Régie|Emile Denize Régie|
|Virginie Watrinet|Virginie Watrinet|
|Lila Burdet Administration|Lila Burdet Administration|
|Emilie Henin|Emilie Henin|
|Léa Coutel|Léa Coutel|
|Le Grand R Scène|Théâtre Jean-Vilar de Vitry-sur-Seine|
|Roche-sur-Yon|Le Grand R Scène|
|Festival d'Avignon|Roche-sur-Yon|
|Théâtre Nouvelle Génération|Festival d'Avignon|
|Lyon|Théâtre Nouvelle Génération|
|Nanterre-Amandiers|Lyon|
|La Comédie de Colmar|Nanterre-Amandiers|
|Grand Est Alsace|La Comédie de Colmar|
|Comédie de|Grand Est Alsace|
|Théâtre Gérard Philipe Centre|Comédie de|
|Saint-Denis|Théâtre Gérard Philipe Centre|
|La Villette Paris|Saint-Denis|
|CRÉA - Festival Momix - Scène|La Villette Paris|
|d'Intérêt National|CRÉA – Festival Momix - Scène|
|Kingersheim|d'Intérêt National|
|Théâtre National de Bretagne|Kingersheim|
|Rennes|Théâtre National de Bretagne|
|Le Grand Bleu|Rennes|
|Lille|Le Grand Bleu|
|Drac Île-de-France|Lille|
|Région Île-de-France|Drac Île-de-France|
|Département de l'Essonne|Région Île-de-France|
|Théâtre Brétigny|Département de l'Essonne|
|Fonds de production de la|Théâtre Brétigny|
|DGCA|Fonds de production de la|
|Département du Val-de-Marne Résidences Ferme|DGCA|
|Noisiel|Département du Val-de-Marne Résidences|
|Théâtre Jean-Vilar de Vitry-sur-Seine|Noisiel|
|Le Grand R Scène|Le Grand R Scène|
|Roche-sur-Yon Spectacle|Roche-sur-Yon Spectacle|
|Festival d'Avignon|Festival d'Avignon|


Bnf_fds_LeChevalierDOlmedoMiseEnScèneDeLluisPasqual_FDA1992_page_6.md (mean NER precision: **0.9750**, mean CER on matches **0.7803976013321492** :

|Prediction|Reference|
|---|---|
|Lluís Pasqual|Reus|
|Reus|Espagne|
|Espagne|Fabia Puigserver|
|Fabia Puigserver|Théâtre Lliure de Barcelone|
|Théâtre Lliure de Barcelone|Centro Dramatico Nacional-Teatro Maria Guerrero de Madrid|
|Centro Dramatico Nacional-Teatro Maria Guerrero de Madrid|Espagne|
|Espagne|La vie du roi|
|La vie du roi|Eduard II d'Angleterre|
|Eduard II d'Angleterre|Marlowe|
|Marlowe|Brecht|
|Brecht|Festival d'Avignon|
|Festival d'Avignon|Lumières de Bohème de|
|Lumières de Bohême de|l'Odéon-Théâtre de l'Europe|
|l'Odéon-Théâtre de l'Europe|Une des dernières soirées de carnaval|
|Une des dernières soirées de carnaval|Goldoni|
|Goldoni|El publico de|
|El publico de|García Lorca|
|Garcia Lorca|Lluís Pasqual|
|Giorgio Strehler|Giorgio Strehler|
|l'Odéon-Théâtre de l'Europe|l'Odéon-Théâtre de l'Europe|
|Pièce|Pièce|
|Garcia Lorca|Garcia Lorca|
|Le Balcon de Genet|Le Balcon de Genet|
|Tirano Banderas|Tirano Banderas|
|Valle-Inclán|Valle-Inclán|
|France|France|
|L'Enlèvement|L'Enlèvement|
|Mozart|Mozart|
|Théâtre du Châtelet|Théâtre du Châtelet|
|Paris|Paris|
|Le Turc|Le Turc|
|Italie|Italie|
|Rossini|Rossini|
|l'Opéra de Lille|l'Opéra de Lille|
|Chevalier d'Olmedo|Chevalier d'Olmedo|
|Zéno Bianu|Zéno Bianu|
|Actes Sud-Papiers|Actes Sud-Papiers|
|Alternative théâtrale|Alternative théâtrale|
|l'Odéon - Théâtre de l'Europe|l'Odéon - Théâtre de l'Europe|


CommAvignon_fds_enAtendant_FDA2023_page_2.md (mean NER precision: **0.8636**, mean CER on matches **0.7487912672123198** :

|Prediction|Reference|
|---|---|
|Belgique|Belgique|
|Anne Teresa De Keersmaeker|Anne Teresa De Keersmaeker|
|Cœur|Cour|
|l'Ars Subtilior|Cœur|
|XIVe|l’Ars Subtilior|
|Atendant|XIVe|
|Programmer En Atendant|Atendant|
|EXIT ABOVE|Programmer En Atendant|
|Anne Teresa De Keersmaeker|EXIT ABOVE|
|En Atendant|Anne Teresa De Keersmaeker|
|Belgium|En Atendant|
|Cour|Belgium|
|Cœur ensemble|Cœur ensemble|
|Ars Subtilior|Ars Subtilior|
|Black Death|Black Death|
|Atendant|Atendant|
|Programming En Atendant|Programming En Atendant|
|EXIT ABOVE|EXIT ABOVE|
|Festival d'Avignon|Festival d’Avignon|


Bnf_fds_TheAlvinAileyCityCenterDanceTheater_FDA1974_page_4.md (mean NER precision: **0.9828**, mean CER on matches **0.7254415325560993** :

|Prediction|Reference|
|---|---|
|Processional : Clover Mathis|Processional : Clover Mathis|
|Tina Yuan|Tina Yuan|
|Melvin Jones|Melvin Jones|
|Elbert Watson|Elbert Watson|
|Masazumi Chaya|Masazumi Chaya|
|Cynthia Penn|Cynthia Penn|
|Linda Kent|Linda Kent|
|Peter Woodin|Peter Woodin|
|Warren Spears|Warren Spears|
|Edward Love|Edward Love|
|Linda Kent|Linda Kent|
|Peter Woodin|Peter Woodin|
|Warren Spears|Warren Spears|
|Kelvin Rotardier|Kelvin Rotardier|
|Estelle Spurlock|Estelle Spurlock|
|Judith Jamison|Judith Jamison|
|Sara Yarborough|Sara Yarborough|
|Clive Thompson|Clive Thompson|
|Judith Jamison|Judith Jamison|
|Sara Yarborough|Sara Yarborough|
|Kelvin Rotardier|Kelvin Rotardier|
|Judith Jamison|Judith Jamison|
|Judith Jamison|Kelvin Rotardier|
|Ella Jenkins|Judith Jamison|
|A Man|Ella Jenkins|
|River|A Man|
|Ella Jenkins I Want|River|
|Dudley Williams|Ella Jenkins I Want|
|James Miller Move|Dudley Williams|
|Move Sinner Man|James Miller Move|
|Kenneth Pearl|Move Sinner Man|
|Hector Mercado|Kenneth Pearl|
|Clover Mathis|Hector Mercado|
|Clover Mathis|Clover Mathis|
|Hector Mercado|Clover Mathis|
|Masazumi Chaya|Hector Mercado|
|The Day is Past and Gone : La Compagnie You May Run Home : La Compagnie Arrangement : Brother|Masazumi Chaya|
|John Sellers|The Day is Past and Gone : La Compagnie You May Run Home : La Compagnie Arrangement : Brother|
|Howard Roberts|John Sellers|
|Bosom of|Howard Roberts|
|Compagnie Blues Suite|Bosom of|
|Créé en mars 1958|Compagnie Blues Suite|
|New-York|Créé en mars 1958|
|Alvin Ailey Décors|New-York|
|Ves Harper Lumières|Alvin Ailey Décors|
|Nicola Cernovitch|Ves Harper Lumières|
|John Sellers|Nicola Cernovitch|
|Noirs du Sud|John Sellers|
|Blues|Noirs du Sud|
|Good Morning Blues : La Compagnie Long Time :|Blues|
|Kelvin Rotardier|Good Morning Blues : La Compagnie Long Time :|
|Compagnie Mean Ol' Frisco|Compagnie Mean Ol' Frisco|
|Hector Mercado|Hector Mercado|
|Edward Love|Edward Love|
|Michihiko Oka|Michihiko Oka|
|Ulysses Dove|Ulysses Dove|
|Kenneth Pearl|Kenneth Pearl|


