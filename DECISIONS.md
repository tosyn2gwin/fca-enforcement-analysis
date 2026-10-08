# Decisions and known limitations

## Coverage
- Data covers 2016 to 2026 inclusive (11 years, 200 entries).
- Earlier years were excluded: the FCA's /news/news-stories/<year>-fines
  pages do not exist for 2013-2015, so the decade is 2016 onward.

## Scope: who and what is included
- Both firms and individuals are included, as the FCA publishes them together.
- Court fines from criminal prosecutions (2 entries) are included but flagged
  with is_court_fine = 1, so they can be excluded from penalty analysis.
  These are not FCA regulatory penalties and arguably answer a different question.

## Dates
- Dates are the date of the Final Notice or press release, i.e. the enforcement
  date, NOT the date of the underlying conduct. Conduct often predates the
  penalty by several years. Any trend over time is a trend in enforcement
  activity, not in misconduct.
- One 2022 entry used a two-digit year (12/10/22). Both formats are handled.

## Amounts
- amount_raw keeps the FCA's original text; amount_gbp is the parsed number.
- One 2022 entry (Thomas Henry Ward) has no amount on the FCA's page.
  Stored as NULL, not 0, and excluded from amount-based totals.
  Treating it as £0 would understate averages.

## Links
- Some entries link to the Final Notice PDF, others to a press release.
  Session 3 classification quality may vary between the two.