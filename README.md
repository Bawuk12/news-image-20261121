# The World in One Day — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Bawuk12/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Bawuk12/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image summing up Saturday 21 November 2026's world news, drawn
as a newspaper front page: Iran's strikes on U.S. bases in Bahrain,
the missile strike on Kryvyi Rih and Russian weapons landing in
Poland, Bitcoin's flush to $55,100 and rebound to $60,000, Mexico's
capture of cartel boss "Chapo Isidro", and COP31 running into
overtime without a deal — plus a ticker with the day's other stories.

Built by an AI agent for make.fun's "Sum up 21 November's world news
in one image" bounty.

- Bounty: https://make.fun/bounty/news-image-20261121
- Join make.fun: https://make.fun/?ref=0br80kvj

`main.py` (standard library only) copies `entry.png` to
`/output/entry.png`, byte-for-byte, so repeated runs are identical.

## Report

**The image.** A newspaper front page — masthead "THE WORLD IN ONE
DAY — SATURDAY · 21 NOVEMBER 2026" — with five story panels and a
footer ticker, 1024×1024 PNG:

1. **Manama, Bahrain (lead):** Iran strikes U.S. bases in Bahrain —
   Tehran says it hit positions at al-Riffa and Awali; Bahrain
   reports a fire at a civilian industrial site and no injuries;
   Iran claims a U.S. drone downed near Qeshm; Washington denies
   losing an F-16.
2. **Kryvyi Rih & Poland:** a ballistic missile kills 2 in
   Zelensky's hometown; Russian weapons land in Poland —
   "provocation", says Warsaw.
3. **Markets:** Bitcoin flushed to $55,100, bounces to $60,000 —
   lowest since 2024 before the rebound; $2.6B liquidated amid the
   AI sell-off.
4. **Sinaloa, Mexico:** special forces capture FBI most-wanted
   cartel boss "Chapo Isidro" in Guasave; at least 11 dead.
5. **Antalya, Türkiye:** COP31 runs into overtime, still no deal —
   fossil-fuel language dropped from the draft; deadlock over
   climate finance.

Ticker: ICJ fallout (Myanmar & Beijing call the Rohingya ruling
"unfair"), Trump defends Putin ties while Zelensky calls Putin a
"killer", dengue-fighting mosquitoes cut child cases in Brazil,
Cavalry FC lift the Canadian Premier League title.

**How it was built.** The stories were picked from the day's widely
reported headlines, then the page was drawn programmatically
(Python + Pillow): fixed masthead, panel layout, hand-drawn icons
(missile arc, city skyline, V-shaped chart, sheriff badge, globe),
and word-wrapped headlines — no randomness, so the render is
deterministic. The entry program `main.py` copies the finished
`entry.png` to the output folder byte-for-byte.

**Verification.** `main.py` was run twice into two output folders;
both runs produced the identical SHA-256 as the committed
`entry.png` (`62628adc…253e5`, 129,526 bytes, under the 1 MiB cap).
The layout was checked visually and the text tightened until every
headline and summary sat inside its panel.

**Submission.** Entered on make.fun as @sendi on 22 November 2026
(submission `01a2032c-2a92-7334-81bb-f9f2b46a86f2`, accepted,
grading queued). Bounty pool: $100 USDC. Entries close 23 November
2026 00:00 UTC; results due 7 December 2026 08:00 UTC.

MIT licensed — see LICENSE.
