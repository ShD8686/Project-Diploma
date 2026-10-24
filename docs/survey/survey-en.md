# Survey: walking in hot weather and shade on the route

Ready to copy into Google Forms. About 4-5 minutes, anonymous. The questionnaire is given in English for documentation;
the form distributed to respondents is in Russian (`survey-ru.md`, same questions and numbering).
Target sample (proposal): at least 100 responses, of which at least 40 students and 40 residents (TODO: approve with the supervisor).

## Intro text (first page of the form)
Hello! I am Damir, a student at Astana IT University. For my diploma project I am developing a system that builds walking
routes taking the shade of buildings into account. The survey is anonymous and voluntary; no personal data (name, phone, e-mail)
is collected. Answers are used only in aggregated form. You can stop at any time. By pressing "Next" you agree to take part.

## Block A. About you
| No. | Question | Type | Options |
|---|---|---|---|
| A1 | Your status | single choice | Student; Working; Studying and working; Retired; Other |
| A2 | Age | single choice | under 18; 18-24; 25-34; 35-49; 50-64; 65+ |
| A3 | District of Astana where you walk most often | single choice | Yesil; Almaty; Saryarka; Baikonur; Other / not in Astana |
| A4 | Do you have a condition that makes heat or sun harder to bear (age, health, stroller, light sensitivity)? | single choice | Yes; No; Prefer not to say |

## Block B. Walking habits
| No. | Question | Type | Options |
|---|---|---|---|
| B1 | How often do you walk at least 10 minutes in the warm season (May-September)? | single choice | Almost daily; 3-5 times a week; 1-2 times a week; Less often |
| B2 | Where do you walk most often? | multiple choice | Study/work; Shops and services; Bus stop/metro; Leisure; Sport; Other |
| B3 | Typical walking trip length | single choice | up to 10 min; 10-20 min; 20-30 min; over 30 min |
| B4 | Do you use an app for walking routes? | multiple choice | Yandex Maps; Google Maps; 2GIS; Other; None |

## Block C. Heat, sun and shade
Scale for C1-C5: 1 = strongly disagree, 2 = somewhat disagree, 3 = neutral, 4 = somewhat agree, 5 = strongly agree.
| No. | Statement | Scale |
|---|---|---|
| C1 | In summer, walking in the sun is unpleasant for me | 1-5 |
| C2 | I deliberately choose the shady side of the street or a shady route | 1-5 |
| C3 | In the heat I give up walking in favour of transport | 1-5 |
| C4 | I know at what time of day my route is shaded and when it is not | 1-5 |
| C5 | I sometimes walk longer in order to walk in the shade | 1-5 |

| No. | Question | Type | Options |
|---|---|---|---|
| C6 | What most often makes you change your route in the heat? | up to 2 answers | Shade; Trees/park; Coolness near water/fountains; Fewer people; Shorter path; I change nothing |

## Block D. Willingness to detour (informs the detour limit)
Imagine a hot summer day. The shortest path takes **15 minutes** and mostly runs in the sun. Another path has clearly more shade.
| No. | Question | Type | Options |
|---|---|---|---|
| D1 | How much longer would you walk for significantly more shade? | single choice | Not at all; +1-2 min (about +10%); +3-4 min (about +25%); +5-7 min (about +40%); more than 7 min (over +45%) |
| D2 | Same question for a **short** 5-minute path | single choice | Not at all; +0.5 min (about +10%); +1 min (about +20%); +2 min (about +40%); more than 2 min |
| D3 | How would you prefer to choose between the shortest and the shady path? | single choice | The app shows 3 variants at once; I move a "shade - shorter" slider; Only one recommended route; Does not matter |

## Block E. Which features you need
Scale for E1-E6: importance from 1 (not important) to 5 (very important).
| No. | Feature | Scale |
|---|---|---|
| E1 | Choosing date and time of departure | 1-5 |
| E2 | Shade on the map (shade/sun colours along the route) | 1-5 |
| E3 | Length, shade share and "how much longer" for each variant | 1-5 |
| E4 | A "shade - shorter" slider | 1-5 |
| E5 | A mobile app (not only web) | 1-5 |
| E6 | Taking trees into account, not only buildings | 1-5 |

| No. | Question | Type | Options |
|---|---|---|---|
| E7 | Would you use such a system on hot days? | single choice | Definitely yes; Probably yes; Not sure; Probably not; Definitely not |
| E8 | What is most important for you to see in such an app? (one sentence) | text | - |

## Block F. Finish
| No. | Question | Type |
|---|---|---|
| F1 | Would you like to try the prototype and give feedback? (leave an e-mail, used only for contact and stored separately from answers) | optional, text |
| F2 | Comments and wishes | optional, text |

## Link between questions and the project
| Questions | What they give | Where it goes |
|---|---|---|
| D1, D2 | Real willingness to detour | Justification of the detour limit (FR-7, default +30%) and of the M3 threshold (median <= 15%, max <= 30%) |
| D3, E4 | Preferred way to choose | Interface design, lambda slider and three modes (FR-3, FR-4) |
| E1, E2, E3 | Importance of time, map, metrics | FR-1, FR-5, API response |
| E5, E6 | Demand for mobile app and trees | Won't list and future work |
| C1-C5, B1-B3 | Problem and target audience description | Problem statement, relevance |
| E7 | Intention to use | Complement to usability (NFR-8) |

## Analysis plan (quantitative)
- Descriptive statistics: shares, medians and interquartile ranges for all questions; Likert scales treated as ordinal.
- Compare "students" and "residents" on C1-C5, D1, E7: Mann-Whitney test; for categorical data chi-squared (or Fisher's exact test for small cells).
- Key result for the project: distribution of D1 and D2, i.e. the percentage willing to accept a detour of <= 15% and <= 30%.
- Sample limitation: the survey is voluntary and not random, so conclusions describe the respondents, not all residents of Astana. This must be stated in the thesis.

## Separate questionnaire after the prototype: SUS (for NFR-8)
Give it to 5 test participants after they perform tasks on the prototype. Scale 1-5 (strongly disagree - strongly agree).
1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

SUS scoring: for odd items (score - 1), for even items (5 - score); multiply the sum by 2.5. Result 0-100; the target from the requirements is SUS >= 68.
Also measure the time for the task "build a shaded route" (target <= 60 s, NFR-8).
