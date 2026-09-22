---
title: CS846: FMxAI
course: CS 846: FMxAI
instructor: Federico Mora
instructor_url: https://federico.morarocha.ca
university: University of Waterloo
term: Fall '26
schedule: Tues 3:00-5:50pm
---

<!-- slide:title -->
# CS846: FMxAI

---

<!-- slide:content -->
# Syllabus

1. [Syllabus](index.html)
2. [LEARN quiz](https://learn.uwaterloo.ca)

---

<!-- slide:section -->
# Agents and Tool-Use (Sep 22)
`ATU`

---

<!-- slide:paper -->
## LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers

[Olausson et al., EMNLP '23](https://aclanthology.org/2023.emnlp-main.313.pdf)

`ATU`

<figure class="paper-figure paper-figure-large">
  <img src="images/olausson-emnlp-23.png" alt="Diagram of the LINC pipeline: an LLM semantic parser samples logic formulas from a natural-language problem, a theorem prover checks each sample and filters out syntax/semantic errors, and majority voting over the remaining labels produces the final output">
</figure>

---

<!-- slide:paper -->
## Reinforcement Learning from Human Feedback, Chapter 13

[Lambert, Textbook '26](https://rlhfbook.com/c/13-tools)

`ATU` `CONFIRMED`

<figure class="paper-figure">
  <img src="https://rlhfbook.com/c/images/tool_use_generation.png" alt="Diagram of tool use interleaving model generation with external tool execution">
  <figcaption>Figure 1: Tool use interleaves model generation with external execution: the model generates tokens until it emits a tool call (orange), an external system executes the tool and injects the output (purple) into the sequence, and then the model continues generating. Models can emit multiple tool calls in a single generation. During training, tool call and output tokens are typically masked from the loss.</figcaption>
</figure>

---

<!-- slide:paper -->
## Towards Verifiably Safe Tool Use for LLM Agents

[Doshi et al., ICSE-NIER '26](https://dl.acm.org/doi/pdf/10.1145/3786582.3786839)

`ATU`

<figure class="paper-figure">
  <img src="images/doshi-icse-nier-26.png" alt="Example agent conversation where an LLM agent reschedules a meeting and, without being asked, emails the other attendee an explanation that leaks the sensitive reason for the reschedule">
</figure>

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:section -->
# Constraints on LLM Outputs (Sep 29)
`CLO`

---

<!-- slide:paper -->
## How To Generate Text: Using Different Decoding Methods For Language Generation With Transformers

[von Platen, Blog '20](https://huggingface.co/blog/how-to-generate)

`CLO` `CONFIRMED`

<figure class="paper-figure">
  <img src="https://huggingface.co/blog/assets/02_how-to-generate/top_k_sampling.png" alt="Top-K sampling illustrated with two bar charts of word probabilities: the top 6 words after 'The' cover 68% of probability mass, while the top 6 after 'The car' cover 99%, showing that a fixed K can be too small or too large depending on the distribution">
  <figcaption>Example sampling startegy: top-K sampling redistributes probability mass among the K most likely next words, but a fixed K can cut off a flat distribution too early or admit too many words from a peaked one.</figcaption>
</figure>

---

<!-- slide:paper -->
## Constrained Adaptive Rejection Sampling

[Parys et al., ICML '26](https://arxiv.org/pdf/2510.01902)

`CLO`

<div class="figure-row">

<figure class="paper-figure">
  <img src="images/parys-icml-26-ex.png" alt="Example 3.1: a grammar for arithmetic expressions over digits 0 and 1, where strings like 1+0+1 are accepted but 0++ or +1 are not">
</figure>

<figure class="paper-figure">
  <img src="images/parys-icml-26-plot.png" alt="Plot comparing approximation error versus number of samples for CARS against other exact and inexact constrained sampling methods, showing CARS reaches low error with fewer samples than most baselines">
</figure>

</div>

---

<!-- slide:paper -->
## Type-Constrained Code Generation with Language Models

[Mündler et al., PLDI '25](https://dl.acm.org/doi/10.1145/3729274)

`CLO`

<figure class="paper-figure">
  <img src="images/mundler-pldi-26.png" alt="A partial TypeScript program awaiting completion, with five candidate completions shown alongside whether vanilla, syntax-constrained, and type-constrained decoding accept or reject each one; only type-constrained decoding correctly rejects all four invalid completions and accepts the well-formed one">
</figure>

---

<!-- slide:paper -->
## Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages

[Mora et al., NeurIPS '24](https://arxiv.org/pdf/2406.03636)

`CLO`

<figure class="paper-figure">
  <img src="images/mora-neurips-24.png" alt="A desire path meme: a person walks the worn dirt shortcut labeled 'LLM Outputs' instead of the paved path labeled 'Formal Language', illustrating that LLM-generated code naturally drifts toward informal syntax rather than the target formal language">
</figure>

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:section -->
# Generating System Constraints (Oct 06)
`GSC`

---

<!-- slide:paper -->
## Mining Specifications

[Ammons et al., POPL '02](https://haoxintu.github.io/files/10-Mining%20specifications.pdf)

`GSC`

<figure class="paper-figure">
  <img src="images/ammons-popl-02.png" alt="Problem 2.1: given an unlabelled training set of interaction traces with an API or ADT, find an automaton that generates exactly the correct traces; this automaton is called a specification, and an algorithm that finds it is called a specification miner">
</figure>

---

<!-- slide:paper -->
## Learning Context-Free Grammars for Grammar-Constrained Decoding via Declarative Agentic Programming with Guarantees

[Cheang et al., arXiv '26](https://arxiv.org/abs/2608.05493)

`GSC`

<figure class="paper-figure">
  <img src="images/cheang-arxiv-26.png" alt="Autogrammar's two-phase pipeline: in the learning phase, execution logs and API documentation are used to produce a context-free grammar for the target DSL; in the deployment phase, a downstream LM uses the grammar through a validator to generate correct DSL programs in response to natural-language tasks">
</figure>

---

<!-- slide:paper -->
## A Neurosymbolic Approach to Natural Language Formalization and Verification

[An et al., CAV '26](https://link.springer.com/chapter/10.1007/978-3-032-32526-6_28)

`GSC`

<figure class="paper-figure paper-figure-large">
  <img src="images/an-cav-26.png" alt="End-to-end architecture of ARC: a Policy Model Creator autoformalizes a natural-language policy document into a policy model, refines it via test-case enumeration, conflict detection, and user feedback, and an Answer Verifier autoformalizes a question-and-answer conversation, aggregates logical equivalence, and checks it against the policy model with an SMT solver">
</figure>

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:section -->
# Satisfiability (Modulo Theories) (Oct 20)
`SAT`

---

<!-- slide:paper -->
## Introduction to Neural Network Verification, Chapters 4, 6 (7 optional)

[Albarghouthi, Textbook '26](https://verifieddeeplearning.com/nnv_book.pdf)

`SAT` `CONFIRMED`

<div class="figure-column">

<figure class="paper-figure figure-narrow">
  <img src="images/albargouthi-textbook-1.png" alt="Chapter 4 title banner: Logics and Satisfiability">
</figure>

<figure class="paper-figure figure-narrow">
  <img src="images/albargouthi-textbook-2.png" alt="Chapter 6 title banner: DPLL Modulo Theories">
</figure>

</div>

---

<!-- slide:paper -->
## Guiding High-Performance SAT Solvers with Unsat-Core Predictions

[Selsam and Bjørner, SAT '19](https://arxiv.org/pdf/1903.04671)

`SAT`

> The _NeuroSAT_ neural network architecture was introduced in [37] for
> predicting properties of propositional formulae. When trained to predict the
> satisfiability of toy problems, it was shown to find solutions and
> unsatisfiable cores on its own. However, the authors saw "no obvious path" to
> using the architecture to improve the state-of-the-art. In this work, we train
> a simplified NeuroSAT architecture to directly predict the unsatisfiable cores
> of real problems. We modify several high-performance SAT solvers to
> periodically replace their variable activity scores with NeuroSAT’s prediction
> of how likely the variables are to appear in an unsatisfiable core.

In short, 

> ... we use it to help inform variable branching decisions within
> high-performance SAT solvers on real problems.

---

<!-- slide:paper -->
## Learning to Solve SMT Formulas

[Balunović et al., NeurIPS '18](https://www.sri.inf.ethz.ch/publications/balunovic2018learnsmt)

`SAT`

<div class="figure-column">

<figure class="paper-figure">
  <img src="images/balunovic-neurips-18-1.png" alt="Search tree over tactic applications: starting from formula phi, each transformation (tactic) branches into new formulas, some of which time out and others of which are solved quickly, illustrating the need to choose tactics wisely">
</figure>

<figure class="paper-figure">
  <img src="images/balunovic-neurips-18-2.png" alt="The action space of available tactics, including constant folding, normalizing bounds, bit blasting, and calling a decision procedure over reals, integers, or bitvectors">
</figure>

</div>

---

<!-- slide:paper -->
## SATzilla: Portfolio-based Algorithm Selection for SAT

[Xu et al., JAIR '08](https://arxiv.org/abs/1111.2249)

`SAT`

> It has been widely observed that there is no single "dominant" SAT solver; instead, different
> solvers perform best on different instances. Rather than following the traditional approach
> of choosing the best solver for a given class of instances, we advocate making this decision
> online on a per-instance basis.

<figure class="paper-figure">
  <img src="https://2020blogfor.github.io/images/blog_images/sat/onlinechart.png" alt="Flowchart of SATzilla's online phase: select a SAT instance from test data, compute features, use hardness models to predict algorithm runtimes, run the predicted fastest algorithm, and return the result">
  <figcaption>Source: Costa, Natarajan, Rosa, Shao, and Zhai, <a href="https://2020blogfor.github.io/posts/2020/04/sat/">"SATzilla"</a>, Blog '20.</figcaption>
</figure>

---

<!-- slide:paper -->
## MedleySolver: Online SMT Algorithm Selection

[Pimpalkhare et al., SAT '21](https://www.pure.ed.ac.uk/ws/files/248374419/MedleySolver_PIMPALKHARE_DOA05072021_AFV.pdf)

`SAT`

<figure class="paper-figure">
  <img src="images/pimpalkhare-sat-21.png" alt="Pipeline diagram: queries from SMT-enabled tools like UCLID5, KLEE, and the Rosette language are streamed into MedleySolver, which learns online and outputs SAT/UNSAT for each query">
</figure>

> SMT users rarely aim to solve a single query in isolation and usually care
> about [total] resource consumption. For example, verification engines generate many
> verification queries for one verification problem and aim to solve these
> queries in the least amount of time.

---

<!-- slide:paper -->
## Domain-Specific Hyperspecialization (For SAT)

[Green, Blog '26](https://c.mov/lymphosat/)

`SAT`

<figure class="paper-figure paper-figure-large">
  <img src="images/green-blog-26.png" alt="Satirical diagram mapping four NP-hard problems (graph coloring, bin packing, set cover, SAT) each to its own bespoke custom solver, instead of reducing them all to a single general SAT solver">
</figure>

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:section -->
# Program Verification (Oct 27)
`PVE`

---

<!-- slide:paper -->
## Getting Started with Dafny: A Guide

[Leino, Textbook '23](https://dafny.org/latest/OnlineTutorial/guide)

`PVE` `CONFIRMED`

<figure class="paper-figure paper-figure-large">
  <img src="images/leino-textbook-23.png" alt="Dafny code for binary search: a sorted predicate and a BinarySearch method with requires/ensures contracts and a while loop annotated with invariants, verified statically against the specification">
</figure>

---

<!-- slide:paper -->
## AutoVerus: Automated Proof Generation for Rust Code

[Yang et al., OOPSLA '25](https://dl.acm.org/doi/full/10.1145/3763174)

`PVE`

<figure class="paper-figure paper-figure-large">
  <img src="images/yang-oopsla-25.png" alt="A Rust count_digits function alongside its Verus spec functions, with the proof annotations (loop invariants and asserts) needed to verify the implementation against the specification highlighted separately from the specification itself">
</figure>

---

<!-- slide:paper -->
## VERINA: Benchmarking Verifiable Code Generation

[Ye et al., ICLR '26](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b8c80f9113b9f8e2e129447221682a-Abstract-Conference.html)

`PVE`

> Verifiable code generation—jointly generating code, specifications, and
> proofs of code-specification alignment—offers a promising path to address this
> limitation and further unleash LLMs’ benefits in coding. Yet, there exists a
> significant gap in evaluation: current benchmarks often focus on only
> individual components rather than providing a holistic evaluation framework of
> all tasks.

But proof success is quite low:

> The best model, OpenAI o3, achieves a 72.6% code correctness rate,
> 52.3% for specification soundness and completeness, and a mere 4.9% proof success 
> rate (based on one trial per task).

---

<!-- slide:paper -->
## Large Language Model Powered Symbolic Execution

[Li et al., OOPSLA '25](https://doi.org/10.1145/3763163)

`PVE`

<figure class="paper-figure paper-figure-large">
  <img src="images/li-oopsla-25.png" alt="Example workflow: source code is parsed into an AST, a path slice is generated and rendered back into source, then an LLM is prompted with a pre-condition, the slice, and a post-condition to decide whether the post-condition holds along that path, passing or failing accordingly">
</figure>

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:section -->
# Superoptimization (Nov 10)
`SUP`

---

<!-- slide:paper -->
## Program Synthesis is Possible

[Sampson, Blog '18](https://www.cs.cornell.edu/~asampson/blog/minisynth.html)

`SUP`

> you have the "slow" expression `x * 2`, and you know that there's a "faster"
> version to be had that can be written `x << ??` for some value of `??`. 
> Let's ask Z3 what to write there...

---

<!-- slide:paper -->
## Stochastic Superoptimization

[Schkufza et al., ASPLOS '13](https://dl.acm.org/doi/10.1145/2490301.2451150)

`SUP`

<figure class="paper-figure paper-figure-large">
  <img src="images/schkufza-asplos-13.png" alt="Cycling Through 3 Values benchmark: gcc -O3 translates the esoteric bit-twiddling implementation almost literally into assembly, while STOKE rediscovers the intuitive algorithm using conditional move instructions in far fewer instructions">
</figure>

---

<!-- slide:paper -->
## Faster Sorting Algorithms Discovered Using Deep Reinforcement Learning

[Mankowitz et al., Nature '23](https://www.nature.com/articles/s41586-023-06004-9)

`SUP`

<figure class="paper-figure paper-figure-large">
  <img src="images/mankowitz-nature-23.png" alt="Diagram of the AssemblyGame: AlphaDev selects an assembly instruction to append to the algorithm being built, then all test input sequences are run through the algorithm and the outputs are compared against expected outputs to compute a correctness-based reward">
</figure>

---

<!-- slide:paper -->
## Mathematical Discoveries from Program Search with Large Language Models

[Romera-Paredes et al., Nature '23](https://www.nature.com/articles/s41586-023-06924-6)

`SUP`

<figure class="paper-figure paper-figure-large">
  <img src="images/romera-paredes-nature-23.png" alt="Diagram of the FunSearch loop: a specification and prompt built from high-scoring programs sampled from a programs database are fed to a pretrained LLM, which generates new programs that are evaluated and, if correct, stored back in the programs database, with the highest-scoring program retrievable at any point">
  <figcaption>Overview of FunSearch. The input to FunSearch is a specification of the problem in the form of an 'evaluate' function, an initial implementation of the function to evolve, which can be trivial, and potentially a skeleton. At each iteration, FunSearch builds a prompt by combining several programs sampled from the programs database (favouring high-scoring ones). The prompt is then fed to the pretrained LLM and new programs are created. Newly created programs are then scored and stored in the programs database (if correct), thus closing the loop. The user can at any point retrieve the highest-scoring programs discovered so far.</figcaption>
</figure>

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:section -->
# Theorem Proving (Nov 17)
`TPR`

---

<!-- slide:paper -->
## Generative Language Modeling for Automated Theorem Proving

[Polu and Sutskever, arXiv '20](https://arxiv.org/abs/2009.03393)

`TPR`

> We present an automated prover and proof assistant, GPT-f, for the Metamath
> formalization language, and analyze its performance. GPT-f found new short
> proofs that were accepted into the main Metamath library, which is to our
> knowledge, the first time a deep learning based system has contributed proofs
> that were adopted by a formal mathematics community.

---

<!-- slide:paper -->
## Hilbert: Recursively Building Formal Proofs with Informal Reasoning

[Varambally et al., ICLR '26](https://openreview.net/pdf?id=GN8OdkTo3B)

`TPR`

<figure class="paper-figure paper-figure-large">
  <img src="images/varambally-iclr-26.png" alt="Diagram of the Hilbert algorithm: given a target theorem, a prover attempts formal proof generation; on failure the theorem is decomposed into subgoal theorems that are each retried with the prover and a reasoner (shallow solve), recursing into further decomposition until all subgoals are resolved">
</figure>

---

<!-- slide:paper -->
## Postmortem for Kernel Soundness Bug #14576

[de Moura, Blog '26](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/)

`TPR`

> On July 25, Ramana Kumar published a repository containing a `sorry`-free
> "disproof" of the Collatz conjecture, produced with AI assistance. It is not a
> valid proof because it exploits a bug in the kernel's handling of nested
> inductive types.

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:section -->
# Machine-Learning Verification (Nov 24)
`MLV`

---

<!-- slide:paper -->
## Introduction to Neural Network Verification, Chapters 1, 2, 3, 5

[Albarghouthi, Textbook '26](https://verifieddeeplearning.com/nnv_book.pdf)

`MLV` `CONFIRMED`

> This book is about verifying that a neural network behaves according to some
> set of desirable properties.

Importantly, 

> A number of people in the verification community, the author included, argue
> that specification [deciding on the set of desirable properties] is harder than
> verification---that is, the hard part is asking the right questions!

---

<!-- slide:paper -->
## VNN-LIB 2.0: Rigorous Foundations for Neural Network Verification

[Roy et al., CAV '26](https://arxiv.org/pdf/2605.07451)

`MLV`

```
(vnnlib-version <2.0>)

; Network declaration
(declare-network f
    (declare-input  X float32 [2,2])
    (declare-output Y float32 [1])
)

; Input constraints
(assert (and (>= X[0,0] 0.0) (<= X[0,0] 1.0)))
(assert (and (>= X[0,1] 0.0) (<= X[0,1] 1.0)))
(assert (and (>= X[1,0] 0.0) (<= X[1,0] 1.0)))
(assert (and (>= X[1,1] 0.0) (<= X[1,1] 1.0)))

; Output constraints
(assert (or (<= Y[0] -3.0) (>= Y[0] 0.0)))
```

---

<!-- slide:paper -->
## Beta-CROWN: Efficient Bound Propagation with Per-neuron Split Constraints for Complete and Incomplete Neural Network Robustness Verification

[Wang et al., NeurIPS '21](https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html)

`MLV`

<figure class="paper-figure paper-figure-large">
  <img src="https://camo.githubusercontent.com/f9399e783288dfcf70f7467159c13fb5dfb2ce6a0bba3663d0bdf36f6769c6cf/68747470733a2f2f7777772e6875616e2d7a68616e672e636f6d2f696d616765732f75706c6f61642f616c7068612d626574612d63726f776e2f6c6f676f5f323032322e706e67" alt="The αβ-CROWN logo: a crown badge reading 'winner of International Verification of Neural Networks Competitions (VNN-COMP 2021-2025)'">
</figure>

---

<!-- slide:section -->
# Bonus or Guest Talks (Dec 01)

---

<!-- slide:content -->
# Speed Matching <svg class="lightning" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2v11h3v9l7-12h-4l4-8z"/></svg>

- Find a pair (30 seconds)
- Describe a research project that you have worked on or that you would like to work on (1 minute)
- Listen to a research project that your pair has worked on or would like to work on (1 minute)
- Brainstorm with your pair on a project that you could work on together (2 minutes)
- Find a new pair (30 seconds) and repeat

---

<!-- slide:content -->
# References

- Seshia, S. A. (2024). *EECS 219C: Formal methods: Specification,
  verification, and synthesis* [Course website](https://people.eecs.berkeley.edu/~sseshia/219c/spr24/). University of California,
  Berkeley.
- Chasins, S. E. (2024). *CS 294-184: Building user-centered programming
  tools* [Course website](https://schasins.com/cs294-usable-programming-2024/). University of California, Berkeley.
- Willsey, M. (2024). *CS 294-260: Declarative program analysis and
  optimization* [Course website](https://inst.eecs.berkeley.edu/~cs294-260/sp24/). University of California, Berkeley.
- Artificial Intelligence Tool(s): Claude (Sonnet 5), Anthropic;
  Writing: Claude was used to fix spelling and grammatical mistakes in the syllabus; 
  Project Administration: Claude was used to build and maintain Markdown-to-HTML
  scripts and keep the Schedule and Reading Bank tables in sync.