# FYW 1323 Syllabus Website — Editing Guide

This is a plain HTML/CSS/JavaScript website. There's no build step, no
installs, and no command line needed to edit it — just open the file in a
text editor, change the text, save, and refresh your browser.

## Files

```
syllabus website/
├── index.html      ← all the syllabus content lives here
├── css/styles.css   ← colors, fonts, spacing (rarely needs editing)
├── js/tabs.js        ← makes the tabs work (you shouldn't need to touch this)
└── README.md         ← this file
```

**You will do almost all of your editing inside `index.html`.**

## How to edit the content

1. Open `index.html` in any text editor (TextEdit in plain-text mode,
   VS Code, Notepad, etc.).
2. Use Find (Cmd+F / Ctrl+F) to search for `EDIT:` — every spot that needs
   your real information has an `<!-- EDIT: ... -->` comment right above or
   next to it explaining what to change. There are about 30 of these.
3. Replace placeholder text (names, dates, emails, policies) with your own.
   Comments themselves (the `<!-- ... -->` parts) are invisible on the
   actual website — you can leave them in place, or delete them once
   you've made the edit.
4. Save the file, then open `index.html` in your browser (double-click it,
   or drag it into a browser window) to see your changes.

### Editing a table (grading breakdown, schedule, rubric)

Tables are built from repeating blocks that look like this:

```html
<tr><td>Essay 1: Defining the Undefinable (rhetorical analysis)</td><td class="num">15%</td></tr>
```

Each `<tr>...</tr>` is one row. Each `<td>...</td>` inside it is one cell.
To add a new week to the schedule or a new grading category, copy an
existing `<tr>...</tr>` line, paste it as a new line, and edit the text
inside the `<td>` tags.

### Editing a policy block

Policies live in blocks like this — just edit the text between the tags:

```html
<div class="policy-block">
  <h3>Attendance</h3>
  <p>Your policy text goes here.</p>
</div>
```

To add a whole new policy, copy one of these `<div class="policy-block">
...</div>` blocks and paste it below an existing one.

## Publishing the site

This site is static, so you can host it almost anywhere for free:

- **GitHub Pages** — push this folder to a GitHub repo and enable Pages in
  the repo settings.
- **Your university's web space** — many schools give faculty a personal
  web folder (ask your IT department).
- **Netlify / Vercel** — drag-and-drop the folder onto their dashboard.

You can also just email students the `index.html` file, or post it to your
LMS (Canvas/Blackboard) as a file — it will open correctly in any browser
without needing to be "hosted" anywhere.

## Accessibility notes (please keep these intact)

This site was built to meet WCAG accessibility guidelines for students
with disabilities:

- Tabs work with keyboard navigation (arrow keys, Home/End) and are
  announced correctly by screen readers.
- There's a "Skip to main content" link for keyboard users.
- Color contrast between text and backgrounds meets AA standards.
- Tables use proper header cells (`<th scope="col">`) so screen readers
  can announce column headers with each cell.
- The print stylesheet forces black-on-white text for anyone who prints
  the syllabus.

If you add new content, try to:
- Keep heading levels in order (don't skip from `<h2>` to `<h4>`).
- Give any new images meaningful `alt` text (or `alt=""` if purely
  decorative).
- Use real table markup (`<table>`, `<tr>`, `<td>`) for tabular data
  rather than trying to fake it with spaces or line breaks.

## Changing colors or fonts

Open `css/styles.css` and look at the top of the file, inside the `:root {
... }` block. Every color used on the site is defined there once — change
a value there (e.g. `--teal: #5eead4;`) and it updates everywhere that
color is used.
