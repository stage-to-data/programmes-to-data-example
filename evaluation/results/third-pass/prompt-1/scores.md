<!-- Third-pass run, scored against ground truth commit 0d40e2fc (151 pages,
     36,417 words, 249,500 characters) — an earlier state of the corpus than the
     final-tests runs. The two are not comparable. Corrected values for the
     Levenshtein-on-matches columns are in ../../../corrected-metrics.md
     Scatter plots omitted; regenerate them from scores.json. -->

# LLM Evaluation (Prompt 1)

"_third pass, prompt-1 (transcriptions not kept in this repository)_" (**151 files**) was tested against _evaluation/ground-truth/md_ (**151 files**). Found **0 missing files**.

Evaluation word count : 36417 (0-798), character count: 249500 (0-5438)

## Full file-level analyses

- **Mean Levenshtein ratio (raw)** : 0.9204.
- **Mean Levenshtein ratio (parsed)** : 0.9362.
- **Mean Levenshtein ratio (raw, weighted by word)** : 0.9739.
- **Mean Levenshtein ratio (parsed, weighted by word)** : 0.9833.

### 10 worst Levenshtein ratios:

- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_2.txt
- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_3.txt
- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_1.txt
- 0.0000 : Bnf_fds_LeCercleDeCraieCaucasienMiseEnScèneDeBennoBesson_FDA1978_page_4.txt
- 0.0113 : Bnf_fds_ChroniquesDuneFinDaprèsmidiMiseEnScèneDePierre _FDA1988_page_4.txt
- 0.3858 : Bnf_fds_BéréniceMiseEnScèneDeLambertWilson_FDA2001_page_1.txt
- 0.6262 : CommAvignon_fds_lesIdiots_FDA2015_page_1.txt
- 0.6738 : Bnf_fds_AvronEvrardMiseEnScèneDePhilippeAvronEtClaudeEvr_FDA1971_page_1.txt
- 0.7211 : CommAvignon_fds_dieEheDerMariaBraun_FDA2014_page_1.txt
- 0.7761 : CommAvignon_fds_laMaisonDeThe_FDA2019_page_1.txt


## Precision/recall

- **Mean precision** : 0.6950.
- **Mean recall** : 0.7789.

- **Mean WER on matches** : 0.3326.
- **Mean CER on matches** : 0.4243.
- **Mean Levenshtein on matches** : 0.8862.
---
- **Mean precision (word-weighted)** : 0.7835.
- **Mean recall (word-weighted)** : 0.8451.

- **Mean WER on matches (word-weighted)** : 0.3083.
- **Mean CER on matches (word-weighted)** : 0.3908.
- **Mean Levenshtein on matches (word-weighted)** : 0.8996.

## NER Precision/recall

- **Mean precision** : 0.8714.
- **Mean recall** : 0.8635.

- **Mean WER on matches** : 0.1026.
- **Mean CER on matches** : 0.0885.
- **Mean Levenshtein on matches** : 0.9501.
---
- **Mean precision (word weighted)** : 0.9393.
- **Mean recall (word weighted)** : 0.9053.

- **Mean WER on matches (word weighted)** : 0.1201.
- **Mean CER on matches (word weighted)** : 0.1106.
- **Mean Levenshtein on matches (word weighted)** : 0.9424.

### 10 Worst NER Precision scores:

349953_667c39485f230-1_page_2.txt (mean NER precision: **0.9000**, mean CER on matches **1.2961913290957405** :

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
|Absalon ! Œuvre-monde|Absalon !|
|David|Thomas Sutpen|
|Absalon|Mississipi|
|Thomas Sutpen|Séverine Chavrier|
|Mississipi|Faulkner|
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


CommAvignon_fds_dieEheDerMariaBraun_FDA2014_page_1.txt (mean NER precision: **0.6667**, mean CER on matches **1.25** :

|Prediction|Reference|
|---|---|
|JUIL|France|
|France|JUIL|


CommAvignon_fds_lesIdiots_FDA2015_page_2.txt (mean NER precision: **0.7593**, mean CER on matches **1.09684287626257** :

|Prediction|Reference|
|---|---|
|France|IDIOTS D'APRÈS LARS|
|IDIOTS D'APRÈS LARS|TRIER KIRILL SEREBRENNIKOV|
|TRIER KIRILL SEREBRENNIKOV|Madame Filipp Avdeev|
|Yulia Aug Madame Filipp Avdeev|La secrétaire au tribunal|
|La secrétaire au tribunal|La chef de la secrétaire|
|La chef de la secrétaire|Olga Woof|
|Olga Woof|La juge Oksana Fandera|
|La juge Oksana Fandera|Karina Sergey Galakhov|
|Karina Sergey Galakhov L'officier|Le serveur|
|Le serveur|L’agent|
|L'agent|Le policier|
|Le policier|Le frère de Masha|
|Le frère de Masha|Un homme|
|Un homme|Le gestionnaire|
|Le gestionnaire|Le mari de|
|Le mari de|L’acheteur|
|L'acheteur|Le chef de Sergey|
|Le chef de Sergey|Kachan|
|Kachan|Un homme|
|Un homme|Le père de Karina|
|Le père de Karina|Sergey Olga Naumenko|
|Sergey Olga Naumenko|La femme au foyer|
|La femme au foyer|La tante d’Elisey|
|La tante d'Elisey|La mère de Karina|
|La mère de Karina|Aleksandra Revenko|
|Aleksandra Revenko Katya|Mathieu Beaufort|
|Mathieu Beaufort|Laura Deleaz|
|Laura Deleaz|Amandine Huynh|
|Amandine Huynh|Nedjma Ortiz|
|Nedjma Ortiz|Clément Paimpara Mise|
|Clément Paimpara Mise|Kirill Serebrennikov|
|Kirill Serebrennikov|Kirill Serebrennikov|
|Kirill Serebrennikov|Gogol Center|
|Moscou|Moscou|
|Russie|de France|
|Russie|Russie|
|l'Onda Office national de diffusion artistique|Russie|
|EN+ Group Spectacle|Office national de diffusion artistique et de|
|Gogol Center|EN+ Group Spectacle|
|Moscou|Moscou|
|Russie|Russie|


Bnf_fds_LesAveugles FantasmagorieTechnologiqueConceptionEtR_FDA2002_page_2.txt (mean NER precision: **0.9667**, mean CER on matches **0.9593354090389319** :

|Prediction|Reference|
|---|---|
|France|France|
|Chapelle|Chapelle|
|lycée St Joseph|lycée St Joseph|
|Les Aveugles|Maurice Maeterlinck|
|Maurice Maeterlinck|Denis Marleau|
|Denis Marleau|Céline Bonnier|
|Céline Bonnier|Paul Savoie|
|Paul Savoie|Pierre Laniel|
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


CommAvignon_fds_enAtendant_FDA2023_page_5.txt (mean NER precision: **0.9310**, mean CER on matches **0.8932657526153461** :

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
|Rosàs|Rosas|
|Marc Blanchet|Marc Blanchet|
|En Attendant|En Atendant|
|Vertu|Vertu|
|Tant|Tant|
|Gouster|Gouster|
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


CommAvignon_fds_lePetitChaperonRouge_FDA2022_page_2.txt (mean NER precision: **0.9524**, mean CER on matches **0.8286361918656364** :

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


Bnf_fds_LeChevalierDOlmedoMiseEnScèneDeLluisPasqual_FDA1992_page_6.txt (mean NER precision: **0.9750**, mean CER on matches **0.7805619668811301** :

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
|Lumières de Bohème de|l'Odéon-Théâtre de l'Europe|
|l'Odéon-Théâtre de l'Europe|Une des dernières soirées de carnaval|
|Une des dernières soirées de carnaval|Goldoni|
|Goldoni|El publico de|
|El publico de|García Lorca|
|García Lorca|Lluís Pasqual|
|Giorgio Strehler|Giorgio Strehler|
|l'Odéon-Théâtre de l'Europe|l'Odéon-Théâtre de l'Europe|
|Pièce|Pièce|
|García Lorca|Garcia Lorca|
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


CommAvignon_fds_enAtendant_FDA2023_page_2.txt (mean NER precision: **0.8636**, mean CER on matches **0.7487912672123198** :

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


Bnf_fds_LaTragiqueHistoireDHamletPrinceDeDanemarkMiseEn _FDA1977_page_2.txt (mean NER precision: **0.7969**, mean CER on matches **0.7184707596044724** :

|Prediction|Reference|
|---|---|
|d'Hamlet|d'Hamlet|
|William Shakespeare Texte|William Shakespeare Texte|
|François Bérault Mise|François Bérault Mise|
|Benno Besson Assisté|Benno Besson Assisté|
|Jean-François Prévand|Jean-François Prévand|
|Daniel Edinger|Daniel Edinger|
|Dominique Serreau Scénographie|Dominique Serreau Scénographie|
|Ezzio Toffolutti Musique|Ezzio Toffolutti Musique|
|José Berghmans|José Berghmans|
|Francisco|Francisco|
|Jacques Roussillon Marcellus|Alain Frerot|
|Denis Benoliel Horatio|Jacques Roussillon Marcellus|
|d'Hamlet Dominique Serreau Gertrude|Denis Benoliel Horatio|
|Danemark|Jacques Boudet|
|Danemark|Dominique Serreau Gertrude|
|Dominique Serreau Hamlet|Danemark|
|François Lauzon Cornélius|Danemark|
|Jack Gatteau Polonius|Dominique Serreau Hamlet|
|Alain Frerot Laërte|François Lauzon Cornélius|
|Polonius Nicolas Serreau Ophélie|Jack Gatteau Polonius|
|Polonius Brigitte Roüan Reynaldo|Alain Frerot Laërte|
|Laërte|Nicolas Serreau Ophélie|
|François Lauzon Rosencrantz|Brigitte Roüan Reynaldo|
|d'Hamlet Daniel Edinger Premier|Laërte|
|Jacques Roussillon|François Lauzon Rosencrantz|
|François Lauzon|Emmanuel Pierson|
|Nicolas Serreau Fortinbras|Daniel Edinger Premier|
|François Lauzon|Jacques Roussillon|
|Le capitaine norvégien|François Lauzon|
|Jacques Boudet|Nicolas Serreau Fortinbras|
|Denis Benoliel|François Lauzon|
|Alain Frerot|Le capitaine norvégien|
|Alain Frerot|Denis Benoliel|
|Un paysan|Alain Frerot|
|Jacques Roussillon|Alain Frerot|
|Denis Benoliel Osric|Un paysan|
|Denis Benoliel Nobles|Jacques Roussillon|
|Daniel Edinger|Denis Benoliel Osric|
|Alain Frerot|Denis Benoliel Nobles|
|Emmanuel Pierson|Daniel Edinger|
|Jean-François Prévand|Jean-François Prévand|
|Nicolas Serreau|Nicolas Serreau|
|Aléna Sluneckova Régie|Aléna Sluneckova Régie|
|Jack Gatteau Coordination|Jack Gatteau Coordination|
|Michel Le Moal Son|Michel Le Moal Son|
|Jean-Marie Bourdat Habilleuse|Jean-Marie Bourdat Habillage|
|Nicole Aubry Maquillages|Nicole Aubry Maquillages|
|Suzanne Pisteur Costumes|Suzanne Pisteur Costumes|
|Jeanine Aguillella|Jeanine Aguilella|
|Joëlle Loucif|Joëlle Loucif|
|Claude Carliez|Claude Carliez|


Bnf_fds_LesAveugles FantasmagorieTechnologiqueConceptionEtR_FDA2002_page_3.txt (mean NER precision: **0.9200**, mean CER on matches **0.6281223607310564** :

|Prediction|Reference|
|---|---|
|Maurice Maeterlinck Menus|Maurice Maeterlinck Menus|
|– Le Théâtre|– Le Théâtre|
|Douze|Douze|
|Aveugles|Les Aveugles|
|Maurice Maeterlinck|Maurice Maeterlinck|
|Princesse Maleine|La Princesse Maleine|
|Pelléas et Mélisande|Pelléas et Mélisande|
|Intérieur|Jarry|
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


