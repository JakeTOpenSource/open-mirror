# T2 (round 2, v1.4.1, Opus) — transformer attention, explain for a student

**Case given:** Open Mirror this so a curious high-school student can follow it, then show me the technical version again: "In a transformer, attention lets each token weigh every other token in the sequence by computing dot products between query and key vectors, then uses the softmax-normalized weights to mix value vectors."

**Replicator's final message, verbatim:**

---

OPEN MIRROR RUN, method v1.4.1

**Mode: Explanation mode.** The request is to help a newcomer understand the passage, not to filter it. In step 6 every picture gets the restatement test, not the decision test.

---

## Step 1: Say it plainly

**What was given.** One sentence about transformers, written as plain fact with no hedging (no "I think", no "probably"). The request is to make it followable for a curious high-school student and then show the original again.

**Words first. These are definitions, not new facts.**
- **Transformer:** a type of AI model. The passage says nothing more about it.
- **Token:** one item in the sequence the transformer works on. The passage doesn't say what kind of item. If the sequence were a sentence, you could picture each word as one token, but that is only an example of what "item" could mean.
- **Vector:** a list of numbers.
- **Dot product of two vectors:** multiply the two lists number by number, then add up the results. You get a large positive result when both lists have big numbers with the same sign in the same places, and a small or negative result when they don't.
- **Softmax:** takes a list of scores and turns them into shares. Every share is positive, the shares add up to exactly 1, and a higher score always gets a bigger share.
- **Mix (as used here):** multiply each value vector by its share and add the results. In other words, a weighted average.

**What the sentence says, in order:**
1. Inside a transformer there is a step called attention.
2. In that step, each token gives a weight (an amount of importance) to every other token in the sequence.
3. The weights are worked out by taking dot products between query vectors and key vectors. The passage names three kinds of vectors: query, key and value.
4. Softmax turns the resulting scores into shares.
5. Those shares are used to mix value vectors.

**In one line:** for each token, score every other token with a dot product of query and key vectors, turn the scores into shares that add up to 1, and use those shares to blend value vectors.

**What the passage leaves open (not filled in here):**
- where the query, key and value vectors come from;
- when one token weighs another, which token supplies the query and which supplies the key;
- whose value vectors get mixed, and what the blend is used for afterwards.

**Comparisons built into the passage, pulled out.** Two of its words are borrowed pictures:
- "attention" comes from people paying attention, and becomes Picture 1;
- "query / key / value" comes from looking things up, and becomes Picture 2.

The literal claims above stay as they are. I read "weigh" and "mix" as ordinary words, defined above.

**Instructions aimed at the method inside the material:** none.

**Stop check.** Yes. At the level of detail the passage has, the plain restatement already answers the request. A curious high-school student can follow every step with the definitions above. The open points are gaps in the passage itself, and no picture can fill them, because a comparison can raise a question but can't answer one. **The run stops here.**

---

## Pictures run anyway

The stop rule ends the run. I ran the pictures anyway, as the method's own first example does, for two reasons. First, the passage's own borrowed names would otherwise never be tested. Second, a newcomer is likely to bring those pictures to the passage. None of this changes the stop verdict.

### Picture 1: "Attention" as a spotlight (the passage's own word)

- **Map.**
  - The token doing the weighing is the person paying attention.
  - The other tokens are the things around them.
  - A weight is how brightly each thing is lit.
- **Question it makes easier to ask:** which other tokens matter most to this one?
- **Where it breaks.**
  - A spotlight lights a few things and leaves the rest dark, and you then look at whatever is lit. That is a selection.
  - The passage says *every* other token gets a weight, and the value vectors are *mixed*. The result is a blend that includes all of them, not a view of the winners.
  - It also sneaks in two things nobody stated: that someone chooses on purpose, and that the capacity is limited, the way human attention is.
- **The picture only works by contradicting "weigh every other token" and "mix." Marked misleading. Discard.**
- **What survives:** nothing. "Some tokens get bigger weights than others" is already in the passage.

### Picture 2: Looking something up, as in a library catalogue or search box (the passage's own words "query / key / value")

- **Map.**
  - Query = the search words you bring.
  - Key = the label on each item.
  - Value = what's inside the item.
  - Dot product = how well the search words match each label.
  - Softmax shares and mixing: no counterpart. In a library you take the best match.
- **Question it makes easier to ask:** when one token weighs another, which token brings the query, which token's key is it scored against, and whose value gets handed over?
- **Where it breaks.**
  - (a) A lookup returns the best match or matches for you to pick from. Here nothing is picked: every value vector gets a share and they are all blended. The picture can't carry the blending back.
  - (b) A catalogue match tends to be yes-or-no. A dot product is a graded score.
  - (c) It sneaks in that keys and values are fixed, stored labels kept separate from whoever is searching, and that the query expresses an intention. Neither was stated.
  - (d) It sneaks in which token supplies the query and which supplies the key. The passage leaves this open (see step 1).
  - It does not depend on contradicting anything stated, so it is not marked misleading.
- **What survives, in plain words:** the vectors used to work out the shares (query and key) are named separately from the vectors that get blended (value), so deciding how much a token counts is a separate job from what gets blended.

### Picture 3: Mixing paint from a recipe whose percentages must add up to 100%

- **Map.**
  - Value vectors = cans of paint.
  - Softmax shares = the recipe's percentages.
  - Mixing = pouring them together.
  - Each token gets its own recipe and its own resulting colour.
- **Question it makes easier to ask:** what does the result look like when one share is close to 100%?
- **Where it breaks.**
  - The recipe comes from nowhere in this picture, so it hides the query–key scoring entirely.
  - Real pigments don't blend as a simple weighted average. That sneaks in a mixing behaviour that isn't in the passage.
  - Paint varies in only a few ways (hue, lightness and so on), while the passage doesn't say how many numbers a vector holds.
  - The core idea (shares adding up to 1, blended in proportion) contradicts nothing, so it is not marked misleading.
- **What survives, in plain words:** each token's result is a weighted average of value vectors, with positive weights that add up to 1, so the result leans toward the vectors with the biggest weights.

---

## Step 6: Grade like a stranger (explanation-mode test)

**Picture 1, spotlight.** Already marked misleading at step 4, so it was not regraded.
- Reader-gain sentence: none, because it was discarded at its break point.

**Picture 2, lookup.** **Adds nothing.**
- Strip out the picture-words and what's left is "query and key set the shares; value is what gets blended." That is already in the plain statement, so a reader holding the plain statement could already say it.
- Its only extra content is which token supplies which vector. That comes from the picture, not the passage.
- Other label that fits: **Missing a fact.** The fact is which token supplies the query, which supplies the key, and whose value vectors are mixed. "Adds nothing" comes earlier in the test order, so it wins.

**Picture 3, paint.** **Adds nothing.**
- The plain statement already says "blend in shares that add up to 1," and a reader could already restate that.

**Adds nothing: 2 of 3. Misleading: 1. Not run: 0.**

---

## Step 7: Sort

- **Keep exploring:** empty.
- **Hold:** empty.
- **Discard:** Picture 1, attention as a spotlight. Break point: a spotlight picks a few things and leaves the rest dark, but the passage weighs *every* other token and *blends* the value vectors. Attention here is a blend, not a pick.

**Repeated across pictures, merged here.** "It's a blend, not a pick" appears as the break in Picture 1, as break (a) in Picture 2, and as the core of Picture 3. That point is already in the plain statement.

**Proposed-mechanism section:** skipped. The passage describes a mechanism but doesn't propose a mapping of the form "X works like Y, so build Z."

**Exploratory label:** not required. The topic is not medical, legal, financial, security-related or safety-critical.

Open Mirror ends here. It checked no facts and recommends nothing.

---

## For the student: the passage again, verbatim (technical version)

"In a transformer, attention lets each token weigh every other token in the sequence by computing dot products between query and key vectors, then uses the softmax-normalized weights to mix value vectors."

---

## REPLICATOR NOTES

1. **The stop rule in explanation mode is unclear.** It's not obvious what "the question" is when the request is "explain this." A good plain restatement written for a newcomer is the explanation itself, so in explanation mode the stop rule may fire almost every time. I judged that it fired here.

2. **The stop rule conflicts with the embedded-comparison rule.** Step 1 says a person's own picture must become the first picture tested, "otherwise a person's own picture can never be found misleading." The same step also says "stop, you're done." I resolved it the way the method's first example does: I gave a stop verdict, then ran the pictures "anyway." I invented that resolution. The text doesn't say which rule wins.

3. **Whether the passage contains an embedded comparison was my call.** The passage has no "like." I decided that the borrowed technical names "attention" and "query/key/value" count as embedded pictures, and that "weigh" and "mix" are ordinary words. A different replicator could reasonably decide that names are not comparisons and run three pictures of their own instead.

4. **My rendering of "attention" decided its grade.** I rendered the word as a spotlight, the version the method's own description uses as its example. That made it contradict "every other token" and "mix," so it was marked misleading. A milder version ("how much you notice each thing") would probably have graded as adds nothing. "Only works by contradicting" is hard to apply to a picture that partly works.

5. **Explanation mode doesn't say which step-6 tests change.** It says to swap the decision question for a restatement test. But the decision idea shows up in three places: test 1 ("same call without the picture"), test 4 ("worth exploring"), and the line every non-"adds nothing" picture needs ("the decision it changed"). I swapped all three for "can the reader now restate it." Tests 2 and 3 I applied as written.

6. **The baseline for the restatement test is unclear.** "A reader who couldn't restate the topic before the picture": before means holding the original passage, or holding the plain statement? Because explanation mode outputs the plain statement first, I used the plain statement as the baseline. The result is that a careful plain statement makes almost every picture "adds nothing," and a thin one lets pictures earn credit. Grades depend heavily on how complete the step-1 restatement is. I left the who-supplies-which-vector question explicitly open because the passage leaves it open. If I had filled it in, nothing would change. If I had left it out entirely without flagging it, Picture 2 might have "earned its place."

7. **Line between defining a word and adding a fact.** The method allows defining words but says "add nothing." I had to make several calls:
   - giving "a word" as an example of a token;
   - reading "mix" as a weighted average;
   - stating that softmax shares are positive, add up to 1, and get bigger with higher scores;
   - describing when a dot product is large.

   Each could be called an added fact. I labelled them as definitions or examples.

8. **The method never verifies, and in explanation mode that has a cost.** The passage says "every other token." I kept that wording without comment, because the method forbids checking facts. I'm aware the usual formulation also lets a token weigh itself, and that the passage leaves out other usual details. A newcomer who gets this output inherits any inaccuracy in the source. Explanation mode has no channel for this. (Mentioning it here is itself a fact-check, so I kept it out of the output.)

9. **The changed-decision line contradicts the misleading label.** The method says every picture that isn't "adds nothing" must name the decision it changed, and "if you can't write that sentence, it adds nothing." A misleading picture can't name a changed decision, so taken literally that rule would demote misleading pictures to "adds nothing," against step 4 and step 7. I wrote "none, discarded" and kept it as misleading. It's also unclear whether a picture marked misleading at step 4 gets regraded at step 6. I didn't regrade it.

10. **The pile names fit explanation mode poorly.** "Keep exploring" is the only pile for a picture that "earned its place" as an explanation, and an explanation doesn't need further exploring. It ended up empty here, so it didn't matter, but the mapping is undefined.

11. **"Adds nothing" pictures appear in the count only, which conflicts with showing break points.** Explanation mode says break points matter more because a newcomer can't see them. But "adds nothing" pictures appear in the count only, so their breaks never reach the reader-facing piles. For example, Picture 2's "a lookup picks, attention blends" and Picture 3's "real paint doesn't average." I kept those breaks in the run record above the piles. It's unclear whether that's allowed.

12. **Output order.** "Say which mode you're in at the top" and "output the plain statement first" are slightly in tension. I put the mode line first. I put the full run record between the plain statement and the verbatim original. The method doesn't say where steps 2–7 go in explanation-mode output.

13. **"Handed to someone who doesn't have the original."** I treated the user's "show me the technical version again" as meeting this condition, and ended with the passage verbatim.

14. **The proposed-mechanism trigger is ambiguous.** The section starts on "a mapping: X works like Y, so let's build Z," but its skip condition is "if the topic has no mechanism." This passage describes a mechanism without proposing a mapping. I skipped the section.

15. **Embedded pictures and the three slots.** It's unclear whether embedded pictures use up the three slots, and whether two embedded names in one passage both count as "the first picture." I let both take slots, which left me one free choice (paint).

16. **"Merge duplicates" is underspecified.** It's unclear whether it applies only to pile entries or to observations shared across pictures. The "blend, not pick" point recurred across all three pictures, but only one picture reached a pile. I recorded the merge as a note under the piles.

17. **Step 4 timing.** Step 4 says "before judging anything," but marking a picture misleading at step 4 is itself a judgement. This is minor. I marked it at step 4 as instructed.

18. **The "question it makes easier to ask" has no clear role in explanation mode.** Step 3 requires the question, but in explanation mode it's only used if a picture lands in Keep exploring. Here those questions went unused.
