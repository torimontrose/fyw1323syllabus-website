# Print PDF syllabus generator

Generates the magazine-style print PDF from the exact text on the live site
(re-transcribed by hand into `fyw_data.py` / `build_fyw.py` — if the live
site's `index.html` changes, these files need to be updated to match).

## Regenerate the PDF

```
python3 build_fyw.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-margins \
  --print-to-pdf="FYW1323-Syllabus.pdf" --print-to-pdf-no-header \
  "file://$(pwd)/fyw-syllabus.html"
```

Output: `FYW1323-Syllabus.pdf`, plus `fyw-syllabus.html` (intermediate, safe
to ignore/delete and regenerate).

## Files

- `print-system.css` — shared component library (also used by REL 224 and
  REL 320's generators; identical copy in each repo, not linked)
- `gen_schedule.py` — shared schedule-table HTML generator
- `build_fyw.py` — page layout/content for this course
- `fyw_data.py` — schedule row data, transcribed verbatim from the site
- `cover-photo.png` — cover image

## Rules this must follow (see project memory for full detail)

- White page background (ink-saving for printing) — small dark accent
  blocks (cover hero, schedule title bar) are fine to keep.
- Every line of prose/schedule content must match the live site **exactly**
  — no paraphrasing, no cuts.
- After any rebuild, verify every page's rendered content against the site
  text programmatically (extract PDF text via PyMuPDF, check for expected
  phrases + check no page's content exceeds ~780pt of the 792pt page height)
  before treating it as done.
