# The Kalson Cup 2026 — Whistling Straits

Father & Son Invitational — Whistling Straits and Blackwolf Run, Kohler,
Wisconsin. 20–23 August 2026.

**https://jkalson11.github.io/Whistling-Straits-Father-Son-/**

Michael Kalson · Josh Kalson · Matt Reiner · Jon Vandegrift

## The page

A single self-contained page (`index.html`) covering the field, the full
itinerary with tee times and dinner confirmations, the five courses, complete
scorecards, the match format, lodging and travel, local knowledge, and a
record book for past and future editions.

Edit `index.html` and commit to `main`; the site redeploys itself in about a
minute.

## Open items

Anything not yet confirmed shows a small **To confirm** chip on the page.
Search `index.html` for `class="tbd"` to find every one at once.

## Photographs

Drop files into `img/` using the names listed in `img/README.md` and they
appear automatically. Until a file exists the page falls back to its own
engraved artwork, so nothing breaks.

The anthem works the same way — see `audio/README.md`.

## Scorecards

All four full-length courses are transcribed in the page: hole names, par,
stroke index and five tee sets each.

`scorecards.py` holds the source data and regenerates that section. It refuses
to emit anything unless every computed Out / In / Total matches the figure
printed on the physical card — twenty tee sets across four courses — along
with the pars and a clean odd/even split of the stroke indexes.

```
python3 scorecards.py
```
