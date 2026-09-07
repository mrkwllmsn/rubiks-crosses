# Every Face a Cross

An interactive walkthrough of a Rubik's Cube pattern that puts a cross on all six
faces using nothing but the Right-Hand Algorithm (`R U R' U'`).

## The method

Pick a face to look at — your **anchor**. Run the Right-Hand Algorithm three times,
turn the whole cube a quarter turn clockwise while still watching the anchor, and
repeat. After exactly **9 rounds** the anchor comes back solid, along with the face
behind it, and the four faces ringing them are crosses.

Then change anchor: turn one of the cross faces to the front and run the same nine
rounds against it. All six faces end up with a cross.

```
phase 1:  (R U R' U' ×3, z) ×9      anchor + opposite solid, 4 crosses
re-anchor: y                        a cross face comes to the front
phase 2:  (R U R' U' ×3, z) ×9      six crosses
```

216 face turns, 19 whole-cube rotations, one algorithm.

Nothing recognisable appears before round 9 — no partial cross, no hint you are
close — which is why the pattern is easy to miss.

### Choosing the two colours

In phase one every face keeps its own colour as the background and takes as its
cross *the colour a single spin would bring onto it* — spinning clockwise, that is
the face on its left. Put the background colour on top and the cross colour on its
left before you start. Only adjacent colours can pair, so opposite colours never
meet. Stop at the end of phase one if you want a specific pair; phase two
re-colours everything.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Source of truth. Authored for the Claude Artifact host, which supplies the `<!doctype>`, `<head>`, viewport meta and a small reset — so this file does **not** render correctly on its own (a phone will lay it out at 980px). |
| `docs/index.html` | Generated, and what gets served. The same page wrapped for ordinary hosting or `file://`. |
| `build.py` | Regenerates `docs/index.html` from `index.html`. |

Edit `index.html`, then:

```sh
python3 build.py
```

## Publishing

`docs/` is laid out for GitHub Pages. In the repository settings, under
**Pages**, set the source to **Deploy from a branch**, branch `main`, folder
`/docs`. Commit the regenerated `docs/index.html` alongside any change to
`index.html`, or the published page will lag the source.

The verified move sequence and the colour rules above were both checked against a
cube simulator before the page was written.

Found by Mark Williamson.
