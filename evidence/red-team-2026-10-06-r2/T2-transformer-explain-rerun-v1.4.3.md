# T2 rerun (v1.4.3 draft, Opus) — transformer attention, explain for a student

**Case given:** Open Mirror this so a curious high-school student can follow it, then show me the technical version again: "In a transformer, attention lets each token weigh every other token in the sequence by computing dot products between query and key vectors, then uses the softmax-normalized weights to mix value vectors."

**Method text given:** `00b-method-packet-explanation-rerun.md` (v1.4.2 plus the rewritten explanation mode; footer still read v1.4.2).

**Replicator's final message, verbatim:**

---

**Mode: Explanation mode.** The request asks to make the passage followable for a newcomer ("so a curious high-school student can follow it"). It is not asking me to filter a comparison.

---

# Reader output (in the order the method asks for)

## 1. The plain statement

This passage describes one part of a **transformer**, which is a type of AI model. The part is called **attention**. Here "attention" is the name of the specific procedure described below. It doesn't mean attention the way people pay attention.

A few words first:
- **Token:** one item in a sequence (a line of items in order). In language models a token is usually a word or a piece of a word.
- **Vector:** a list of numbers.
- **Query, key, value:** in this step each token has three such lists. The passage names them but doesn't say where they come from.
- **Dot product:** take two lists of the same length, multiply them position by position, and add up all the results. You get one number. It is large when both lists have big numbers with the same sign in the same positions.
- **Softmax:** a rule that turns a set of scores into weights. The weights are all positive and add up to 1, and bigger scores get bigger shares.
- **"Weigh"** here means "give a weight to", a number saying how much. It doesn't mean judging how heavy something is.

What the passage says happens:
1. Take one token. Compare its query with the key of every other token in the sequence using a dot product. That gives one score per other token.
2. Run those scores through softmax. Now you have weights that add up to 1.
3. Multiply each other token's value list by its weight, then add all those lists together. The result is a blend (the passage says "mix") of the value lists.
4. Every token does this.

The passage states this as a flat description. It has no hedges or guesses. It doesn't say what happens to the blended result afterwards.

## 2. Pictures in Use

### Picture A: A library where you take a bit of every book

Imagine you walk into a library with a question (your **query**). Every book has a label on its spine (its **key**) and something written inside (its **value**). You check how well each label matches your question (the **dot product score**). Then, instead of borrowing only the best-matching book, you copy a little from *every* book. You copy more from books whose labels matched better (the **softmax weights**), and you combine what you copied into one set of notes (the **mixed value**). In a transformer, every token is a visitor with a question, and every token is also a book on the shelf.

What it helps you see: each token plays three separate roles. It has something it is looking for (query), something it can be found by (key), and something it hands over when it is found (value). Only the query and key decide the scores, and only the value ends up in the blend.

**Where this picture breaks:**
- A real library hands you whole books. Here every book contributes a fraction, and none is picked outright.
- A real library has one visitor at a time. Here every token is searching and being searched at once.
- In a library, people wrote the labels and contents on purpose and understand them. The passage only says the matching is a dot product between lists of numbers. Nothing in it says anyone "understands" the question.
- The picture puts your own book on the shelf too. The passage says "every other token", so it doesn't settle whether a token also weighs itself.
- The picture suggests someone made the labels. The passage doesn't say where queries, keys or values come from.

### Picture B: A weighted class grade

Your final grade in a class might be 50% exams, 30% homework and 20% projects. Each part has a score, and the percentages add up to 100%. The final grade is a blend: no single part is copied over, and each counts by its share. Attention's last step works the same way. The value lists are the parts, the softmax weights are the percentages (they add up to 1, which is 100%), and the mixed result is the "final grade".

What it helps you see: the output for each token is a weighted average of the value lists. The weights are positive and add up to 1, so the result is a blend rather than a copy of any one value.

**Where this picture breaks:**
- A teacher sets class percentages once, in the syllabus. In attention the weights are worked out fresh for each token from its query-key scores, so each token gets a different "syllabus".
- A grade is one number. Here each "part" is a whole list of numbers, blended position by position.
- A teacher decides the percentages. In attention, softmax applied to the dot-product scores produces them.

## 3. The technical version again (original passage, word for word)

"In a transformer, attention lets each token weigh every other token in the sequence by computing dot products between query and key vectors, then uses the softmax-normalized weights to mix value vectors."

---

# Run record (steps 1 to 7)

**Step 1: Say it plainly.** See the plain statement above. The passage contains no comparison that the person is using to make an argument. "Attention" is a term of art (the method's own example), so I defined it and kept it. "Weigh" and "mix" are ordinary descriptive verbs here, not pictures being argued from, so I defined them and kept them. There were no instructions aimed at me in the material. Explanation mode means I don't stop at step 1.

**Step 2: Pictures chosen (3).**
- A. Library with soft borrowing. Kind of relationship: matching and retrieval. It shows the three separate roles.
- B. Weighted class grade. Kind of relationship: proportion and blending. It shows the weights summing to one.
- C. Spotlight ("attention is like a spotlight on the important word"). Kind of relationship: selection. This is the picture most often used for this topic, so I tested it.

**Step 3: Mapping.**
- A. Question → query; spine label → key; book contents → value; how well label matches question → dot product; copy-more-from-better-matches → softmax weights; combined notes → mixed value. *Question it makes easier to ask:* why does each token need a key separate from its value, so that it is matched on one list but hands over another?
- B. Assignment scores → value lists; percentages → softmax weights; percentages add to 100% → weights add to 1; final grade → mixed value. *Question it makes easier to ask:* what happens to the blend when one score is far bigger than the rest, compared with when all scores are close?
- C. Beam → attention weights; lit area → heavily weighted tokens; dark area → ignored tokens. *Question it makes easier to ask:* which single token is each token looking at?

**Step 4: Where each breaks.**
- A. Break points as listed above. It brings in two facts as open questions rather than as givens: whether a token weighs itself, and who or what makes the keys and values. The picture's main point (three separate roles) doesn't depend on either. Not misleading.
- B. Break points as listed above. It brings in "weights are fixed in advance", which conflicts with the stated "computing dot products… softmax-normalized weights". But the picture's main point (a weighted average whose weights sum to one) doesn't rely on that. Not misleading.
- C. A spotlight lights one region and leaves the rest dark. The passage says each token weighs *every* other token and mixes value vectors, so the result is a blend over all of them, not one lit region. The spotlight also implies a single viewer and treats "importance" as a property of the lit token. The passage makes each weight depend on a pair (one token's query with another's key), and every token does this at once. The picture's takeaway only works by contradicting "every other token… mix". **Marked misleading here.** It skips steps 5 and 6 and goes to Discard.

**Step 5: What survives, in plain words.**
- A. Each token has three separate lists: one for what it is looking for, one for what it can be matched against, and one for what it contributes. The scores use only the first two, and only the third appears in the output.
- B. The output for each token is a weighted average of all the value lists, with positive weights that add up to one, so it is a blend rather than a copy of any single value.
- C. Skipped (misleading).

**Step 6: Graded like a stranger, using the explanation-mode test.**
- A. Adds nothing? A newcomer holding only the original passage could not restate in plain words what "query", "key" and "value" are for. After this picture they could say "each word asks with one list, gets found by another, and hands over a third." The picture earns its place. Two readings? No. Missing a fact? The open question of where the lists come from doesn't stop the picture from helping, so this label doesn't fit. → **Use.** *Restatement it enables:* "Each token is matched using its query and the others' keys, and receives a blend of the others' values."
- B. Adds nothing? A newcomer could not restate "uses the softmax-normalized weights to mix value vectors" unaided. After this picture they could say "it takes a weighted average where the weights add to 100%." The picture earns its place. Two readings? No. Missing a fact? No. → **Use.** *Restatement it enables:* "The output is a weighted average of the value lists, with the weights summing to one." It partly overlaps with A, since both convey "a blend, not a pick". A's distinctive part is the three roles and B's is that the weights sum to one, so I did not merge them.
- C. Not graded (misleading).

**Count:** Adds nothing: 0 of 3. Misleading: 1. Not run: 0.

**Step 7: Piles.**
- **Use:** A (library with soft borrowing) and B (weighted class grade), each shown above with its break point.
- **Hold:** empty.
- **Discard:** C (spotlight). Break point: it only works by showing one lit region with the rest dark, which contradicts the passage's "weigh every other token" and "mix value vectors". It also hides that each weight depends on a pair of tokens and that every token does this at once.

**Proposed-mechanism section:** skipped. The passage describes how something works but doesn't bring an "X works like Y, so build Z" mapping. There is also nothing in Keep exploring or Hold.

**Exploratory label:** not required (not a medical, legal, financial, security or safety topic).

Open Mirror ends here.

---

# REPLICATOR NOTES

1. **Version mismatch.** The file name says v1.4.3, but the footer says v1.4.2 and states that "the v1.4.2 wording fixes are untested." I couldn't tell which version I was actually running.
2. **Where the run record goes in explanation mode.** The method fixes the output order as plain statement → Use pictures with break points → original passage word for word. It doesn't say where the step-by-step working, the count line, Hold or Discard go. It says "the count line stays the same" but not where to put it. I invented a layout: reader output first in the prescribed order, then a separate run record.
3. **The "decision it changed" sentence in explanation mode.** Step 6 requires every non-"adds nothing", non-misleading picture to name in one sentence the decision it changed. Explanation mode replaces the decision test with a restatement test but doesn't say whether that sentence requirement still applies. I invented a substitute: a "restatement it enables" sentence.
4. **How the four labels map to Use.** In explanation mode, Use is for pictures that "earned their place", but step 6 still lists Adds nothing / Two readings / Missing a fact / Worth exploring, and earlier labels win. Taken strictly, any picture that raises an unanswered fact (A raises "where do queries/keys/values come from?") could be pushed into Hold ahead of Use. I invented a rule: "Missing a fact" applies only if the picture needs that fact in order to help.
5. **The restatement test is a judgement call.** "Could a newcomer holding only the original restate it?" means imagining a hypothetical high-school student, so the outcome rests on my guess. It's also unclear whether to judge each picture in isolation or cumulatively, and whether to let the newcomer see the step-1 definitions. I judged each picture in isolation, against the original only.
6. **"Add nothing" versus the definitions a newcomer needs.** A plain statement a high-school student can follow needs definitions that aren't in the passage: vector, dot product, softmax (positive weights summing to 1), and token ("usually a word or part of a word"). The method allows defining words but not adding facts, and the line between the two is unclear. I treated these as definitions. "Usually a word or part of a word" is arguably an added fact.
7. **Reading choices in step 1.** Two places needed interpretation:
   - *Whose query meets whose key.* The passage doesn't say outright that the weighing token's query is compared with the other tokens' keys. I took that as the natural reading rather than raising "two readings".
   - *"Every other token."* This literally excludes the token itself. I kept it literal and noted it only as a break point in Picture A.
8. **The method can't catch simplifications in the source.** Because it forbids checking facts, the explanation inherits whatever the passage leaves out. From background knowledge, standard attention usually includes the token itself, often uses masking, scales scores before softmax, and uses multiple heads. None of that is in the passage, so none of it appears in the output.
9. **Choosing a picture likely to fail.** I chose the spotlight partly because it is the common picture and newcomers benefit from seeing where it lies. The method says three is "a ceiling, not a quota" and warns against padding, so including a likely-misleading picture is a judgement the method neither endorses nor forbids. Marking it misleading ("only works by contradicting") was also a judgement: a graded "many dimmer switches" version might have survived. I didn't run that version, and it isn't counted under "Not run", which only covers pictures the person named.
10. **Spotting comparisons inside the passage.** "Weigh" and "mix" are mildly figurative. The method only says to pull out comparisons "the person is using to argue", and it treats terms of art as words, not pictures. I decided the passage contains none, but the line between a figurative verb and an embedded picture isn't defined.
11. **What step 4 compares against.** Step 4 says to name facts the picture sneaks in "that weren't in the plain statement". Explanation mode says never to compare a picture against the plain statement, though only for step 6. I used the plain statement in step 4 and the original in step 6. Because my plain statement contains definitions I added, this changes what counts as "sneaked in".
12. **Partial overlap between pictures.** "Merge duplicates and name both" doesn't cover pictures that only partly overlap, as A and B do on "a blend, not a pick". I kept them separate and noted the overlap.
13. **When the proposed-mechanism section applies.** Its trigger is unclear. The passage describes a mechanism, but the section title says "proposed mechanism" and the text says the person brings "a mapping". It also says "if the topic has no mechanism, skip". I skipped it because there was no mapping, and in any case nothing landed in Keep exploring or Hold, which are the piles it refers to in filter mode.
14. **"Show me the technical version again"** I mapped onto the method's required "original passage word for word". The method doesn't say whether a user's extra request should replace or add to that step. Here they matched, so no rule was needed.
