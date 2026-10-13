# BRAG Plan — Customer Insurance Purchase Prediction System

## Invocation
`/brag --tone cinematic` (cinematic, landscape, no voice).

## 9-question rubric

1. **What is the app?**
   A supervised machine-learning pipeline that predicts which customers will purchase insurance from demographic data (Age, Estimated Salary), built during a 15-week AI/ML internship at IntrnForte Technologies.

2. **Most impressive claim.**
   Five classifiers were benchmarked; K-Nearest Neighbors won at 93% accuracy (89% precision / 92% recall on the positive class).

3. **Visual hook.**
   A scatter ocean of customers splitting into two camps — buyers and non-buyers — as a decision boundary cuts between them.

4. **What should be shown from the actual project?**
   The Age × Estimated Salary scatter plot (colored by purchase outcome, coolwarm) and the five-model accuracy comparison.

5. **Shortest satisfying video.**
   20 seconds. Hook → reveal → model leaderboard → KNN hero → scatter plot → outro.

6. **Tone.**
   Preset: `cinematic`. Direction: "data-lab trailer — the buyers were never random."

7. **Audio.**
   Steady cinematic bed (`vol-12`), restrained impact SFX. Audio-reactive: subtle; hero glow and cards breathe with RMS. No waveform visuals.

8. **Share caption.** See `share-copy.txt`.

9. **User flow worth showing.**
   Load demographic data → train and compare five classifiers → read the best model's verdict on a customer.

## Angle

Insurance sales look like luck until you plot the customers. The video treats the dataset as a hidden pattern the model exposes: a scatter that separates buyers from non-buyers, five models racing, and one clear winner. Cinematic scale, declarative sentences.

Pattern: Hook (0–3.5s) → Reveal (3.5–7.0s) → Highlights (7.0–17.4s) → Outro (17.4–20.5s).

## Storyboard (total: 20.5s)

### Scene 1 — Hook — 0.0–3.5s
- Dark lab grid; scattered data points drift in.
- Line 1 "SOME CUSTOMERS BUY." at 0.2s.
- Line 2 "THE DATA KNOWS WHICH." at 0.9s, second half in accent blue.
- SFX: `impact/impactSoft_medium_000` at 0.15s.
- Fade out at 3.1s.

### Scene 2 — Reveal — 3.5–7.0s
- Badge "AI / ML INTERNSHIP PROJECT" at 3.7s.
- Title "Customer Insurance Purchase Prediction" two lines at 3.82s (near beat 3.82).
- Subtitle "Five classifiers. A 100-record test set. One clear winner." at 4.6s.
- Accent underline scaleX 0→1 at 4.7s.
- SFX: `impact/impactBell_heavy_000` at 3.7s.
- Fade out at 6.6s.

### Scene 3 — Model leaderboard — 7.0–10.5s
- Eyebrow "FIVE CLASSIFIERS, BENCHMARKED" at 7.2s.
- Horizontal bars grow: Decision Tree 84% (7.64), SVM 86% (8.19), Logistic Regression 88% (8.74, strong cue // beat-locked), Random Forest 89% (9.0), KNN 93% (9.29).
- SFX: `interface/drop_001..003` on first bars.
- Fade out at 10.1s.

### Scene 4 — KNN hero — 10.5–14.0s
- Eyebrow "BEST MODEL — K-NEAREST NEIGHBORS" at 10.7s.
- Big stat counts 0→93% starting on strong cue 10.93 (// beat-locked).
- Label "accuracy" at 11.5s.
- Sub "89% precision · 92% recall on the positive class." at 12.0s.
- SFX: `impact/impactMetal_medium_002` at 10.9s.
- Fade out at 13.6s.

### Scene 5 — Scatter plot — 14.0–17.4s
- Eyebrow "AGE × ESTIMATED SALARY" at 14.2s.
- Scatter card scales in at 14.73s: axes, grey non-buyers, blue buyers, decision boundary drawn.
- Points pop on beats 15.29→16.38 (// beat-grid).
- Caption "Purchase outcome, plotted and separated." at 16.5s.
- SFX: `impact/impactSoft_medium_001` at 14.7s.
- Fade out at 17.0s.

### Scene 6 — Outro — 17.4–20.5s
- "CUSTOMER INSURANCE PREDICTION" slams in at 17.47s (// beat-locked).
- Tagline "Predict the buyer before the pitch." at 18.3s.
- Accent bar scaleX at 18.56s (// beat-locked).
- SFX: `impact/impactBell_heavy_004` at 17.45s; music fades under the logo.

## Music cue guidance
Source: bundled preset `<skill-dir>/assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json`.
Strong cues used: 8.74s, 10.93s, 17.47s, 18.56s. Cue metadata is optional timing guidance.

## Voiceover
Not requested. No narration.
