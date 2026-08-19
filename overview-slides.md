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

1. Proposal (due Oct 09) — problem definition and a brief literature survey; at most one page.
2. Mini presentation (Nov 03) — proposal recap, status update, and timeline; at most 10 minutes.
3. Final presentation (Dec 08) — updated problem definition, literature survey, and results; at most 20 minutes.
4. Report (due Dec 18) — a conference paper-style write-up.

---

<!-- slide:content -->
# Paper Discussions

- Every student will present two papers.

---

<!-- slide:content -->
# Schedule

All due dates are end of day on the date listed.

| Date | Description | Read |
| --- | --- | --- |
| Sep 15 | Introduction and overview | [1](overview-slides.html) |
| **Sep 15** | **[Discussion preferences due](FORM_URL_HERE)** | |
| Sep 22 | Agents and tool-use **ATU** | [1](https://rlhfbook.com/c/13-tools), ? |
| Sep 29 | Constraints on LLM outputs **SSC** | [1](https://huggingface.co/blog/how-to-generate), ? |
| Oct 06 | Learning specifications from data **LSD** | ?, ? |
| **Oct 09** | **Proposals due** | |
| ~~Oct 13~~ | ~~Reading week~~ | |
| Oct 20 | Autoformalization **AUF** | ?, ? |
| Oct 27 | Satisfiability (modulo theories) **SAT** | [1](https://verifieddeeplearning.com/nnv_book.pdf), ? |
| _Nov 03_ | _Mini presentations day_ | |
| Nov 10 | Theorem proving **TPR** | ?, ? |
| Nov 17 | Verification of programs **VER** | ?, ? |
| Nov 24 | Superoptimization **SUP** | ?, ? |
| Dec 01 | Bonus | [1](https://proceedings.neurips.cc/paper/2020/hash/342285bb2a8cadef22f667eeb6a63732-Abstract.html), ? |
| _Dec 08_ | _Final presentations day_ | |
| **Dec 18** | **Reports due** | |

---

<!-- slide:section -->
# Agents and Tool-Use (Sep 22)
`ATU`

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
## LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers

[Olausson et al., EMNLP '23](https://aclanthology.org/2023.emnlp-main.313.pdf)

`ATU`

---

<!-- slide:paper -->
## Towards Verifiably Safe Tool Use for LLM Agents

[Doshi et al., ICSE-NIER '26](https://dl.acm.org/doi/pdf/10.1145/3786582.3786839)

`ATU`

---

<!-- slide:section -->
# Constraints on LLM Outputs (Sep 29)
`SSC`

---

<!-- slide:paper -->
## How To Generate Text: Using Different Decoding Methods For Language Generation With Transformers

[von Platen, Blog '20](https://huggingface.co/blog/how-to-generate)

`SSC` `CONFIRMED`

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
# Learning Specifications from Data (Oct 06)
`LSD`

---

<!-- slide:paper -->
## Mining Specifications

[Ammons et al., POPL '02](https://haoxintu.github.io/files/10-Mining%20specifications.pdf)

`LSD`

---

<!-- slide:paper -->
## Learning Concise Models from Long Execution Traces

[Jeppu et al., DAC '20](https://arxiv.org/abs/2001.05230)

`LSD`

---

<!-- slide:paper -->
## Learning Context-Free Grammars for Grammar-Constrained Decoding via Declarative Agentic Programming with Guarantees

[Cheang et al., arXiv '26](https://arxiv.org/abs/2608.05493)

`LSD`

---

<!-- slide:section -->
# Autoformalization (Oct 20)
`AUF`

---

<!-- slide:paper -->
## Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages

[Mora et al., NeurIPS '24](https://arxiv.org/pdf/2406.03636)

`AUF`

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
# Satisfiability (Modulo Theories) (Oct 27)
`SAT`

---

<!-- slide:paper -->
## Introduction to Neural Network Verification, Chapters 4, 6 (7 optional)

[Albarghouthi, Textbook '26](https://verifieddeeplearning.com/nnv_book.pdf)

`SAT` `CONFIRMED`

---

<!-- slide:paper -->
## SATzilla: Portfolio-based Algorithm Selection for SAT

[Xu et al., JAIR '08](https://arxiv.org/abs/1111.2249)

`SAT`

---

<!-- slide:paper -->
## MedleySolver: Online SMT Algorithm Selection

[Pimpalkhare et al., SAT '21](https://www.pure.ed.ac.uk/ws/files/248374419/MedleySolver_PIMPALKHARE_DOA05072021_AFV.pdf)

`SAT`

---

<!-- slide:paper -->
## Guiding High-Performance SAT Solvers with Unsat-Core Predictions

[Selsam and Bjørner, SAT '19](https://link.springer.com/chapter/10.1007/978-3-030-24258-9_24)

`SAT`

---

<!-- slide:paper -->
## Learning to Solve SMT Formulas

[Balunović et al., NeurIPS '18](https://www.sri.inf.ethz.ch/publications/balunovic2018learnsmt)

`SAT`

---

<!-- slide:paper -->
## Domain-Specific Hyperspecialization (For SAT)

[Green, Blog '26](https://c.mov/lymphosat/)

`SAT`

---

<!-- slide:section -->
# Theorem Proving (Nov 10)
`TPR`

---

<!-- slide:paper -->
## Generative Language Modeling for Automated Theorem Proving

[Polu and Sutskever, arXiv '20](https://arxiv.org/abs/2009.03393)

`TPR`

---

<!-- slide:paper -->
## Postmortem for Kernel Soundness Bug #14576

[de Moura, Blog '26](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/)

`TPR`

---

<!-- slide:section -->
# Verification of Programs (Nov 17)
`VER`

---

<!-- slide:paper -->
## Large Language Model Powered Symbolic Execution

[Li et al., OOPSLA '25](https://doi.org/10.1145/3763163)

`VER`

---

<!-- slide:paper -->
## Let a Neural Network Be Your Invariant

[Giacobbe et al., NeurIPS '25](https://openreview.net/forum?id=qBPb7g1SEa)

`VER`

---

<!-- slide:paper -->
## Agentic Verification of Software Systems

[Tu et al., FSE '26](https://arxiv.org/abs/2511.17330)

`VER`

---

<!-- slide:paper -->
## Introduction to Neural Network Verification, Chapters 1, 2, 3, 5

[Albarghouthi, Textbook '26](https://verifieddeeplearning.com/nnv_book.pdf)

`VER`

---

<!-- slide:paper -->
## Proving Data-Poisoning Robustness in Decision Trees

[Drews et al., PLDI '20](https://dl.acm.org/doi/10.1145/3385412.3385975)

`VER`

---

<!-- slide:paper -->
## Beta-CROWN: Efficient Bound Propagation with Per-neuron Split Constraints for Complete and Incomplete Neural Network Robustness Verification

[Wang et al., NeurIPS '21](https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html)

`VER`

---

<!-- slide:section -->
# Superoptimization (Nov 24)
`SUP`

---

<!-- slide:paper -->
## Stochastic Superoptimization

[Schkufza et al., ASPLOS '13](https://dl.acm.org/doi/10.1145/2490301.2451150)

`SUP`

---

<!-- slide:paper -->
## Faster Sorting Algorithms Discovered Using Deep Reinforcement Learning

[Mankowitz et al., Nature '23](https://www.nature.com/articles/s41586-023-06004-9)

`SUP`

---

<!-- slide:section -->
# Neuro-symbolic Programming (Dec 01)
`NSP`

---

<!-- slide:paper -->
## Learning Differentiable Programs with Admissible Neural Heuristics

[Shah et al., NeurIPS '20](https://proceedings.neurips.cc/paper/2020/hash/342285bb2a8cadef22f667eeb6a63732-Abstract.html)

`NSP` `CONFIRMED`

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
# Discussion Preferences (Due Sep 15)

Fill out [this form](FORM_URL_HERE) to submit your discussion preferences by
end of day on Sep 15.

You will be matched to papers based on your submitted preferences on Sep 16.
