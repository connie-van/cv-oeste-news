# Oeste News — update rules

These rules are read at the start of every scheduled update. Follow all of them.

## Coverage
1. Towns: Rincón (top priority — search it first and most thoroughly), Aguada, Aguadilla, Añasco, Mayagüez.
2. Look back about 2 days each run. Cover all kinds of local news, not just crime: community events, weather/flood/surf advisories, power and water outages, roads, municipal government, business, beaches, food and culture, schools.
3. Good sources: El Nuevo Día, Primera Hora, Metro PR, El Vocero, Telemundo PR, WAPA, NotiCel, Foro Noticioso, Periódico La Perla, Semanario Visión, municipal websites, NWS San Juan, LUMA.

## Writing
4. Read each article (WebFetch) before writing it up. Write everything in plain English in your own words; never copy article sentences. Never invent details. Only add stories with a real https link.
5. Set media to "photo" or "video" only when the article has real photos or video of the story itself — not generic file/stock photos.

## Archive and duplicates
6. news.json is a permanent archive that powers the calendar. Never delete existing items or rewrite their original content.
7. Skip any story already saved: same url, or the same event reported by a different outlet.
8. Exception — real new information (arrest, charges, change in someone's condition, cause found, date or plan change, etc.):
   a. Add an entry to the original item's "updates" list: {date, text, source, url}. "text" is 1–2 sentences of only what's new.
   b. Also add one new item dated the day of the update, with "ref" set to the original item's id, a title starting with "Update:", a summary of only what's new, plus facts and body as usual. Same town and category as the original.
9. Nothing new about a known story → add nothing.

## Case tracker
10. Flamas case (tracking id "flamas"): shooting ~1:24 a.m. Nov 20, 2026, in front of Restaurante Flamas, barrio Victoria, Aguadilla; victim Alejandro Chaparro, 66, of Aguada; CIC Aguadilla Homicide Division investigating. Search specifically for new developments each run. If found: add a timeline entry at the top {date, text, source, url, body} and update status and summary. If nothing new: only change the date on the top "No new public developments" entry to today.

## Item format
11. New item fields: id (unique slug like "rin-word-mmdd"), town (exactly one of the five), date (YYYY-MM-DD), cat (Power, Weather, Food & culture, Events, Travel, Development, Crime, Courts, Accident), title, summary (1–2 sentences), facts (2–4 [label, value] pairs), body (2–3 short paragraphs), source, url, optional media, optional ref, optional updates.

## Message to Bean
12. After publishing, send a short message: first line is the Flamas case (the new development, or "No new developments in the Flamas case"). Then up to 3 new Rincón items and up to 2 from nearby towns, one line each — or say nothing new turned up. Brief and direct.
