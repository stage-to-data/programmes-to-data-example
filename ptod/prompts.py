transcription_prompt = """
This image corresponds to a page in a theater program.
You will perform a complete and detailed OCR analysis of this image. 
DO NOT generate or use any code, do not use Tesseract or pytesseract — only use your internal vision to read the image.
Extract all visible text WITHOUT changing it.
DO NOT summarize, paraphrase, or infer missing text. DO NOT invent people's names.
Retain all spacing, punctuation, and formatting exactly as in the image.

You MUST follow the following rules when dealing with these specific cases:
- All titles are indicated with a preceding # with no hierarchy (example: # Title content). If the title contains line breaks, recompose the title into one single line.
- Exponents are given as lower case roman characters (example: XVe)
- Footnotes are given as special characters (example: word¹)
- When you detect the number of a page, return it at the start of the text using the word "PAGE"' followed by the number (example: PAGE 13)
- Do not describe images or logos, simply extract any text within them.
- Do not insert special characters for things like columns and page separation
- For distribution: if you detect a table-like stucture, typography variation that could be interpreted as a function/name or name/function pairing, or a string of points linking a function and name, apply the following structure:
Element 1 : Associated element 1, Associated element 2
Element 2 and Element 3, description : Associated element 3 and Associated element 4
(Note that in the case of enumeration, there are NO line breaks, there are commas)
- If you detect any other function/name or name/function pairs that are separated by a character like | or /, chnage the character to a : (example: element 1 : associated element 1)
- If you detect a completely empty page, or if the page is much too faint or blurry to confidently transcribe, simply return: [UNABLE TO TRANSCRIBE]
- Some pages may include texts of different languages, or old languages (for example old French). It is very important to NOT CHANGE the content, simply trnscribe the letters you see.

Check the overall readability of your transcription and make sure it reflects the structure of the original document.
The output should be ONLY the trancribed content (DO NOT add comments like "this is a theatre program" or "I was unable to reliably transcribe this").
"""

data_extraction_system_prompt = """
You are an expert in performing arts documentation and the LA-PA (Linked Art Performing Arts) ontology. Your task is to extract structured data from the markdown transcription of a theatre programme and populate the fields for each of the 8 LA-PA models listed below.

Core rules:

Extract only information explicitly present in the document. Do not infer unless the field description explicitly permits it.
When a field is marked Verbatim, copy the exact string from the source, including original spelling, punctuation, and language.
When a field requires a controlled vocabulary (AAT, BNF roles), use only the allowed values. If you are not 95% confident, leave the field empty (null).
For Role fields, use the BNF role vocabulary: https://data.bnf.fr/vocabulary/roles — use only the French labels and definitions; ignore the Library of Congress equivalents.
For ID fields, follow the construction rule specified per model.
For Reference to Textual Work and Reference to Digital Object, use the ID of the programme document (Model 2) when applicable.
Output a single JSON object with one key per model. Each model's value is a list of instances (even if there is only one).
"""

data_extraction_prompt = """
Below is the markdown transcription of a theatre programme. Extract all available data and return a JSON object structured according to the 8 LA-PA models below. If a field cannot be filled, use null. If a model has multiple instances (e.g. multiple productions), return a list.

Programme (markdown):

{&&MARKDOWN_CONTENT}

---

## Output Schema
Return a JSON object with the following top-level keys:

{
  "overall_event": [...],
  "programme": [...],
  "textual_work": [...],
  "work": [...],
  "production": [...],
  "performance": [...],
  "audience": [...],
  "projected_event_tour": [...],
  "place": [...]
}

---

## Model Definitions

### MODEL 1 — Overall Event

Represents the festival or overarching event edition that the programme documents (e.g., Festival d'Avignon 1988).

|Field| Instructions|
|---|---|
|source| Filename or identifier of the source document|
|type| Fixed value: "Overall Event"|
|title| Display title of the festival edition. For Festival d'Avignon IN: "Festival d'Avignon".|
|id| Unique identifier. Use FDAin (IN programme) or FDAoff (OFF) + - + year. E.g. FDAin-1988. If no explicit year: infer from edition number (1st = 1947, annual thereafter); if unavailable, use YYYY.|
|genre_category|Genre or category of the event. Use AAT controlled vocabulary.|
|date_beginning|Earliest start date (year minimum). If no explicit date on IN programme: infer from edition number (1st edition = 1947, annual). If unavailable: YYYY.|
|date_end| Latest end date. Same inference rules as date_beginning.|
|place| Location of the event.|
|director_name|Name of the artistic director of the festival.|
|director_verbatim_role| Verbatim role label as it appears in the source.|
|team_name| Name of a team member (person or group) involved in realising the event. Repeatable.|
|team_group| Group to which the team member belongs.|
|team_role|Role of the team member. Use BNF role vocabulary.|
|team_verbatim_role| Verbatim role label from source.|
|sponsor_name|Name of a sponsor. Repeatable.|
|sponsor_role|Role of the sponsor. Use AAT: "Patrons" for general supporters; "sponsors" for those assuming primary responsibility; "friends" for members of voluntary associations. Add new types if needed (e.g. for media sponsors). |
|sponsor_verbatim_role|Verbatim sponsor role from source (e.g. "parraine", "avec la participation de").|
|reference_textual_work|ID of a related Textual Work instance.|
|reference_digital_object | ID of a related Digital Object instance.|

---

### MODEL 2 — Programme (Textual Work / Document)

Represents the programme document itself as a textual work.

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|type|Type of programme. Choose from: "show programme", "general programme", "season programme".|
|title|Display title of the document.|
|id|Unique ID: FDS (show programme) or PROG (general/season) + FDAin/FDAoff + 4 first letters of production title (if known) + date + 4 random alphanumeric characters. E.g. FDS-FDAin-HAML-1988-a3bZ.|
|part_of_programme|ID of a parent programme, if this is a component.|
|title_type|Type of title. Use AAT controlled vocabulary (e.g. "titles proper", "subtitles").|
|creator_name|Name of the creator of the document. Repeatable.|
|creator_role|Role of the creator. Use BNF role vocabulary (publishing sector roles).|
|creator_verbatim_role|Verbatim role from source.|
|date|Year of the related event, unless an exact date is mentioned.|
|text_content|Verbatim transcription of the text portion as it appears in the programme. Extract the full text (e.g. the entire biography, the complete synopsis). Repeatable: one instance per distinct text portion.|
|text_language|Language of the text portion.|
|text_topic|Category of the text portion. Choose from: Biographie, Interview, Citation, Extrait de presse, Synopsis, Éditorial, Présentation générale, Information complémentaire sur la production, Note d'intention, Texte littéraire, Traduction, Autre.|
|link_to_production|ID of the production the text portion refers to, when multiple productions are present.|
|text_source|ID or reference to another document from which the text portion derives.|
|image_part|Reference to a visual item that is part of this textual work.|
|language|Overall language(s) of the document. List from most to least used if multilingual.|
|publisher_name|Publisher name.|
|publisher_role|Publisher role. Use BNF role vocabulary (publishing sector).|
|publisher_verbatim_role|Verbatim publisher role from source.|
|reference_textual_work|ID of a related Textual Work.|
|reference_digital_object|ID of a related Digital Object.|

---

### MODEL 3 — Textual Work (Play / Source Text)

Represents a literary or dramatic work referenced by the programme (the play, libretto, adapted text, etc.).

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|type|Fixed value: "Textual Work"|
|title|Title of the play or textual work.|
|id|Unique ID: Play + 4 letters of title + 4 letters of first creator name + 4 random alphanumeric chars. E.g. Play-HAML-SHAK-456g.|
|title_type|Type of title. Use AAT controlled vocabulary.|
|creator_name|Name of the author or creator. Repeatable.|
|creator_role|Role of the creator. Use BNF role vocabulary.|
|creator_verbatim_role|Verbatim role from source.|
|date|Date of creation or publication as mentioned in source.|
|publisher_name|Publisher name, if mentioned.|
|publisher_role|Publisher role. Use BNF role vocabulary.|
|publisher_verbatim_role|Verbatim publisher role from source.|
|reference_textual_work|ID of a related Textual Work.|
|reference_digital_object|ID of a related Digital Object.|

---

### MODEL 4 — Work

Represents the abstract artistic staging project (the Work in the LA-PA sense: e.g., Chéreau's Hamlet staging as a conceptual unit, independent of individual productions).

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|type|Fixed value: "Work"|
|title|Title of the work.|
|title_type|Type of title. Use AAT controlled vocabulary.|
|identifier|Unique ID: W + 4 letters of title + 4 letters of creator/company name (use nnnn if absent) + date_end (yyyy) + 4 random alphanumeric chars. E.g. W-HAML-CHER-1988-x7kL.|
|company_name|Producing company involved in creating the work.|
|company_role|Role of the company. Use BNF role vocabulary.|
|creator_name|Name of the creator (director, choreographer, etc.). Repeatable.|
|creator_role|Role of the creator. Use BNF role vocabulary.|
|creator_verbatim_role|Verbatim role from source.|
|date_beginning|Earliest date of creation (typically first rehearsal or creation period start).|
|date_end|Latest date of creation; usually the premiere date.|
|date_verbatim|Verbatim date string as it appears in source or historical documents.|
|play_used|ID of the Textual Work (Model 3) that is the source text. Only if explicitly mentioned in the programme.|
|adapted_from_inspired_by|ID of the Textual Work used as adaptation base, if different from play_used.|
|part_of|ID of a greater Work of which this work forms a part.|
|reference_textual_work|ID of a related Textual Work.|

---

### MODEL 5 — Production

Represents a specific production event: one staged realisation of a Work at a given time and place, with its full team, performers, and financing.

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|type|Fixed value: "Production"|
|title|Title of the production.|
|title_type|Type of title. Use AAT controlled vocabulary.|
|production_identifier|Unique ID: P + 4 letters of title + 4 letters of first team member + year of date_beginning (yyyy) + 4 random alphanumeric chars. E.g. P-HAML-CHER-1988-j2mN.|
|work_produced|ID of the Work (Model 4) that this production realises.|
|genre_verbatim|Genre as it appears verbatim in the source.|
|predicted_genre|Genre determined by the model. Use BNF role vocabulary if applicable; otherwise leave null.|
|language|Language of the production as stated in the source.|
|language_predicted|Language as inferred by the model. Leave null if same as language.|
|part_of_production|ID of the Overall Event or larger production of which this production forms a part.|
|order_in_production|Position of this production when scheduled with others. Format: "n/total", e.g. "1/3".|
|scheduled_with|ID of another production scheduled simultaneously.|
|date_beginning|Earliest date of the production.|
|date_end|Latest date of the production.|
|duration|Duration in minutes, if mentioned.|
|production_venue|Venue where the production takes place.|
|performers|List of performer objects. Each object: {name, group, role, verbatim_role, character}. Use BNF role vocabulary for role.|
|animals|List of animal objects. Each object: {name, species, verbatim_species, character}.|
|musicians|List of musician objects. Each object: {name, group, instrument_vocal_range, verbatim_role, character}.|
|team|List of team member objects. Each object: {name, group, role, verbatim_role}. Use BNF role vocabulary for role.|
|sponsors|List of sponsor objects. Each object: {name, role, verbatim_role}. Trigger words: "avec la participation de", "avec le soutien de". Role: AAT "Patrons".|
|funders|List of funder objects. Each object: {name, role, verbatim_role}. For financial contributors other than producers (e.g. "résidences", "remerciements").|
|producing_companies|List of producing company objects. Each object: {name, role, verbatim_role}. Trigger words: "Producteur", "Coproducteur".|
|audience|ID of an Audience instance (Model 6), if applicable.|
|reference_textual_work|ID of a related Textual Work.|
|reference_digital_object|ID of a related Digital Object.|

---

### MODEL 6 — Performance (Individual Showing)

Represents a single showing/representation of a production on a specific date and at a specific place. A Performance is part of a Production (and, by extension, of an Overall Event). Each scheduled date generates one Performance instance.

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|type|Fixed value: "Performance"|
|title|Title of the performance (typically the title of the production).|
|title_type|Type of title. Use AAT controlled vocabulary.|
|id|Unique ID: PE- + 4 letters of production title + year + 4 random alphanumeric chars. E.g. PE-HAML-1988-a1b2. Each performance instance on a distinct date gets a distinct ID.|
|premiere_type|Type of premiere, if mentioned (e.g. "world premiere", "French premiere").|
|premiere_verbatim|Verbatim premiere label from source.|
|part_of_event|Array of IDs linking this performance to all containing entities, from broadest to narrowest: Overall Event ID first, then parent Production IDs in hierarchical order (see composite programme rule below). E.g. ["FDAin-2011", "P-SUJE-nnnn-2011-greg", "P-PROG-nnnn-2011-grea", "P-TREN-DAVI-2011-grea"].|
|date_beginning|Date (and time if available) of the performance, ISO format: YYYY-MM-DD or YYYY-MM-DD HH:MM.|
|date_end|End date of the performance, if distinct from date_beginning.|
|performance_venue|Venue of the performance (verbatim or ID of Place instance).|
|digital_reference|URL or ID of a digital document referencing this performance.|
|audience|ID of an Audience instance (Model 7), if applicable.|
|performers|List of performer objects specific to this performance, if different from the production's general cast. Each object: {name, role, verbatim_role, character}.|
|reference_textual_work|ID of a related Textual Work.|

---

### MODEL 7 — Audience

Represents the audience of a production or event, including any quantitative dimension (capacity, attendance).

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|audience_name|String value of the audience name or designation (e.g. "Public", "Scolaires").|
|audience_name_type|Type of the audience name.|
|audience_id|Unique identifier for this audience instance.|
|part_of_event|ID of the Performance, Production, or Overall Event to which this audience belongs.|
|dimension_value|Numerical value of a dimension (e.g. attendance figure, capacity).|
|dimension_unit|Unit of the dimension (e.g. "persons").|
|dimension_type|Type of dimension (e.g. "capacity", "attendance").|
|reference_textual_work|ID of a related Textual Work.|
|reference_digital_object|ID of a related Digital Object.|

---

### MODEL 8 — Performance (Projected / Tour Dates)

Represents an individual performance date or a tour, linked to a production.

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|title|Title of the performance or tour.|
|part_of_production|ID of the Production (Model 5) to which this performance belongs.|
|date_beginning|Earliest date of the performance or first date of the tour.|
|date_end|Latest date of the performance or last date of the tour.|
|date_verbatim|Verbatim date string as it appears in the programme.|
|place_verbatim|Verbatim place name as it appears in the programme.|

---

### MODEL 9 — Place

Represents a named place or venue mentioned in the programme.

|Field|Instructions|
|---|---|
|source|Filename or identifier of the source document.|
|type|Fixed value: "Place"|
|id|Unique ID: PL + 4 letters of place name + 4 random alphanumeric chars. E.g. PL-COUR-123p.|
|place_name|Name of the place as it appears in the source.|
|place_type|Type of the place (e.g. "théâtre", "cour", "gymnase").|
|reference_textual_work|ID of a related Textual Work.|
|reference_digital_object|ID of a related Digital Object.|

---

## Additional Extraction Rules

1. Multiple instances: If the programme contains several productions, create one instance of Models 4, 5, and 6 per production.

2. Composite programme — hierarchical part_of rule: When a programme documents an evening composed of multiple individual works (e.g. Sujets à Vif – Programme A containing TRENTE-TROIS TOURS and VOYAGE COLA), apply the following at both Work and Production levels:
    - Create one parent Work/Production for the overarching event (e.g. W-SUJE, P-SUJE).  
    - If there is an intermediate grouping (e.g. Programme A / Programme B), create one intermediate Work/Production per group, with part_of → parent ID. 
    - Create one leaf Work/Production per individual spectacle, with part_of listing all ancestor IDs (parent + intermediate if applicable).
    - At the Performance level, part_of_event must list all hierarchy levels: [Overall Event ID, parent Production ID, intermediate Production ID (if any), leaf Production ID].
    - Example (Sujets à Vif, FDA 2011):
        - Works: W-SUJE (parent) → W-PROG-A (part_of: W-SUJE) → W-TREN (part_of: ["W-SUJE", "W-PROG-A"])   
        - Productions: P-SUJE → P-PROG-A (part_of: P-SUJE) → P-TREN (part_of: ["P-SUJE", "P-PROG-A"])  
        - Performance of TRENTE-TROIS TOURS on 2011-07-08: part_of_event: ["FDAin-2011", "P-SUJE-...", "P-PROG-A-...", "P-TREN-..."]

3. Verbatim copy: Never normalise or translate verbatim fields. Copy the exact string including capitalisation and diacritics.

4. Null vs. absent: Use null for fields not found in the source. Do not guess.

5. Roles: When a role label is present but does not match the BNF controlled vocabulary with ≥95% confidence, set the role field to null and preserve the string in the verbatim_role field.

6. AAT titles: Choose from the following values for title_type: titles (general, names), abbreviated titles, alternative titles, brief titles, collection titles, collective titles, constructed titles, descriptive titles, exhibition titles, former titles, full titles, generic titles, group titles, inscribed titles, original titles, popular titles, portfolio titles, published titles, repository titles, series titles, sub-group titles, subtitles, titles proper, title statements, translated titles, uniform titles, volume titles, working titles.

7. Repeatable fields: Fields marked as "Repeatable" in these instructions must be returned as JSON arrays, even if there is only one value.

Cross-references: Populate reference_textual_work and reference_digital_object with the id values you assign in Model 2 and Model 3 respectively.
"""