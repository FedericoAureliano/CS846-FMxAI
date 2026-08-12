---
title: CS846: FMxAI
course: CS 846: FMxAI
instructor: Federico Mora
instructor_url: https://federico.morarocha.ca
university: University of Waterloo
term: Fall '26
schedule: Tues 3:00-5:50pm
location: DC 2585
---

<!-- slide:title -->
# CS846: FMxAI

---

<!-- slide:content -->
# Grading

Our meetings will be centered around paper discussions. Attendance, reading of assigned papers, and participation are essential.

- 20% participation
- 30% discussion leads
- 50% project

---

<!-- slide:content -->
# Project

Every project must contain new research — a new idea or insight — and an element of both formal methods and artificial intelligence. Students can work in groups of up to three.

1. Proposal — problem definition and a brief literature survey; at most one page.
2. Mini presentation — proposal recap, status update, and timeline; at most 10 minutes.
3. Final presentation — updated problem definition, literature survey, and results; at most 20 minutes.
4. Report — a conference paper-style write-up.

---

<!-- slide:content -->
# Paper Discussions

- Every student picks and presents two papers, each from a different theme.
- Each paper-discussion day pairs two assigned readings with two student-led presentations.
- Come having read the assigned papers, ready to engage respectfully with your peers' work.

---

<!-- slide:content -->
# Schedule

| Date | Description | Read |
| --- | --- | --- |
| Sep 15 | Introduction and overview | [1](overview-slides.html) |
| **Sep 16** | **Reading preferences due** | |
| Sep 22 | Agents and tool-use **ATU** | TBD |
| Sep 29 | Constraints on LLM outputs **SSC** | TBD |
| Oct 06 | Learning constraints from data **LCD** | TBD |
| **Oct 09** | **Proposals due** | |
| ~~Oct 13~~ | ~~Reading week~~ | |
| Oct 20 | Autoformalization **AUF** | TBD |
| Oct 27 | Program analysis **PRA** | TBD |
| _Nov 03_ | _Mini presentations day_ | |
| Nov 10 | Satisfiability (modulo theories) **SAT** | TBD |
| Nov 17 | Theorem proving **TPR** | TBD |
| Nov 24 | Superoptimization **SUP** | TBD |
| Dec 01 | Bonus (**NSP**, **MLV**, **PRP**, or **TST**) | TBD |
| _Dec 08_ | _Final presentations day_ | |
| **Dec 18** | **Reports due** | |

---

<!-- slide:section -->
# Agents and Tool-Use
`ATU`

Next token prediction plus a harness for tool calling.

---

<!-- slide:paper -->
## LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers

[Olausson et al., EMNLP '23](https://aclanthology.org/2023.emnlp-main.313.pdf)

`ATU` `AUF`

---

<!-- slide:paper -->
## Learning Context-Free Grammars for Grammar-Constrained Decoding via Declarative Agentic Programming with Guarantees

[Cheang et al., Arxiv '26](https://arxiv.org/abs/2608.05493)

`ATU` `LCD` `AUF`

---

<!-- slide:paper -->
## Reinforcement Learning from Human Feedback, Chapter 13

[Lambert, Textbook '26](https://rlhfbook.com/c/13-tools)

`ATU`

---

<!-- slide:section -->
# Constraints on LLM Outputs
`SSC`

Techniques for constraining what a language model can generate so its output is syntactically or semantically valid by construction.

---

<!-- slide:paper -->
## How To Generate Text: Using Different Decoding Methods For Language Generation With Transformers

[von Platen, Blog '20](https://huggingface.co/blog/how-to-generate)

`SSC`

---

<!-- slide:paper -->
## PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models

[Scholak et al., EMNLP '21](https://aclanthology.org/2021.emnlp-main.779/)

`SSC`

---

<!-- slide:paper -->
## Grammar Prompting for Domain-Specific Language Generation with Large Language Models

[Wang et al., NeurIPS '23](https://arxiv.org/pdf/2305.19234)

`SSC`

---

<!-- slide:paper -->
## Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages

[Mora et al., NeurIPS '24](https://arxiv.org/pdf/2406.03636)

`AUF` `SSC` `PRP`

---

<!-- slide:paper -->
## Constrained Adaptive Rejection Sampling

[Parys et al., ICML '26](https://arxiv.org/pdf/2510.01902)

`SSC`

---

<!-- slide:paper -->
## ChopChop: A Programmable Framework for Semantically Constraining the Output of Language Models

[Nagy et al., POPL '26](https://arxiv.org/pdf/2509.00360)

`SSC`

---

<!-- slide:section -->
# Learning Constraints from Data
`LCD`

Inferring specifications, invariants, models or other formal artifacts automatically from examples or execution traces.

---

<!-- slide:paper -->
## Learning Regular Sets from Queries and Counterexamples

[Angluin, I&C '87](https://swt.informatik.uni-freiburg.de/teaching/WS2019-20/AutomataTheory/Learning%20Automata%20%28Caveat%20not%20related%20to%20Machine%20Learning?month:int=4&year:int=2025&orig_query=)

`LCD`

---

<!-- slide:paper -->
## Mining Specifications

[Ammons et al., POPL '02](https://haoxintu.github.io/files/10-Mining%20specifications.pdf)

`LCD`

---

<!-- slide:paper -->
## Learning Concise Models from Long Execution Traces

[Jeppu et al., DAC '20](https://arxiv.org/abs/2001.05230)

`LCD`

---

<!-- slide:paper -->
## LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference

[Wu et al., ASE '24](https://dl.acm.org/doi/10.1145/3691620.3695014)

`LCD` `PRA`

---

<!-- slide:paper -->
## Specgen: Automated Generation Of Formal Program Specifications Via Large Language Models

[Ma et al., ICSE '25](https://dl.acm.org/doi/10.1109/ICSE55347.2025.00129)

`AUF` `LCD`

---

<!-- slide:paper -->
## Let a Neural Network Be Your Invariant

[Giacobbe et al., NeurIPS '25](https://openreview.net/forum?id=qBPb7g1SEa)

`LCD` `PRA`

---

<!-- slide:section -->
# Autoformalization
`AUF`

Translating informal, natural-language mathematics and specifications into formal, machine-checkable statements.

---

<!-- slide:paper -->
## A Neurosymbolic Approach to Natural Language Formalization and Verification

[An et al., CAV '26](https://link.springer.com/chapter/10.1007/978-3-032-32526-6_28)

`AUF`

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
# Program Analysis
`PRA`

Formally analyzing programs

---

<!-- slide:paper -->
## Large Language Model Powered Symbolic Execution

[Li et al., OOPSLA '25](https://doi.org/10.1145/3763163)

`PRA`

---

<!-- slide:paper -->
## Agentic Verification of Software Systems

[Tu et al., FSE '26](https://arxiv.org/abs/2511.17330)

`PRA`

---

<!-- slide:section -->
# Satisfiability (Modulo Theories)
`SAT`

Algorithms and heuristics for deciding the satisfiability of logical formulas.

---

<!-- slide:paper -->
## SATzilla: Portfolio-based Algorithm Selection for SAT

[Xu et al., JAIR '08](https://arxiv.org/abs/1111.2249)

`SAT`

---

<!-- slide:paper -->
## Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks

[Katz et al., CAV '17](https://link.springer.com/chapter/10.1007/978-3-319-63387-9_5)

`MLV` `SAT`

---

<!-- slide:paper -->
## Learning to Solve SMT Formulas

[Balunović et al., NeurIPS '18](https://www.sri.inf.ethz.ch/publications/balunovic2018learnsmt)

`SAT`

---

<!-- slide:paper -->
## Guiding High-Performance SAT Solvers with Unsat-Core Predictions

[Selsam and Bjørner, SAT '19](https://link.springer.com/chapter/10.1007/978-3-030-24258-9_24)

`SAT`

---

<!-- slide:paper -->
## MedleySolver: Online SMT Algorithm Selection

[Pimpalkhare et al., SAT '21](https://www.pure.ed.ac.uk/ws/files/248374419/MedleySolver_PIMPALKHARE_DOA05072021_AFV.pdf)

`SAT`

---

<!-- slide:paper -->
## Domain-Specific Hyperspecialization (For SAT)

[Green, Blog '26](https://c.mov/lymphosat/)

`SAT`

---

<!-- slide:section -->
# Theorem Proving
`TPR`

Automating the search for formal proofs

---

<!-- slide:paper -->
## Generative Language Modeling for Automated Theorem Proving

[Polu and Sutskever, arXiv '20](https://arxiv.org/abs/2009.03393)

`TPR`

---

<!-- slide:paper -->
## HyperTree Proof Search for Neural Theorem Proving

[Lample et al., NeurIPS '22](https://proceedings.neurips.cc/paper_files/paper/2022/hash/a8901c5e85fb8e1823bbf0f755053672-Abstract-Conference.html)

`TPR`

---

<!-- slide:paper -->
## Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving

[ByteDance, Arxiv '25](https://arxiv.org/pdf/2507.23726)

`TPR`

---

<!-- slide:section -->
# Superoptimization
`SUP`

Improving (usually in terms of speed) programs by searching the space of equivalent programs.

---

<!-- slide:paper -->
## Stochastic Superoptimization

[Schkufza et al., ASPLOS '13](https://dl.acm.org/doi/10.1145/2490301.2451150)

`SUP`

---

<!-- slide:paper -->
## Learning to Superoptimize Programs

[Bunel et al., ICLR '17](https://arxiv.org/abs/1612.01094)

`SUP`

---

<!-- slide:section -->
# Neuro-symbolic Programming
`NSP`

Programming languages and systems that combine neural components with symbolic, logical reasoning.

---

<!-- slide:paper -->
## DeepProbLog: Neural Probabilistic Logic Programming

[Manhaeve et al., NeurIPS '18](https://proceedings.neurips.cc/paper/2018/hash/dc5d637ed5e62c36ecb73b654b05ba2a-Abstract.html)

`NSP`

---

<!-- slide:paper -->
## Scallop: A Language for Neurosymbolic Programming

[Li et al., PLDI '23](https://dl.acm.org/doi/pdf/10.1145/3591280)

`NSP`

---

<!-- slide:section -->
# Machine-Learning Verification
`MLV`

Formally verifying properties of machine-learned models, such as robustness.

---

<!-- slide:paper -->
## Proving Data-Poisoning Robustness in Decision Trees

[Drews et al., PLDI '20](https://dl.acm.org/doi/10.1145/3385412.3385975)

`MLV`

---

<!-- slide:paper -->
## Beta-CROWN: Efficient Bound Propagation with Per-neuron Split Constraints for Complete and Incomplete Neural Network Robustness Verification

[Wang et al., NeurIPS '21](https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html)

`MLV`

---

<!-- slide:paper -->
## Neural Network Verification with Proof Production

[Isac et al., FMCAD '22](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10026587&casa_token=6jy7_pSgbOwAAAAA:HNny8NVwdhsCPew67iMK2jLHdzqnTfss8SOPuMsrDubYtSQ_Y8IiU8myHghTs7t7MO1ymxzL9Q)

`MLV`

---

<!-- slide:section -->
# Program Repair
`PRP`

Automatically finding and applying fixes to buggy programs.

---

<!-- slide:paper -->
## Automated Repair of Programs from Large Language Models

[Fan et al., ICSE '23](https://dl.acm.org/doi/10.1109/ICSE48619.2023.00128)

`PRP`

---

<!-- slide:section -->
# Testing
`TST`

Automatically generating tests

---

<!-- slide:paper -->
## Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models

[Deng et al., ISSTA '23](https://dl.acm.org/doi/abs/10.1145/3597926.3598067)

`TST`

---

<!-- slide:paper -->
## CODAMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models

[Lemieux et al., ICSE '23](https://www.carolemieux.com/codamosa_icse23.pdf)

`TST`

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
# Reading Preferences (Due Tuesday, September 16)

Email Federico your ranking of 9 papers, one from each of 9 different themes, from most to least preferred. Feel free to use this template.

```
Subject: CS 846 Reading Preferences

Hi Federico,

Here is my ranked list of 9 papers, one from each theme,
from most to least preferred:

1. <Theme> — <Paper Title>
2. <Theme> — <Paper Title>
...
9. <Theme> — <Paper Title>

Thanks,
<Your Name>
```
