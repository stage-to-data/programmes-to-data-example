<!-- Third-pass run, scored against ground truth commit 0d40e2fc (151 pages,
     36,417 words, 249,500 characters) — an earlier state of the corpus than the
     final-tests runs. The two are not comparable. Corrected values for the
     Levenshtein-on-matches columns are in ../../../corrected-metrics.md
     Scatter plots omitted; regenerate them from scores.json. -->

# LLM Evaluation (Prompt 1 (gpt))

"_third pass, prompt-1-gpt (transcriptions not kept in this repository)_" (**151 files**) was tested against _evaluation/ground-truth/md_ (**151 files**). Found **0 missing files**.

Evaluation word count : 36417 (0-798), character count: 249500 (0-5438)

## Full file-level analyses

- **Mean Levenshtein ratio (raw)** : 0.9138.
- **Mean Levenshtein ratio (parsed)** : 0.9309.
- **Mean Levenshtein ratio (raw, weighted by word)** : 0.9609.
- **Mean Levenshtein ratio (parsed, weighted by word)** : 0.9699.

### 10 worst Levenshtein ratios:

- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_2.txt
- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_3.txt
- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_1.txt
- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_4.txt
- 0.0153 : Bnf_fds_ChroniquesDuneFinDaprèsmidiMiseEnScèneDePierre _FDA1988_page_4.txt
- 0.6230 : Bnf_fds_LeChevalierDOlmedoMiseEnScèneDeLluisPasqual_FDA1992_page_1.txt
- 0.6744 : CommAvignon_fds_lesIdiots_FDA2015_page_1.txt
- 0.7488 : Bnf_fds_BéréniceMiseEnScèneDeLambertWilson_FDA2001_page_1.txt
- 0.7569 : Bnf_fds_LaTragiqueHistoireDHamletPrinceDeDanemarkMiseEn _FDA1977_page_2.txt
- 0.7733 : CommAvignon_fds_laMaisonDeThe_FDA2019_page_1.txt


## Precision/recall

- **Mean precision** : 0.7254.
- **Mean recall** : 0.7692.

- **Mean WER on matches** : 0.3686.
- **Mean CER on matches** : 0.4942.
- **Mean Levenshtein on matches** : 0.9107.
---
- **Mean precision (word-weighted)** : 0.7927.
- **Mean recall (word-weighted)** : 0.8239.

- **Mean WER on matches (word-weighted)** : 0.4146.
- **Mean CER on matches (word-weighted)** : 0.6476.
- **Mean Levenshtein on matches (word-weighted)** : 0.9104.

## NER Precision/recall

- **Mean precision** : 0.8100.
- **Mean recall** : 0.8288.

- **Mean WER on matches** : 0.1294.
- **Mean CER on matches** : 0.1148.
- **Mean Levenshtein on matches** : 0.9439.
---
- **Mean precision (word weighted)** : 0.8524.
- **Mean recall (word weighted)** : 0.8733.

- **Mean WER on matches (word weighted)** : 0.1777.
- **Mean CER on matches (word weighted)** : 0.1837.
- **Mean Levenshtein on matches (word weighted)** : 0.9118.

### 10 Worst NER Precision scores:

05_ Thyeste_FDS2018_page_6.txt (mean NER precision: **0.8358**, mean CER on matches **2.753685323324181** :

|Prediction|Reference|
|---|---|
|Le sujet de Thyeste|THYESTE|
|Argos|Le sujet de Thyeste|
|Tantale|Argos|
|Atrée|Tantale|
|Thyeste|Atrée|
|Jupiter|Thyeste|
|Atrée|Jupiter|
|Thyeste|Atrée|
|Jupiter|Thyeste|
|Atrée|Jupiter|
|Thyeste|Thyeste|
|Mycènes|Atrée|
|Thyeste|Thyeste|
|Atrée|Mycènes|
|Sénèque|Atrée|
|Thomas Jolly|Sénèque|
|Sénèque|Thomas Jolly|
|Atreus|Sénèque|
|FESTIVAL –|Atreus|
|Théâtre de l’Archipel Scène|FESTIVAL –|
|Perpignan –|Théâtre de l'Archipel Scène|
|Comédie de Saint-Étienne|Perpignan –|
|Centre|Comédie de Saint-Étienne|
|–|Centre|
|Le Quai|–|
|Angers –|Le Quai|
|Le Grand T Théâtre de Loire-Atlantique|Angers –|
|Nantes|Le Grand T Théâtre de Loire-Atlantique|
|–|Nantes|
|Théâtre national de Strasbourg|–|
|Théâtre des Salins|Théâtre national de Strasbourg|
|Martigues –|Théâtre des Salins|
|Palais des Beaux-Arts|Martigues –|
|Charleroi|Palais des Beaux-Arts|
|Belgique|Charleroi|
|–|Belgique|
|La Coursive Scène nationale de La Rochelle – 12|–|
|Les Célestins|La Coursive Scène nationale de La Rochelle – 12|
|Théâtre de Lyon|Les Célestins|
|Théâtre de Caen|Théâtre de Lyon|
|–|Théâtre de Caen|
|Le Liberté|La Liberté|
|Scène nationale de|Scène nationale de|
|Toulon|Toulon|
|–|–|
|La Criée Théâtre national de Marseille|La Criée Théâtre national de Marseille|
|–|–|
|Théâtre Firmin Gémier La Piscine|Théâtre Firmin Gémier La Piscine|
|Châtenay-Malabry|Châtenay-Malabry|
|Théâtre du Nord|–|
|Lille|Théâtre du Nord|
|FESTIVAL-AVIGNON.COM FDA18 Feuille|Lille|
|English|FESTIVAL-AVIGNON.COM FDA18|
|La Grande Camisole 2014|English|
|Annik Wetter Licence Festival|La Grande Camisole|
|THYESTE|Annick Wetter Licences|


CommAvignon_fds_laPrincesseMaleine_FDA2017_page_4.txt (mean NER precision: **0.5152**, mean CER on matches **1.609931245225363** :

|Prediction|Reference|
|---|---|
|La Princesse Maleine|La Princesse Maleine|
|Maeterlinck|Maeterlinck|
|Marion Canelas|Maleine|
|Béguines|Béguines|
|Europe|Europe|
|Maleine|Maeterlinck|
|Maleine|Maleine|
|Maeterlinck|Maleine|
|C’est|Maeterlinck|
|Maleine|C'est|
|Maleine|Maleine|
|Anne|Anne|
|meurtrier|meurtrier|
|Hadewijch d’Anvers|–|
|–|Hadewijch d'Anvers|
|Maeterlinck|XIXe|
|XIXe|Marion Canelas|


CommAvignon_fds_lesIdiots_FDA2015_page_3.txt (mean NER precision: **0.7812**, mean CER on matches **1.2818387096774193** :

|Prediction|Reference|
|---|---|
|ENTRETIEN AVEC|ENTRETIEN AVEC|
|Les Idiots|d’une|
|d’une|Kirill Serebrennikov|
|Kirill Serebrennikov|Gogol Center|
|Gogol Center|– Rocco|
|Rocco|Luchino Visconti –|
|Luchino Visconti –|Rainer Werner Fassbinder|
|Rainer Werner Fassbinder|Moscou|
|Les Idiots|Moscou|
|Lars von Trier|Les Idiots|
|Moscou|Rocco|
|Moscou|Alexey Mizgirev|
|Les Idiots|Tous les autres s’appellent Ali|
|Rocco|Vlad Nastashev|
|Alexey Mizgirev|d’une|
|Tous les autres s’appellent Ali|Les Idiots|
|Vlad Nastashev|Dogme 95|
|d’une|J’ai|
|Dogme 95|Les Idiots|
|J’ai|Gogol Center|
|Gogol Center|c’est|
|c’est|Gogol Center|
|Gogol Center|d’eux-mêmes|
|d’eux-mêmes|Lars von Trier|
|Russie|Russie|


Bnf_fds_LeChevalierDOlmedoMiseEnScèneDeLluisPasqual_FDA1992_page_6.txt (mean NER precision: **0.8462**, mean CER on matches **0.8468748019186617** :

|Prediction|Reference|
|---|---|
|Lluís Pasqual|Reus|
|Reus|Espagne|
|Espagne|Fabia Puigserver|
|Fabia Puigserver|Théâtre Lliure de Barcelone|
|Théâtre Lliure de Barcelone|Centro Dramatico Nacional-Teatro Maria Guerrero de Madrid|
|Centro Dramatico Nacional-Teatro Maria Guerrero de Madrid|Espagne|
|Espagne|La vie du roi|
|La vie du roi|Marlowe|
|Marlowe|Brecht|
|Brecht|Festival d'Avignon|
|Festival d’Avignon|Lumières de Bohème de|
|Lumières de Bohème de|Une des dernières soirées de carnaval|
|Une des dernières soirées de carnaval|Goldoni|
|Goldoni|El publico de|
|El publico de|García Lorca|
|Garcia Lorca|Lluís Pasqual|
|Giorgio Strehler|Giorgio Strehler|
|Pièce|Pièce|
|Garcia Lorca|Garcia Lorca|
|Le Balcon de Genet|Le Balcon de Genet|
|Tirano Banderas|Tirano Banderas|
|Valle-Inclán|Valle-Inclán|
|France|France|
|Mozart|Mozart|
|Théâtre du Châtelet|Théâtre du Châtelet|
|Paris|Paris|
|Le Turc|Le Turc|
|Italie|Italie|
|Rossini|Rossini|
|Chevalier d’Olmedo|Chevalier d'Olmedo|
|Zéno Bianu|Zéno Bianu|
|Actes Sud-Papiers|Actes Sud-Papiers|
|Alternative théâtrale|Alternative théâtrale|


CommAvignon_fds_lePetitChaperonRouge_FDA2022_page_2.txt (mean NER precision: **0.9355**, mean CER on matches **0.8285700069108116** :

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
|Céleste Germe Collaboration|Céleste Germe Collaboration|
|Maëlys Ricordeau Musique J. Stambach|Maëlys Ricordeau Musique|
|James Brandily Lumière|James Brandily Lumière|
|Sébastien Lefèvre|Sébastien Lefèvre Images|
|Flavie Trichet-Lespagnol Son|Flavie Trichet-Lespagnol Son|
|Jérôme Tuncer Costumes|Jérôme Tuncer Costumes|
|Marion Stoufflet Assistant|Marion Stoufflet Assistant|
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
|Festival d’Avignon|Roche-sur-Yon|
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
|Kingersheim|CRÉA – Festival Momix - Scène|
|Théâtre National de Bretagne|Kingersheim|
|Rennes|Théâtre National de Bretagne|
|Le Grand Bleu|Rennes|
|Lille|Le Grand Bleu|
|Drac Île-de-France|Lille|
|Région Île-de-France|Drac Île-de-France|
|Théâtre Brétigny|Région Île-de-France|
|Fonds de production de la|Théâtre Brétigny|
|DGCA|Fonds de production de la|
|Département du Val-de-Marne Résidences Ferme|DGCA|
|Noisiel|Département du Val-de-Marne Résidences|
|Théâtre Jean-Vilar de Vitry-sur-Seine|Noisiel|
|Le Grand R Scène|Le Grand R Scène|
|Roche-sur-Yon Spectacle|Roche-sur-Yon Spectacle|
|Festival d’Avignon|Festival d'Avignon|


CommAvignon_fds_laPrincesseMaleine_FDA2017_page_6.txt (mean NER precision: **0.8000**, mean CER on matches **0.7672368421052631** :

|Prediction|Reference|
|---|---|
|Maurice Maeterlinck|PRINCESSE MALEINE|
|Grimm|Maurice Maeterlinck|
|XIXe|Grimm|
|La Princesse Maleine|XIXe|
|princesse Maleine|La Princesse Maleine|
|Hjalmar|princesse Maleine|
|Anne|Hjalmar|
|Pascal Kirsch|Anne|
|Princess Maleine|Pascal Kirsch|
|PRINCESSE MALEINE APRÈS|Princess Maleine|
|– Octobre 2018|– Octobre 2018|
|MC93 - Maison de la Culture de Seine-Saint-Denis –|MC93 - Maison de la Culture de Seine-Saint-Denis –|
|Le Parvis Scène|Le Parvis Scène|
|Ibos –|Ibos –|
|Châteauroux –|Châteauroux –|
|La Passerelle Scène|La Passerelle Scène|
|– Automne 2018|– Automne 2018|
|MC2|MC2|
|Grenoble 71e|Grenoble 71e|
|FESTIVAL-AVIGNON.COM FDA17|FESTIVAL-AVIGNON.COM FDA17|


Bnf_fds_LesAveugles FantasmagorieTechnologiqueConceptionEtR_FDA2002_page_3.txt (mean NER precision: **0.7273**, mean CER on matches **0.6987759925259924** :

|Prediction|Reference|
|---|---|
|Maurice Maeterlinck Menus|Maurice Maeterlinck Menus|
|– Le Théâtre|– Le Théâtre|
|Douze|Douze|
|Les Aveugles|Les Aveugles|
|Maurice Maeterlinck|Maurice Maeterlinck|
|Princesse Maleine|La Princesse Maleine|
|Pelléas et Mélisande|Pelléas et Mélisande|
|Intérieur|La Mort de Tintagiles|
|Mort de Tintagiles|Jarry|
|Jarry|Craig|
|Craig|Denis Marleau|
|Denis Marleau|Montréal|
|Montréal|Trois Derniers Jours|
|Trois Derniers Jours|Fernando Pessoa|
|Fernando Pessoa|Pessoa|
|Pessoa|Urfaust|
|Urfaust|Goethe|
|Goethe|Pessoa|
|Pessoa|Les Aveugles|
|Aveugles|Maeterlinck|
|Maeterlinck|Intérieur|
|Théâtre du Rideau|Théâtre du Rideau|
|Montréal|Montréal|
|UBU|UBU|


349953_667c39485f230-1_page_2.txt (mean NER precision: **0.9756**, mean CER on matches **0.6798746867167921** :

|Prediction|Reference|
|---|---|
|Absalon !|William Faulkner|
|William Faulkner|France Séverine Chavrier|
|France Séverine Chavrier|JUIN|
|JUIN|FABRICA 5H|
|FABRICA 5H|AVEC|
|AVEC|COMPRIS Création Festival d'Avignon 2024|
|COMPRIS Création Festival d’Avignon 2024|In French|
|In French|English|
|English|Les Palmiers sauvages|
|Les Palmiers sauvages|Séverine Chavrier|
|Séverine Chavrier|William Faulkner|
|William Faulkner|Absalon|
|Absalon|Absalon ! Œuvre-monde|
|Absalon ! Œuvre-monde|guerre de Sécession|
|guerre de Sécession|David|
|David|Absalon !|
|c’est|c’est|
|Thomas Sutpen|Thomas Sutpen|
|Mississippi|Mississipi|
|Séverine Chavrier|Séverine Chavrier|
|Faulkner|Faulkner|
|d’une|d’une|
|Hantés|Hantés|
|The Wild Palms|The Wild Palms|
|Séverine Chavrier|Séverine Chavrier|
|William Faulkner|William Faulkner|
|Absalom|Absalom|
|Absalom|Absalom|
|America of the Civil War|America of the Civil War|
|David|David|
|Absalom|Absalom|
|Absalom|Absalom|
|Thomas Sutpen|Thomas Sutpen|
|Mississippi|Mississippi|
|Greek|Greek|
|Faulkner|Faulkner|
|guerra de Secesión|guerra de Secesión|
|Faulkner|Faulkner|
|Spectacle|Spectacle|
|Festival d’Avignon|Festival d'Avignon|


349953_667c39485f230-1_page_4.txt (mean NER precision: **0.9200**, mean CER on matches **0.5882850241545894** :

|Prediction|Reference|
|---|---|
|Séverine Chavrier Qu’est|Séverine Chavrier Qu’est|
|Faulkner Absalon|Faulkner Absalon|
|Absalon !|Absalon !|
|Séverine Chavrier|Séverine Chavrier|
|J’aborde|J’aborde|
|d’une|d’une|
|d’une|d’une|
|Pouvez|Pouvez|
|c’est|Faulkner|
|d’une|c’est|
|l’univers de|d’une|
|l’histoire|l’univers de|
|m’appuie|l’histoire|
|Faulkner|m’appuie|
|Faulkner|Faulkner|
|Blancs|Faulkner|
|Faulkner|Blancs|
|États-Unis|Faulkner|
|Sud|États-Unis|
|Nord|Sud|
|L’enfance|Nord|
|Faulkner|L’enfance|
|Pouvez|Pouvez|


Bnf_fds_TheAlvinAileyCityCenterDanceTheater_FDA1974_page_6.txt (mean NER precision: **0.6471**, mean CER on matches **0.5828695418273909** :

|Prediction|Reference|
|---|---|
|The Lark Ascending Cry Rainbow' Round my Shoulder Entracte Revelations Entracte Programme|The Lark Ascending Cry Entracte Rainbow' Round my Shoulder Entracte Revelations Programme|
|Blues|Blues|
|Carmina Burana|A Song for you Revelations|
|A Song for you Revelations Entracte|Alvin Ailey City Center Dance Theater|
|Le Alvin Ailey City Center Dance Theater|Dance Theater Foundation Inc|
|Dance Theater Foundation Inc|Dance Theater Foundation|
|Le Dance Theater Foundation|New York State Council on the Arts|
|New York State Council on the Arts|National Endowment for the Arts|
|National Endowment for the Arts|Carmina Burana|
|Spirituals|Spirituals|
|Grace Costumes|Grace Costumes|


