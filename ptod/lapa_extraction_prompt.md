# LA-PA Extraction Prompt — From Markdown Programme to Structured Data

## System Prompt

You are an expert in performing arts documentation and the LA-PA (Linked Art Performing Arts) ontology. Your task is to extract structured data from the markdown transcription of a theatre programme and populate the fields for each of the 8 LA-PA models listed below.	

**Core rules:**

- Extract only information explicitly present in the document. Do not infer unless the field description explicitly permits it.  
- When a field is marked **Verbatim**, copy the exact string from the source, including original spelling, punctuation, and language.  
- When a field requires a controlled vocabulary (AAT, BNF roles), use only the allowed values. If you are not 80% confident, leave the field empty (`null`).  
- For **Role** fields, use the BNF role vocabulary: [https://data.bnf.fr/vocabulary/roles](https://data.bnf.fr/vocabulary/roles) — use only the French labels and definitions; ignore the Library of Congress equivalents.  
- For **ID** fields, follow the construction rule specified per model.  
- For **Reference to Textual Work** and **Reference to Digital Object**, use the ID of the programme document (Model 2\) when applicable.  
- Output a single JSON object with one key per model. Each model's value is a list of instances (even if there is only one).

---

## User Prompt

Below is the markdown transcription of a theatre programme. Extract all available data and return a JSON object structured according to the 8 LA-PA models below. If a field cannot be filled, use `null`. If a model has multiple instances (e.g. multiple productions), return a list.

**Programme (markdown):**

{MARKDOWN\_CONTENT}

---

## Output Schema

Return a JSON object with the following top-level keys:

{

  "overall\_event": \[...\],

  "programme": \[...\],

  "textual\_work": \[...\],

  "work": \[...\],

  "production": \[...\],

  "performance": \[...\],

  "audience": \[...\],

  "projected\_event\_tour": \[...\],

  "place": \[...\]

}

---

## Model Definitions

### MODEL 1 — Overall Event

*Represents the festival or overarching event edition that the programme documents (e.g., Festival d'Avignon 1988).*

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `type` | Fixed value: `"Overall Event"` |
| `title` | Display title of the festival edition. For Festival d'Avignon IN: `"Festival d'Avignon"`. |
| `id` | Unique identifier. Use `FDAin` (IN programme) or `FDAoff` (OFF) \+ `-` \+ year. E.g. `FDAin-1988`. If no explicit year: infer from edition number (1st \= 1947, annual thereafter); if unavailable, use `YYYY`. |
| `genre_category` | Genre or category of the event. Use AAT controlled vocabulary. |
| `date_beginning` | Earliest start date (year minimum). If no explicit date on IN programme: infer from edition number (1st edition \= 1947, annual). If unavailable: `YYYY`. |
| `date_end` | Latest end date. Same inference rules as `date_beginning`. |
| `place` | Location of the event. |
| `director_name` | Name of the artistic director of the festival. |
| `director_verbatim_role` | Verbatim role label as it appears in the source. |
| `team_name` | Name of a team member (person or group) involved in realising the event. Repeatable. |
| `team_group` | Group to which the team member belongs. |
| `team_role` | Role of the team member. Use BNF role vocabulary. |
| `team_verbatim_role` | Verbatim role label from source. |
| `sponsor_name` | Name of a sponsor. Repeatable. |
| `sponsor_role` | Role of the sponsor. Use AAT: `"Patrons"` for general supporters; `"sponsors"` for those assuming primary responsibility; `"friends"` for members of voluntary associations. Add new types if needed (e.g. for media sponsors). |
| `sponsor_verbatim_role` | Verbatim sponsor role from source (e.g. `"parraine"`, `"avec la participation de"`). |
| `reference_textual_work` | ID of a related Textual Work instance. |
| `reference_digital_object` | ID of a related Digital Object instance. |

---

### MODEL 2 — Programme (Textual Work / Document)

*Represents the programme document itself as a textual work.*

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `type` | Type of programme. Choose **only** from these three values: `"show programme"`, `"general programme"`, `"season programme"`. Use `"show programme"` for a programme dedicated to a single production or company. Use `"general programme"` for a programme covering all productions in an edition, for instance a festival. Use `"season programme"` for a season booklet. |
| `title` | Display title of the document. |
| `id` | Unique ID: `FDS` (show programme) or `PROG` (general/season) \+ `FDAin`/`FDAoff` \+ 4 first letters of production title (if known) \+ date \+ 4 random alphanumeric characters. E.g. `FDS-FDAin-HAML-1988-a3bZ`. |
| `part_of_programme` | ID of a parent programme, if this is a component. |
| `title_type` | Type of title. Choose **only** from the following AAT values: `titles (general, names)`, `abbreviated titles`, `alternative titles`, `brief titles`, `collection titles`, `collective titles`, `constructed titles`, `descriptive titles`, `exhibition titles (work titles)`, `former titles`, `full titles`, `generic titles`, `group titles`, `inscribed titles`, `original titles`, `popular titles`, `portfolio titles`, `published titles`, `repository titles`, `series titles`, `sub-group titles`, `subtitles (titles or names)`, `title statements`, `translated titles`, `uniform titles`, `volume titles`, `working titles`. Use `"titles (general, names)"` as the default when no other type applies more precisely. |
| `creator_name` | Name of the creator of the document. Repeatable. |
| `creator_role` | Role of the creator. Use BNF role vocabulary (publishing sector roles). |
| `creator_verbatim_role` | Verbatim role from source. |
| `date` | Year of the related event, unless an exact date is mentioned. |
| `text_content` | Verbatim transcription of the text portion as it appears in the programme. Extract the full text (e.g. the entire biography, the complete synopsis). Repeatable: one instance per distinct text portion. |
| `text_language` | Language of the text portion. |
| `text_topic` | Category of the text portion. Choose from: `Biographie`, `Interview`, `Citation`, `Extrait de presse`, `Synopsis`, `Éditorial`, `Présentation générale`, `Information complémentaire sur la production`, `Note d'intention`, `Texte littéraire`, `Traduction`, `Autre`. |
| `link_to_production` | ID of the production the text portion refers to, when multiple productions are present. |
| `text_source` | ID or reference to another document from which the text portion derives. |
| `image_part` | Reference to a visual item that is part of this textual work. |
| `language` | Overall language(s) of the document. List from most to least used if multilingual. |
| `publisher_name` | Publisher name. |
| `publisher_role` | Publisher role. Use BNF role vocabulary (publishing sector). |
| `publisher_verbatim_role` | Verbatim publisher role from source. |
| `reference_textual_work` | ID of a related Textual Work. |
| `reference_digital_object` | ID of a related Digital Object. |

---

### MODEL 3 — Textual Work (Play / Source Text)

*Represents a literary or dramatic work referenced by the programme (the play, libretto, adapted text, etc.).*

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `type` | Fixed value: `"Textual Work"` |
| `titles` | Array of title objects, one per distinct title form mentioned in the source. Each object has exactly two keys: `value` — The title string, copied verbatim from the source including original language, capitalisation, and diacritics. `title_type` — Type of the title. Choose from the AAT list below. Required rules: Use `"original titles"` for the title in the original language of composition. Use `"translated titles"` for any title that is a translation into another language. Use `"subtitles (titles or names)"` for a secondary title presented subordinately (e.g. in parentheses below the main title). Use `"titles (general, names)"` when the source provides only one title and its type cannot be determined more precisely. Multiple titles of the same type are allowed (e.g. two translated titles in different languages). **Order:** list the title that appears most prominently in the source first. **Minimum:** every instance must have at least one title object. **Example — single title:** `"titles": [{"value": "Hamlet", "title_type": "titles (general, names)"}]` **Example — original \+ French translation:** `"titles": [{"value": "A Zsenik Iskolája", "title_type": "original titles"}, {"value": "L'École des Génies", "title_type": "translated titles"}]` **Example — French title \+ Occitan subtitle:** `"titles": [{"value": "La Madone des ordures", "title_type": "titles (general, names)"}, {"value": "Nòstra Dòna dei bordilhas", "title_type": "subtitles (titles or names)"}]` **Example — main title \+ subtitle on separate line:** `"titles": [{"value": "Les Aveugles", "title_type": "titles (general, names)"}, {"value": "fantasmagorie technologique", "title_type": "subtitles (titles or names)"}]` |
| `id` | Unique ID: `Play` \+ 4 letters of title \+ 4 letters of first creator name \+ 4 random alphanumeric chars. E.g. `Play-HAML-SHAK-456g`. |
| `creator_name` | Name of the author or creator. Repeatable.**Translation rule.** When a Textual Work instance represents a translation (i.e. `title_type` \= `"translated titles"`), always include **both** the translator and the original author as creator objects in the `creator_name` / `creator_role` arrays: translator: `creator_role` \= `["Traducteur"]`, `creator_verbatim_role` \= verbatim label from source (e.g. `"Traduction"`) original author: `creator_role` \= `["Auteur"]`, `creator_verbatim_role` \= null (inferred, not stated for this instance) The original Textual Work (Model 3, instance with `"original titles"`) keeps only the original author. Cross-reference both instances via `reference_textual_work`. Example — Bonnefoy's translation of Hamlet: creators: \[   {"name": "Yves Bonnefoy", "role": \["Traducteur"\], "verbatim\_role": "Traduction"},   {"name": "Shakespeare",   "role": \["Auteur"\],      "verbatim\_role": null} \] |
| `creator_role` | Role of the creator. Use BNF role vocabulary. |
| `creator_verbatim_role` | Verbatim role from source. |
| `date` | Date of creation or publication as mentioned in source. |
| `publisher_name` | Publisher name, if mentioned. |
| `publisher_role` | Publisher role. Use BNF role vocabulary. |
| `publisher_verbatim_role` | Verbatim publisher role from source. |
| `reference_textual_work` | ID of a related Textual Work. |
| `reference_digital_object` | ID of a related Digital Object. |

---

### MODEL 4 — Work

*Represents the abstract artistic staging project (the Work in the LA-PA sense: e.g., Chéreau's Hamlet staging as a conceptual unit, independent of individual productions).*

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `type` | Fixed value: `"Work"` |
| `titles` | Array of title objects, one per distinct title form mentioned in the source. Each object has exactly two keys: `value` — The title string, copied verbatim from the source including original language, capitalisation, and diacritics. `title_type` — Type of the title. Choose from the AAT list below. Required rules: Use `"original titles"` for the title in the original language of composition. Use `"translated titles"` for any title that is a translation into another language. Use `"subtitles (titles or names)"` for a secondary title presented subordinately (e.g. in parentheses below the main title). Use `"titles (general, names)"` when the source provides only one title and its type cannot be determined more precisely. Multiple titles of the same type are allowed (e.g. two translated titles in different languages). **Order:** list the title that appears most prominently in the source first. **Minimum:** every instance must have at least one title object. **Example — single title:** `"titles": [{"value": "Hamlet", "title_type": "titles (general, names)"}]` **Example — original \+ French translation:** `"titles": [{"value": "A Zsenik Iskolája", "title_type": "original titles"}, {"value": "L'École des Génies", "title_type": "translated titles"}]` **Example — French title \+ Occitan subtitle:** `"titles": [{"value": "La Madone des ordures", "title_type": "titles (general, names)"}, {"value": "Nòstra Dòna dei bordilhas", "title_type": "subtitles (titles or names)"}]` **Example — main title \+ subtitle on separate line:** `"titles": [{"value": "Les Aveugles", "title_type": "titles (general, names)"}, {"value": "fantasmagorie technologique", "title_type": "subtitles (titles or names)"}]` |
| `identifier` | Unique ID: `W` \+ 4 letters of title \+ 4 letters of creator/company name (use `nnnn` if absent) \+ `date_end` (yyyy) \+ 4 random alphanumeric chars. E.g. `W-HAML-CHER-1988-x7kL`. |
| `company_name` | Producing company involved in creating the work. |
| `company_role` | Role of the company. Use BNF role vocabulary. |
| `creator_name` | Name of the creator (director, choreographer, etc.). Repeatable. |
| `creator_role` | Role of the creator. Use BNF role vocabulary. |
| `creator_verbatim_role` | Verbatim role from source. |
| `date_beginning` | Earliest date of creation (typically first rehearsal or creation period start). |
| `date_end` | Latest date of creation; usually the premiere date. |
| `date_verbatim` | Verbatim date string as it appears in source or historical documents. |
| `play_used` | ID of the Textual Work (Model 3\) that is the source text. Only if explicitly mentioned in the programme. |
| `adapted_from_inspired_by` | ID of the Textual Work used as adaptation base, if different from `play_used`. |
| `part_of` | ID of a greater Work of which this work forms a part. |
| `reference_textual_work` | ID of a related Textual Work. |

---

### MODEL 5 — Production

*Represents a specific production event: one staged realisation of a Work at a given time and place, with its full team, performers, and financing.*  
***Mandatory object structure** — `performers`, `team`, and `musicians` fields must each be returned as a JSON array of objects with **exactly the keys** mentioned. No key may be omitted. Example: `{"name": "Judith Jamison", "verbatim_role": "Avec", "role": null, "character": null, "group": "The Alvin Ailey City Center Dance Theater"}`.*  
**`character` — Name of the dramatic character(s) played by this performer. When a single performer is credited with more than one character (double or triple casting), list all character names as a single string separated by `/` (e.g. `"Le Spectre / Le premier Comédien / Le deuxième Fossoyeur"`). If no character is assigned, set to null.**

**Reprise rule — two Production instances.** When a programme documents a revival of an existing work AND provides sufficient data to distinguish the original production from the current one, create **two separate Production instances** both linked to the same Work (Model 4):

- **Production 1 — original creation** (`date_verbatim` contains "créé en…", "created in…", or equivalent). Populate with:  
* `date_beginning` / `date_end`: original creation dates  
* `performers`: the original cast, extracted from the "Créé en \[year\] avec…" line or equivalent  
* `producing_companies`: coproducers explicitly labelled with the creation year (e.g. "Coproduction : 2010")  
* `production_venue`: original venue if mentioned  
* Leave fields blank (`null`) that cannot be determined from the source for the original production  
- **Production 2 — current revival** (the production actually documented by this programme). Populate with:  
* `date_beginning` / `date_end`: current run dates  
* `performers`: current cast (from "Avec :" or equivalent)  
* `team`: full current team as listed  
* `producing_companies`: producers of the current run only (those not labelled with a past year)  
* `funders`, `sponsors`: current run only  
- **Trigger conditions** — apply this rule when the programme contains **at least two** of the following:  
1. An explicit original creation date distinct from the current run dates  
2. A named original cast distinct from the current cast (e.g. "Créé en 2010 avec…")  
3. Coproducers explicitly associated with the original creation year

If only one of these signals is present (e.g. a creation date but no original cast list), create a single Production and note the creation date in `date_verbatim`.

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `type` | Fixed value: `"Production"` |
| `titles` | Array of title objects, one per distinct title form mentioned in the source. Each object has exactly two keys: `value` — The title string, copied verbatim from the source including original language, capitalisation, and diacritics. `title_type` — Type of the title. Choose from the AAT list below. Required rules: Use `"original titles"` for the title in the original language of composition. Use `"translated titles"` for any title that is a translation into another language. Use `"subtitles (titles or names)"` for a secondary title presented subordinately (e.g. in parentheses below the main title). Use `"titles (general, names)"` when the source provides only one title and its type cannot be determined more precisely. Multiple titles of the same type are allowed (e.g. two translated titles in different languages). **Order:** list the title that appears most prominently in the source first. **Minimum:** every instance must have at least one title object. **Example — single title:** `"titles": [{"value": "Hamlet", "title_type": "titles (general, names)"}]` **Example — original \+ French translation:** `"titles": [{"value": "A Zsenik Iskolája", "title_type": "original titles"}, {"value": "L'École des Génies", "title_type": "translated titles"}]` **Example — French title \+ Occitan subtitle:** `"titles": [{"value": "La Madone des ordures", "title_type": "titles (general, names)"}, {"value": "Nòstra Dòna dei bordilhas", "title_type": "subtitles (titles or names)"}]` **Example — main title \+ subtitle on separate line:** `"titles": [{"value": "Les Aveugles", "title_type": "titles (general, names)"}, {"value": "fantasmagorie technologique", "title_type": "subtitles (titles or names)"}]` |
| `production_identifier` | Unique ID: `P` \+ 4 letters of title \+ 4 letters of first team member \+ year of `date_beginning` (yyyy) \+ 4 random alphanumeric chars. E.g. `P-HAML-CHER-1988-j2mN`. |
| `work_produced` | ID of the Work (Model 4\) that this production realises. |
| `genre_verbatim` | Genre label as it appears verbatim in the source. Extract only terms that designate a performing arts genre or form (e.g. "théâtre", "danse", "opéra", "marionnettes", "cirque", "performance"). Do **not** extract production status indicators such as "création", "création en France", "reprise", "première mondiale" — these belong exclusively to `premiere_verbatim` in Model 6\. If no genre label is present in the source, set to null. |
| `predicted_genre` | Genre inferred by the model when `genre_verbatim` is null or insufficient. If the genre cannot be determined with ≥ 80 % confidence from the source content (cast composition, textual references, company description), set to null. Never use production status terms ("création", "reprise") as genre values. |
| `language` | Language of the production as stated in the source. |
| `language_predicted` | Language as inferred by the model. Leave `null` if same as `language`. |
| `part_of_production` | ID of the Overall Event or larger production of which this production forms a part. |
| `order_in_production` | `order_in_production` captures the position of a production within a **single evening**. Set it only when two or more productions are performed on the same night (composite programme, back-to-back works). Use the format "n/total", e.g. "1/3". If the order is explicitly stated in the source, use that; otherwise infer from reading order. Set to null when: (a) the programme documents a single production, or (b) multiple productions are documented but performed on **alternating dates** (not the same evening) — alternation is not co-scheduling. |
| `scheduled_with` | ID of another production scheduled simultaneously. |
| `date_beginning` | Earliest date of the production. |
| `date_end` | Latest date of the production. |
| `duration` | Duration in minutes, if mentioned. |
| `production_venue` | Venue where the production takes place. |
| `performers` | List of performer objects. Each object: `{name, group, role, verbatim_role, character}`. Use BNF role vocabulary for `role`.  When the source places character names under a dramaturgical heading (e.g. "Anciens condisciples d'Hamlet :", "Membres de la garde du roi :", "Conseillers et ambassadeurs danois :"), the heading qualifies the character within the fictional world and must be prepended to each character name in `character`, separated by " : ", not stored in `verbatim_role`. `verbatim_role` is reserved for production-side functional labels ("Avec :", "Distribution :", "et"). |
| `animals` | List of animal objects. Each object: `{name, species, verbatim_species, character}`. |
| `musicians` | List of musician objects for **instrumentalists or vocalists who do not play a dramatic character**. Each object: {name, group, instrument\_vocal\_range, verbatim\_role, character}. Use this field only when the source explicitly credits a person as a musician (pit orchestra, live band, accompanist). When a section labelled "Les musiciens" (or equivalent) lists people who also have character names, treat them as **performers**, not musicians: place them in the `performers` array with verbatim\_role \= the section label (e.g. "Les musiciens") and character \= their character name(s). The `musicians` array remains empty in that case. |
| `team` | List of team member objects. Each object: `{name, group, role, verbatim_role}`. Use BNF role vocabulary for `role`.**Flat list.** The `team` array must be a single flat list — do not group entries into sub-arrays or annotate them with category labels (e.g. do not create separate blocks for "assistants", "régie", "ateliers"). Every credited agent, regardless of their function, appears as a peer object in the same array. **Commercial entities.** When a supplier, workshop, or company is credited by name for work contributing to the production (e.g. "Ateliers Gérard Audier", "Chaussures : Pompei", "Armures : Quadra"), include them as team objects with `name` \= the entity name, `verbatim_role` \= the role label as it appears, and `role` \= `[]` unless a BNF match is reached. This applies even when no individual person's name is given. The test is the same as for persons: would this entity's name appear in the programme if the production were performed without a printed programme? If yes, include in `team`.**Inherited role context for assistants.** When a credit beginning with "Assisté de", "Assistant à", "Assistant au(x)", or any equivalent assistant marker appears immediately after another role credit in the source, the assistant's `verbatim_role` must preserve the parent role context, not just the assistant marker. Concatenate the parent role label and the assistant marker exactly as they appear in the source, joined by the separator used in the source (typically ". " or " — "), and copy the result verbatim. The parent role is the most recent non-assistant credit appearing before the assistant credit, within the same logical block (no intervening blank line, section heading, or unrelated credit). Examples: Source: `Combat réglé par : Raoul Billerey` / `Assisté de : Alain Saugout` → Billerey : `verbatim_role: "Combat réglé par"` → Saugout : `verbatim_role: "Combat réglé par. Assisté de"` Source: `Chef machiniste : Gérard Rocher` / `Assisté de : Bernard Steffenino` → Rocher : `verbatim_role: "Chef machiniste"` → Steffenino : `verbatim_role: "Chef machiniste. Assisté de"` When the assistant marker is itself the explicit role label (e.g. "Assistants à la mise en scène : X, Y, Z"), no inheritance applies — copy the label as-is. The corresponding BNF role mapping in `role` should always be `["Assistant"]` (or its specialised variant if available, e.g. `["Assistant à la mise en scène"]`), regardless of the parent role. The `verbatim_role` carries the contextual link to the assisted person; the `role` array carries the controlled function. |
| `sponsors` | List of sponsor objects. Each object: `{name, role, verbatim_role}`. Trigger words: `"avec la participation de"`, `"avec le soutien de"`. Role: AAT `"Patrons"`. |
| `funders` | List of funder objects. Each object: `{name, role, verbatim_role}`. For financial contributors other than producers (e.g. `"résidences"`, `"remerciements"`). |
| `producing_companies` | List of producing company objects. Each object: `{name, role, verbatim_role}`. Trigger words: `"Producteur"`, `"Coproducteur"`. |
| `audience` | ID of an Audience instance (Model 6), if applicable. |
| `reference_textual_work` | ID of a related Textual Work. |
| `reference_digital_object` | ID of a related Digital Object. |

---

### MODEL 6 — Performance (Individual Showing)

*Represents a single showing/representation of a production on a specific date and at a specific place. A Performance is part of a Production (and, by extension, of an Overall Event). Each scheduled **time slot** generates one Performance instance. If a programme lists multiple times on the same date (e.g. "13h, 14h, 15h, 15h30"), each time slot is a distinct performance and receives its own instance and ID. If a date is listed without any time, it generates a single instance for that date.*  
**`character` — Name of the dramatic character(s) played by this performer. When a single performer is credited with more than one character (double or triple casting), list all character names as a single string separated by `/` (e.g. `"Le Spectre / Le premier Comédien / Le deuxième Fossoyeur"`). If no character is assigned, set to null.**

**Performances — two sets of instances.** Apply the same split to Model 6 :

- **Performances linked to Production 1 (original creation).** Generate one instance per known date/time slot of the original run. In most cases the programme only provides a single explicit date (the creation date, e.g. "Spectacle créé le 9 juillet 2010"). If no full schedule is available for the original run, generate exactly **one Performance instance** for that date, with:  
* `date_beginning`: the creation date (ISO format)  
* `premiere_type`: "world premiere" (or the appropriate premiere type if stated)  
* `premiere_verbatim`: verbatim label from source (e.g. "Création Festival d'Avignon 2010")  
* `part_of_event`: For the original-creation Performance instance, populate `part_of_event` with the inferred Overall Event ID (e.g. `FDAin-2010`) even if no Model 1 instance for that edition exists in the current extraction. This creates a dangling reference that will be resolved when the corresponding programme is processed. Do **not** create a Model 1 instance for an edition that is not the primary subject of the current programme.  
* `performance_venue`: original venue if stated

Do **not** invent additional performance dates for the original run that are not mentioned in the source.

- **Performances linked to Production 2 (current revival).** Generate one instance per scheduled date/time slot as usual, each with:  
* `part_of_event`: \[Overall Event ID of current edition, Production 2 ID\]  
* `premiere_verbatim`: null (a revival is not a premiere)

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `type` | Fixed value: `"Performance"` |
| `title` | Title of the performance (typically the title of the production). |
| `title_type` | Type of title. Choose **only** from the following AAT values: `titles (general, names)`, `abbreviated titles`, `alternative titles`, `brief titles`, `collection titles`, `collective titles`, `constructed titles`, `descriptive titles`, `exhibition titles (work titles)`, `former titles`, `full titles`, `generic titles`, `group titles`, `inscribed titles`, `original titles`, `popular titles`, `portfolio titles`, `published titles`, `repository titles`, `series titles`, `sub-group titles`, `subtitles (titles or names)`, `title statements`, `translated titles`, `uniform titles`, `volume titles`, `working titles`. Use `"titles (general, names)"` as the default when no other type applies more precisely. |
| `id` | Unique ID: `PE-` \+ 4 letters of production title \+ year \+ 4 random alphanumeric chars. E.g. `PE-HAML-1988-a1b2`. Each performance instance — defined as a unique date/time combination — gets a distinct ID. When multiple time slots exist on the same date, append the time in HHMM format: e.g. `PE-AVEU-2002-a001-1300`, `PE-AVEU-2002-a001-1400` |
| `premiere_type` | Type of premiere, if mentioned (e.g. `"world premiere"`, `"French premiere"`). |
| `premiere_verbatim` | Verbatim premiere label from source. |
| `part_of_event` | **Array** of IDs linking this performance to all containing entities, from broadest to narrowest: Overall Event ID first, then parent Production IDs in hierarchical order (see composite programme rule below). E.g. `["FDAin-2011", "P-SUJE-nnnn-2011-greg", "P-PROG-nnnn-2011-grea", "P-TREN-DAVI-2011-grea"]`. |
| `date_beginning` | Date **and time** of the performance, ISO format: `YYYY-MM-DD HH:MM`. When a time is listed in the programme, it is mandatory. When no time is given, use `YYYY-MM-DD` only. |
| `date_end` | End date of the performance, if distinct from `date_beginning`. |
| `performance_venue` | Venue of the performance (verbatim or ID of Place instance). |
| `digital_reference` | URL or ID of a digital document referencing this performance. |
| `audience` | ID of an Audience instance (Model 7), if applicable. |
| `performers` | List of performer objects specific to this performance, if different from the production's general cast. Each object: `{name, role, verbatim_role, character}`. |
| `reference_textual_work` | ID of a related Textual Work. |

---

### MODEL 7 — Audience

*Represents the audience of a production or event, including any quantitative dimension (capacity, attendance).*

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `audience_name` | String value of the audience name or designation (e.g. `"Public"`, `"Scolaires"`). |
| `audience_name_type` | Type of the audience name. |
| `audience_id` | Unique identifier for this audience instance. |
| `part_of_event` | ID of the Performance, Production, or Overall Event to which this audience belongs. |
| `dimension_value` | Numerical value of a dimension (e.g. attendance figure, capacity). |
| `dimension_unit` | Unit of the dimension (e.g. `"persons"`). |
| `dimension_type` | Type of dimension (e.g. `"capacity"`, `"attendance"`). |
| `reference_textual_work` | ID of a related Textual Work. |
| `reference_digital_object` | ID of a related Digital Object. |

---

### MODEL 8 — Performance (Projected / Tour Dates)

*Represents an individual performance date or a tour, linked to a production.*

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `title` | Title of the performance or tour. |
| `part_of_production` | ID of the Production (Model 5\) to which this performance belongs. |
| `date_beginning` | Earliest date of the performance or first date of the tour. |
| `date_end` | Latest date of the performance or last date of the tour. |
| `date_verbatim` | Verbatim date string as it appears in the programme. |
| `place_verbatim` | Verbatim place name as it appears in the programme. |

---

### MODEL 9 — Place

*Represents a named place or venue mentioned in the programme.*

| Field | Instructions |
| :---- | :---- |
| `source` | Filename or identifier of the source document. |
| `type` | Fixed value: `"Place"` |
| `id` | Unique ID: `PL` \+ 4 letters of place name \+ 4 random alphanumeric chars. E.g. `PL-COUR-123p`. |
| `place_name` | Name of the place as it appears in the source. |
| `place_type` | Type of the place (e.g. `"théâtre"`, `"cour"`, `"gymnase"`). |
| `reference_textual_work` | ID of a related Textual Work. |
| `reference_digital_object` | ID of a related Digital Object. |

---

## Additional Extraction Rules

1. **Multiple instances**: If the programme contains several productions, create one instance of Models 4, 5, and 6 per production.  
     
2. **Composite programme — hierarchical `part_of` rule**: When a programme documents an evening composed of multiple individual works (e.g. *Sujets à Vif – Programme A* containing *TRENTE-TROIS TOURS* and *VOYAGE COLA*), apply the following at both Work and Production levels:  
     
   - Create one **parent Work/Production** for the overarching event (e.g. `W-SUJE`, `P-SUJE`).  
   - If there is an intermediate grouping (e.g. Programme A / Programme B), create one **intermediate Work/Production** per group, with `part_of` → parent ID.  
   - Create one **leaf Work/Production** per individual spectacle, with `part_of` listing all ancestor IDs (parent \+ intermediate if applicable).  
   - At the **Performance** level, `part_of_event` must list **all hierarchy levels**: `[Overall Event ID, parent Production ID, intermediate Production ID (if any), leaf Production ID]`.  
   - Example (*Sujets à Vif*, FDA 2011):  
     - Works: `W-SUJE` (parent) → `W-PROG-A` (`part_of`: `W-SUJE`) → `W-TREN` (`part_of`: `["W-SUJE", "W-PROG-A"]`)  
     - Productions: `P-SUJE` → `P-PROG-A` (`part_of`: `P-SUJE`) → `P-TREN` (`part_of`: `["P-SUJE", "P-PROG-A"]`)  
     - Performance of TRENTE-TROIS TOURS on 2011-07-08: `part_of_event: ["FDAin-2011", "P-SUJE-...", "P-PROG-A-...", "P-TREN-..."]`

   

3. **Verbatim copy**: Never normalise or translate verbatim fields. Copy the exact string including capitalisation and diacritics.  
     
4. **Null vs. absent**: Use `null` for fields not found in the source. Do not guess.  
     
5. **Roles**: When a role label is present but does not match the BNF controlled vocabulary with ≥80% confidence, set the `role` field to `null` and preserve the string in the `verbatim_role` field.

	**Multiple roles for a single agent:** When a single person or entity is credited with more than one distinct role — either in a compound verbatim string (e.g., `"livret d'après Mérimée ; chorégraphie"`) or across separate lines in the source — apply the following rules:

1. **`role` field is always an array.** Even when only one role is assigned, return it as a one-element array: `["Chorégraphe"]`. This applies to all `role` fields in `team`, `performers`, `musicians`, `producing_companies`, and all Model 2–4 `creator_role` fields.  
2. **`verbatim_role` remains a single verbatim string.** Copy the full label exactly as it appears in the source, including conjunctions, separators, and prepositional phrases. Do not split or normalise: `"livret d'après Prosper Mérimée ; chorégraphie"` stays as one string. When the programme uses a **section heading** to introduce a group of performers (e.g. "La famille :", "Les musiciens :", "Avec :", "Distribution :"), that heading is the verbatim\_role for every performer listed under it. Copy the heading label exactly, without the colon. If a performer appears under no heading, set verbatim\_role to null.  
3. **Splitting compound verbatim strings into BNF roles.** When a verbatim string contains multiple role indicators separated by `;`, `,`, `et`, `/`, or a line break, map each segment independently to a BNF role and include all matches that meet the confidence threshold in the `role` array. Segments that fall below the threshold are omitted from `role` but are preserved in `verbatim_role`.  
   1. Example: `"livret d'après Mérimée ; chorégraphie"` → `"role": ["Librettiste", "Chorégraphe"]`  
   2. Example: `"conception, costumes, éléments scéniques"` at 80% threshold → `"role": []` (no BNF match reaches threshold; `verbatim_role` is preserved)  
4. **Do not duplicate objects.** A single person credited with multiple roles generates one object with a multi-value `role` array, not one object per role. The only exception is when the same person appears in two structurally distinct positions in the same production (e.g., simultaneously listed under `performers` and `team`): in that case, create one object per position.  
5. **Empty array vs. null.** When a `role` field is present in the source but no BNF match meets the threshold, return `"role": []`, not `null`. Reserve `null` for cases where no role label at all is present in the source.  
6. **Same agent, multiple source contexts.** When the same person or entity is credited under several distinct labels appearing on separate lines or in separate sections of the source (e.g. "Son : X" then later "Régie son : X"), still generate ONE object. Concatenate the verbatim labels with " ; " in `verbatim_role`, and include all corresponding BNF roles in the `role` array. Example — Cachia credited as both sound designer and sound régisseur: `{name: "Philippe Cachia", role: ["Concepteur son", "Régisseur son"], verbatim_role: "Son ; Régie son"}`  
     
6. **AAT titles**: Choose from the following values for `title_type`: `titles (general, names)`, `abbreviated titles`, `alternative titles`, `brief titles`, `collection titles`, `collective titles`, `constructed titles`, `descriptive titles`, `exhibition titles`, `former titles`, `full titles`, `generic titles`, `group titles`, `inscribed titles`, `original titles`, `popular titles`, `portfolio titles`, `published titles`, `repository titles`, `series titles`, `sub-group titles`, `subtitles`, `title statements`, `translated titles`, `uniform titles`, `volume titles`, `working titles`.  
     
7. **Repeatable fields**: Fields marked as "Repeatable" in these instructions must be returned as JSON arrays, even if there is only one value.  
     
8. **Cross-references**: Populate `reference_textual_work` and `reference_digital_object` with the `id` values you assign in Model 2 and Model 3 respectively.  
9. **Strict separation between document credits and production credits**  
   Persons and entities mentioned in the **programme's production credits** (printing, layout, graphic design, cover photography, typesetting) are contributors to the **document itself** (Model 2 only). They must never be placed in the `team`, `performers`, `musicians`, or `producing_companies` fields of Model 5\.  
   Typical indicators of document-level credits: `"IMPRIMERIE"`, `"MAQUETTE"`, `"GRAPHISME"`, `"MISE EN PAGE"`, `"CONCEPTION GRAPHIQUE"`, `"PHOTO DE COUVERTURE"`, `"PRINTING"`, `"LAYOUT"`, `"GRAPHIC DESIGN"`, `"COVER PHOTO"`. These strings typically appear at the bottom of the last page, often in uppercase.  
   In Model 2, distribute these contributors as follows:  
* printer → `publisher_name` / `publisher_verbatim_role`  
* layout artist, graphic designer → `creator_name` / `creator_verbatim_role`  
  When in doubt, apply this test: **would this person's name appear in a theatre programme if the production were performed without a printed programme?** If no, they belong to Model 2 only.  
10. **Verbatim role from source.** Copy only the role label as it appears in the source, excluding the person's name. Example: if the source reads `"chorégraphie : Jacques Garnier"`, the value is `"chorégraphie"`, not `"chorégraphie : Jacques Garnier"`. The name is captured separately in `creator_name`. Apply the same rule to `team_verbatim_role` and `verbatim_role` in all object arrays (`performers`, `team`, `musicians`).

