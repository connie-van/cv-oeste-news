# Oeste News — update rules

These rules are read at the start of every scheduled update. Follow all of them.

## Coverage
1. Towns: Rincón (top priority — search it first and most thoroughly), Aguada, Aguadilla, Añasco, Mayagüez.
2. Look back about 2 days each run. Cover all kinds of local news, not just crime: community events, weather/flood/surf advisories, power and water outages, roads, municipal government, business, beaches, food and culture, schools.
3. Good sources: El Nuevo Día, Primera Hora, Metro PR, El Vocero, Telemundo PR, WAPA, NotiCel, Foro Noticioso, Periódico La Perla, Semanario Visión, municipal websites, NWS San Juan, LUMA.

## Writing
4. Read each article (WebFetch) before writing it up. Write everything in plain English in your own words; never copy article sentences. Never invent details. Only add stories with a real https link.
5. Photos and video (Bean may ask to turn this off — if rules.md ever says media is off, add no image/video fields):
   a. Photo: if an article's own preview image (og:image) is a real photo of the story — the people, place or event — add "image": {"src": <the outlet's https image URL>, "credit": "Photo: <outlet>" or "Photo: supplied, via <outlet>", "alt": <short description>}. Never use generic, file ("Archivo"), stock (e.g. Pexels) or "genérica" images. Never download or copy images; only link the outlet's own URL.
   b. Photos of private people (victims, suspects, family) only when a news outlet published them with its own story — never from social media or other sources.
   c. Video: if the outlet published the story's video on YouTube, add "video": {"provider": "youtube", "id": <video id>, "credit": "Video: <outlet>"}. Only the outlet's own upload.

## Archive and duplicates
6. news.json is a permanent archive that powers the calendar. Never delete existing items or rewrite their original content.
7. Skip any story already saved: same url, or the same event reported by a different outlet.
8. Exception — real new information (arrest, charges, change in someone's condition, cause found, date or plan change, etc.):
   a. Add an entry to the original item's "updates" list: {date, text, source, url}. "text" is 1–2 sentences of only what's new.
   b. Also add one new item dated the day of the update, with "ref" set to the original item's id, a title starting with "Update:", a summary of only what's new, plus facts and body as usual. Same town and category as the original.
9. Nothing new about a known story → add nothing.

## Power & internet (check every run)
news.json has a "utilities" object: {checked, area, luma:{status, headline, detail, updates[]}, claro:{...}}. The focus area is Rincón's pueblo (Barrio Pueblo), Sector Villa Angélica and Sector Corea (Korea).
- Each run, check: LUMA's service status and planned-work list (lumapr.com, lumapr.com/mejorasplanificadas), LUMA and Claro Puerto Rico posts, and news about outages, load shedding (relevos de carga), brownouts, voltage drops or fiber cuts affecting Rincón or the Mayagüez region. If the Rincón outages Facebook group (https://www.facebook.com/groups/1026755354056860/) is readable without logging in, use posts there only as leads, and say "neighbors report" unless an official source or news outlet confirms.
- status is one of: ok, issue (outage), unstable (brownouts, flickering, slow or intermittent service), planned (scheduled work), restored, unknown. headline is a few words ("Outage in pueblo since 2 p.m."); detail is 1–3 sentences on what's affected and what's known.
- Add an entry to updates [{time (ISO with -04:00), text, source, url}] whenever something changes: a new outage, an estimated restoration time, crews on site, service restored. Keep older entries; drop entries older than 14 days.
- Always set "checked" to the current time, even when nothing changed. Never claim a service is working or down without a source; if you can't tell, use unknown.

## Earth watch
Earth watch has live weather alerts (NWS) and earthquakes (USGS) built in. Your job is the "earth" list in news.json: short researched reports on climate and natural events that matter for Puerto Rico's west coast.
- Cover: El Niño / La Niña updates (NOAA's monthly discussion), notable earthquakes or tsunami news for the Mona Passage and west coast, tropical storms and hurricanes threatening Puerto Rico, droughts, floods, sargassum, coral bleaching, and nature reports like unusual blooms, bee or honey seasons, turtle nesting and whale season.
- West coast first: prefer stories about Rincón, Aguada, Aguadilla, Añasco, Mayagüez, the Mona Passage and Desecheo; island-wide stories are fine when they affect the west.
- Facts only: every report needs a real source link (NOAA, NWS, USGS, Red Sísmica, DRNA, universities or established news outlets). No rumors or social-media posts.
- Format: {id, date (YYYY-MM-DD), cat (Climate, Seismic, Tropics, Nature, Ocean), title, summary (1–2 sentences), body (2–3 short paragraphs), source, url}. Same archive rules: only append, skip duplicates, add a new dated report when there's real new information.

## Case tracker
10. Flamas case (tracking id "flamas"): shooting ~1:24 a.m. Nov 20, 2026, in front of Restaurante Flamas, barrio Victoria, Aguadilla; victim Alejandro Chaparro, 66, of Aguada; CIC Aguadilla Homicide Division investigating. Search specifically for new developments each run. If found: add a timeline entry at the top {date, text, source, url, body} and update status and summary. If nothing new: only change the date on the top "No new public developments" entry to today.

## Item format
11. New item fields: id (unique slug like "rin-word-mmdd"), town (exactly one of the five), date (YYYY-MM-DD), cat (Power, Weather, Food & culture, Events, Travel, Development, Crime, Courts, Accident), title, summary (1–2 sentences), facts (2–4 [label, value] pairs), body (2–3 short paragraphs), source, url, optional media, optional ref, optional updates.

## Message to Bean
12. After publishing, send a short message: first line is the Flamas case (the new development, or "No new developments in the Flamas case"). Then up to 3 new Rincón items and up to 2 from nearby towns, one line each — or say nothing new turned up. Brief and direct.
