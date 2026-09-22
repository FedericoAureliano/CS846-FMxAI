---
instructor: Federico Mora
instructor_url: https://federico.morarocha.ca
term: Fall '26
schedule: Tues 3:00-5:50pm
---

# CS846: FMxAI

The goal of this course is to help every student create a novel piece of
research at the intersection of formal methods and artificial intelligence. To
do this, we will discuss important ideas in this space and collaborate to
refine each other's work.

## Grading {: #grading}

Our meetings will be centered around paper discussions and in-class activities.
Attendance, reading of assigned papers, and participation are essential. The
grading scheme reflects that:

- 20% participation;
- 30% discussion leads; and
- 50% project.

## Participation {: #participation}

The best way to achieve the goal of the course is through active participation.
That means completing the assigned readings before class, engaging in
discussions during class, helping other students understand the material,
providing constructive feedback to other students, and doing your best on all
assessments.

This class is not a competition. There is no curve or anything resembling a
curve. The goal is for everyone to learn and create something new, and your
behavior should reflect that. In particular, your actions should never make
another student feel stereotyped, unwelcome, uncomfortable, or unsafe. Not only
would these actions be wrong, but there is a great deal of research that shows
how they damage students' course performance (e.g., see "stereotype threat").
Please take care, so we can create a class in which all students feel supported
and respected.


## Discussion Leads {: #discussion-leads}

Students will submit discussion lead preferences through a 
[LEARN quiz](https://learn.uwaterloo.ca) due Sep 15. Discussion lead 
assignments will be sent out on Sep 16.

There will be three kinds of readings: research papers, textbooks, and blog
posts. For research papers, discussion leads will present a review with four
components:

- research context (~5 minutes);
- paper summary (~15 minutes);
- strengths and weaknesses (~5 minutes); and
- what has changed or will change (~5 minutes).

For textbooks, discussion leads will give a 30-minute tutorial. The goal is to
gain an in-depth understanding of foundational concepts as a class. Students
can follow the textbook content as closely as needed. For blog posts, students
will lead a 30-minute deep-dive into the blog content. This can include slides,
a code demo, or any other pedagogical activities.

## Projects {: #projects}

Every project must contain new research---a new idea or insight---and an
element of both formal methods and artificial intelligence. Students can work
in groups of up to three.

The main deliverables (in chronological order) will be:

1. proposal (due Oct 09);
2. mini presentation (Nov 03);
3. final presentation (Dec 08); and
4. report (due Dec 18).

### Guidelines for Proposal {: #guidelines-for-proposal}

The proposal must contain a problem definition, a literature survey, and an
intuition for a possible solution. It should be at most one page long and use a
reasonable format (margins, font, etc.).

### Guidelines for Mini Presentation {: #guidelines-for-mini-presentation}

The mini presentation should cover the contents of the proposal, a quick status
update, and a timeline for the remainder of the term. The mini presentation
should be at most 10 minutes long.

### Guidelines for Final Presentation {: #guidelines-for-final-presentation}

The final presentation should build on the mini presentation. It should contain
an updated problem definition, an updated literature survey, a description of
the approach, and final results. The final presentation should be at most 20
minutes long.

### Guidelines for Report {: #guidelines-for-report}

The report should be a conference paper-style write-up. For example, students
can use the [AAAI-27
format](https://aaai.org/conference/aaai/aaai-27/main-technical-track-call/) and include the following sections:

1. introduction;
2. technical background;
3. approach;
4. evaluation;
5. related work; and
6. conclusions/future work.

## Schedule {: #schedule}

On paper discussion days, there will be at least two assigned readings and
corresponding student-led presentations.

| Date | Description | Read |
| --- | --- | --- |
| Sep 15 | Introduction and overview | [1](overview-slides.html), [2](https://federico.morarocha.ca/agentic-stack/) |
| **Sep 15** | **[Discussion preferences due](https://learn.uwaterloo.ca)** | |
| Sep 22 | Agents and tool-use **ATU** | [1](https://aclanthology.org/2023.emnlp-main.313.pdf), [2](https://rlhfbook.com/c/13-tools), [3](https://dl.acm.org/doi/pdf/10.1145/3786582.3786839) |
| Sep 29 | Constraints on LLM outputs **CLO** | [1](https://huggingface.co/blog/how-to-generate), [2](https://dl.acm.org/doi/10.1145/3729274), [3](https://arxiv.org/pdf/2504.11703) |
| Oct 06 | Generating system constraints **GSC** | [1](https://haoxintu.github.io/files/10-Mining%20specifications.pdf), [2](https://arxiv.org/abs/2608.05493), [3](https://link.springer.com/chapter/10.1007/978-3-032-32526-6_28) |
| **Oct 09** | **Proposals due** | |
| ~~Oct 13~~ | ~~Reading week~~ | |
| Oct 20 | Satisfiability (modulo theories) **SAT** | [1](https://verifieddeeplearning.com/nnv_book.pdf), [2](https://arxiv.org/pdf/1903.04671), [3](https://c.mov/lymphosat/) |
| Oct 27 | Program verification **PVE** | [1](https://dafny.org/latest/OnlineTutorial/guide), [2](https://dl.acm.org/doi/full/10.1145/3763174), [3](https://doi.org/10.1145/3763163) |
| _Nov 03_ | _Mini presentations day_ | |
| Nov 10 | Superoptimization **SUP** | [1](https://dl.acm.org/doi/10.1145/2490301.2451150), [2](https://www.nature.com/articles/s41586-023-06004-9), [3](https://www.nature.com/articles/s41586-023-06924-6), [4](https://kim-em.github.io/blog/2026-7-24-why-lean-is-faster-than-rust/) |
| Nov 17 | Theorem proving **TPR** | [1](https://arxiv.org/abs/2009.03393), [2](https://openreview.net/pdf?id=GN8OdkTo3B), [3](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) |
| Nov 24 | Machine-learning verification **MLV** | [1](https://verifieddeeplearning.com/nnv_book.pdf), [2](https://arxiv.org/pdf/2605.07451), [3](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b8c80f9113b9f8e2e129447221682a-Abstract-Conference.html)\* |
| Dec 01 | Bonus | [1](https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html)\*, [2](https://proceedings.neurips.cc/paper/2020/hash/342285bb2a8cadef22f667eeb6a63732-Abstract.html), [3](https://www.ijcai.org/proceedings/2024/0211.pdf) |
| _Dec 08_ | _Final presentations day_ | |
| **Dec 18** | **Reports due** | |

\* This reading's theme (see the Reading Bank) is different from the day's theme.

### Reading Bank {: #reading-bank}

The readings will be drawn from the following bank of papers, textbooks, and
blog posts, which cover nine themes: agents and tool-use **ATU**; syntactic and
semantic constraints on LLM outputs **CLO**; generating system constraints
**GSC**; satisfiability (modulo theories) **SAT**; program verification
**PVE**; superoptimization **SUP**; theorem proving **TPR**; machine-learning
verification **MLV**; and neuro-symbolic programming **NSP**.

| Title | Link | Topic |
| --- | --- | --- |
| LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers | [Olausson et al., EMNLP '23](https://aclanthology.org/2023.emnlp-main.313.pdf) | ATU |
| Reinforcement Learning from Human Feedback, Chapter 13 | [Lambert, Textbook '26](https://rlhfbook.com/c/13-tools) | ATU |
| Towards Verifiably Safe Tool Use for LLM Agents | [Doshi et al., ICSE-NIER '26](https://dl.acm.org/doi/pdf/10.1145/3786582.3786839) | ATU |
| How To Generate Text: Using Different Decoding Methods For Language Generation With Transformers | [von Platen, Blog '20](https://huggingface.co/blog/how-to-generate) | CLO |
| Constrained Adaptive Rejection Sampling | [Parys et al., ICML '26](https://arxiv.org/pdf/2510.01902) | CLO |
| Type-Constrained Code Generation with Language Models | [Mündler et al., PLDI '25](https://dl.acm.org/doi/10.1145/3729274) | CLO |
| Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages | [Mora et al., NeurIPS '24](https://arxiv.org/pdf/2406.03636) | CLO |
| Mining Specifications | [Ammons et al., POPL '02](https://haoxintu.github.io/files/10-Mining%20specifications.pdf) | GSC |
| Learning Context-Free Grammars for Grammar-Constrained Decoding via Declarative Agentic Programming with Guarantees | [Cheang et al., arXiv '26](https://arxiv.org/abs/2608.05493) | GSC |
| A Neurosymbolic Approach to Natural Language Formalization and Verification | [An et al., CAV '26](https://link.springer.com/chapter/10.1007/978-3-032-32526-6_28) | GSC |
| Introduction to Neural Network Verification, Chapters 4, 6 (7 optional) | [Albarghouthi, Textbook '26](https://verifieddeeplearning.com/nnv_book.pdf) | SAT |
| Guiding High-Performance SAT Solvers with Unsat-Core Predictions | [Selsam and Bjørner, SAT '19](https://arxiv.org/pdf/1903.04671) | SAT |
| Learning to Solve SMT Formulas | [Balunović et al., NeurIPS '18](https://www.sri.inf.ethz.ch/publications/balunovic2018learnsmt) | SAT |
| SATzilla: Portfolio-based Algorithm Selection for SAT | [Xu et al., JAIR '08](https://arxiv.org/abs/1111.2249) | SAT |
| MedleySolver: Online SMT Algorithm Selection | [Pimpalkhare et al., SAT '21](https://www.pure.ed.ac.uk/ws/files/248374419/MedleySolver_PIMPALKHARE_DOA05072021_AFV.pdf) | SAT |
| Layered and Staged Monte Carlo Tree Search for SMT Strategy Synthesis | [Lu et al., IJCAI '24](https://www.ijcai.org/proceedings/2024/0211.pdf) | SAT |
| Domain-Specific Hyperspecialization (For SAT) | [Green, Blog '26](https://c.mov/lymphosat/) | SAT |
| Getting Started with Dafny: A Guide | [Leino, Textbook '23](https://dafny.org/latest/OnlineTutorial/guide) | PVE |
| AutoVerus: Automated Proof Generation for Rust Code | [Yang et al., OOPSLA '25](https://dl.acm.org/doi/full/10.1145/3763174) | PVE |
| VERINA: Benchmarking Verifiable Code Generation | [Ye et al., ICLR '26](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b8c80f9113b9f8e2e129447221682a-Abstract-Conference.html) | PVE |
| Large Language Model Powered Symbolic Execution | [Li et al., OOPSLA '25](https://doi.org/10.1145/3763163) | PVE |
| Program Synthesis is Possible | [Sampson, Blog '18](https://www.cs.cornell.edu/~asampson/blog/minisynth.html) | SUP |
| Stochastic Superoptimization | [Schkufza et al., ASPLOS '13](https://dl.acm.org/doi/10.1145/2490301.2451150) | SUP |
| Faster Sorting Algorithms Discovered Using Deep Reinforcement Learning | [Mankowitz et al., Nature '23](https://www.nature.com/articles/s41586-023-06004-9) | SUP |
| Mathematical Discoveries from Program Search with Large Language Models | [Romera-Paredes et al., Nature '23](https://www.nature.com/articles/s41586-023-06924-6) | SUP |
| Why Lean is faster than Rust | [Morrison, Blog '26](https://kim-em.github.io/blog/2026-7-24-why-lean-is-faster-than-rust/) | SUP |
| Generative Language Modeling for Automated Theorem Proving | [Polu and Sutskever, arXiv '20](https://arxiv.org/abs/2009.03393) | TPR |
| Hilbert: Recursively Building Formal Proofs with Informal Reasoning | [Varambally et al., ICLR '26](https://openreview.net/pdf?id=GN8OdkTo3B) | TPR |
| Postmortem for Kernel Soundness Bug #14576 | [de Moura, Blog '26](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) | TPR |
| Introduction to Neural Network Verification, Chapters 1, 2, 3, 5 | [Albarghouthi, Textbook '26](https://verifieddeeplearning.com/nnv_book.pdf) | MLV |
| VNN-LIB 2.0: Rigorous Foundations for Neural Network Verification | [Roy et al., CAV '26](https://arxiv.org/pdf/2605.07451) | MLV |
| Beta-CROWN: Efficient Bound Propagation with Per-neuron Split Constraints for Complete and Incomplete Neural Network Robustness Verification | [Wang et al., NeurIPS '21](https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html) | MLV |
| Learning Differentiable Programs with Admissible Neural Heuristics | [Shah et al., NeurIPS '20](https://proceedings.neurips.cc/paper/2020/hash/342285bb2a8cadef22f667eeb6a63732-Abstract.html) | NSP |


## Accommodations {: #accommodations}

The course is designed to help every student create a novel piece of research.
If you find that a change is needed, please come talk to me so that we can work
together to achieve the goal of the course through alternate means. One of the
best ways to work together is to talk about potential issues and solutions as
early as possible. For example, if you already know that you would benefit from
accommodations, please meet with me so we can develop an implementation plan
together.


## AI Use Policy {: #ai}

Careful use of AI tools is allowed. Please refer to the 
[libraries' guide on citing and disclosing AI use](https://subjectguides.uwaterloo.ca/citationstyles/genaitools), 
the [copyright advisory committee's warning](https://uwaterloo.ca/copyright-at-waterloo/teaching/generative-artificial-intelligence), 
and the [university's guidelines regarding university data](https://uwaterloo.ca/generative-ai/ai-tools-and-systems).

## References {: #references}

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
