---
instructor: Federico Mora
instructor_url: https://federico.morarocha.ca
term: Fall '26
schedule: Tues 3:00-5:50pm
location: DC 2585
---

**⚠ DRAFT:** This syllabus will change substantially before the term begins.
{: .draft-banner}

# CS846: FMxAI

This course surveys important ideas and literature at the intersection of formal
methods and artificial intelligence.

## Grading {: #grading}

Our meetings will be centered around paper discussions. Attendance, reading of
assigned papers, and participation are essential. The grading scheme reflects
that:

- 20% participation;
- 30% discussion leads; and
- 50% project.

## Discussion Leads {: #discussion-leads}

Every student will pick and present two papers with two different themes from the reading bank below.

## Projects {: #projects}

Every project must contain new research---a new idea or insight---and an
element of both formal methods and artificial intelligence. Students can work
in groups of up to three.

The main deliverables (in chronological order) will be:

1. proposal;
2. mini presentation;
3. final presentation; and
4. report.

### Guidelines for Proposal {: #guidelines-for-proposal}

The proposal must contain a problem definition and a brief literature survey.
It should be at most one page long and use a reasonable format (margins, font, etc.).

### Guidelines for Mini Presentation {: #guidelines-for-mini-presentation}

The mini presentation should cover the contents of the proposal, a quick status
update, and a timeline for the remainder of the term. The mini presentation
should be at most 10 minutes long.

### Guidelines for Final Presentation {: #guidelines-for-final-presentation}

The final presentation should build on the mini presentation. It should contain
an updated problem definition, an updated literature survey, and final results.
The final presentation should be at most 20 minutes long.

### Guidelines for Report {: #guidelines-for-report}

The report should be a conference paper-style write-up.

## Participation {: #participation}

Students are expected to complete the assigned readings before class and to
engage respectfully with their peers and their work.

## Schedule {: #schedule}

On paper discussion days, there will be **two** assigned readings and
corresponding student-led presentations.

| Date | Description | Readings |
| --- | --- | --- |
| Sep 15 | Introduction and overview | |
| **Sep 16** | **Reading preferences due** | |
| Sep 22 | Agents and tool-use **ATU** | TBD |
| Sep 29 | Syntactic and semantic constraints on LLM outputs **SSC** | TBD |
| Oct 06 | Learning constraints from data **LCD** | TBD |
| **Oct 09** | **Proposals due** | |
| ~~Oct 13~~ | ~~Reading week~~ | |
| Oct 20 | Autoformalization **AUF** | TBD |
| Oct 27 | Program analysis **PRA** | TBD |
| _Nov 03_ | _Mini presentations day_ | |
| Nov 10 | Satisfiability and satisfiability modulo theories **SAT** | TBD |
| Nov 17 | Theorem proving **TPR** | TBD |
| Nov 24 | Superoptimization **SUP** | TBD |
| Dec 01 | Bonus (**NSP**, **MLV**, **PRP**, or **TST**) | TBD |
| _Dec 08_ | _Final presentations day_ | |
| **Dec 18** | **Reports due** | |

## Reading Bank {: #reading-bank}

The readings below span twelve themes: syntactic and semantic constraints on
LLM outputs **SSC**; learning constraints from data **LCD**; agents and
tool-use **ATU**; satisfiability and satisfiability modulo theories **SAT**;
program analysis **PRA**; autoformalization **AUF**; neuro-symbolic programming
**NSP**; superoptimization **SUP**; theorem proving **TPR**; machine-learning
verification **MLV**; program repair **PRP**; and testing **TST**. Use the
dropdown in the table's rightmost column to narrow the list to a single theme.

| Title | Link | Topics |
| --- | --- | --- |
| Learning Regular Sets from Queries and Counterexamples | [Angluin, I&C '87](https://swt.informatik.uni-freiburg.de/teaching/WS2019-20/AutomataTheory/Learning%20Automata%20%28Caveat%20not%20related%20to%20Machine%20Learning?month:int=4&year:int=2025&orig_query=) | LCD |
| Mining Specifications | [Ammons et al., POPL '02](https://haoxintu.github.io/files/10-Mining%20specifications.pdf) | LCD |
| SATzilla: Portfolio-based Algorithm Selection for SAT | [Xu et al., JAIR '08](https://arxiv.org/abs/1111.2249) | SAT |
| Stochastic Superoptimization | [Schkufza et al., ASPLOS '13](https://dl.acm.org/doi/10.1145/2490301.2451150) | SUP |
| Learning to Superoptimize Programs | [Bunel et al., ICLR '17](https://arxiv.org/abs/1612.01094) | SUP |
| Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks | [Katz et al., CAV '17](https://link.springer.com/chapter/10.1007/978-3-319-63387-9_5) | MLV, SAT |
| Learning to Solve SMT Formulas | [Balunović et al., NeurIPS '18](https://www.sri.inf.ethz.ch/publications/balunovic2018learnsmt) | SAT |
| DeepProbLog: Neural Probabilistic Logic Programming | [Manhaeve et al., NeurIPS '18](https://proceedings.neurips.cc/paper/2018/hash/dc5d637ed5e62c36ecb73b654b05ba2a-Abstract.html) | NSP |
| Guiding High-Performance SAT Solvers with Unsat-Core Predictions | [Selsam and Bjørner, SAT '19](https://link.springer.com/chapter/10.1007/978-3-030-24258-9_24) | SAT |
| How To Generate Text: Using Different Decoding Methods For Language Generation With Transformers | [von Platen, Blog '20](https://huggingface.co/blog/how-to-generate) | ATU, SSC |
| Learning Concise Models from Long Execution Traces | [Jeppu et al., DAC '20](https://arxiv.org/abs/2001.05230) | LCD |
| Proving Data-Poisoning Robustness in Decision Trees | [Drews et al., PLDI '20](https://dl.acm.org/doi/10.1145/3385412.3385975) | MLV |
| Generative Language Modeling for Automated Theorem Proving | [Polu and Sutskever, arXiv '20](https://arxiv.org/abs/2009.03393) | TPR |
| MedleySolver: Online SMT Algorithm Selection | [Pimpalkhare et al., SAT '21](https://www.pure.ed.ac.uk/ws/files/248374419/MedleySolver_PIMPALKHARE_DOA05072021_AFV.pdf) | SAT |
| PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | [Scholak et al., EMNLP '21](https://aclanthology.org/2021.emnlp-main.779/) | SSC |
| Beta-CROWN: Efficient Bound Propagation with Per-neuron Split Constraints for Complete and Incomplete Neural Network Robustness Verification | [Wang et al., NeurIPS '21](https://proceedings.neurips.cc/paper/2021/hash/fac7fead96dafceaf80c1daffeae82a4-Abstract.html) | MLV |
| Neural Network Verification with Proof Production | [Isac et al., FMCAD '22](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10026587&casa_token=6jy7_pSgbOwAAAAA:HNny8NVwdhsCPew67iMK2jLHdzqnTfss8SOPuMsrDubYtSQ_Y8IiU8myHghTs7t7MO1ymxzL9Q) | MLV |
| HyperTree Proof Search for Neural Theorem Proving | [Lample et al., NeurIPS '22](https://proceedings.neurips.cc/paper_files/paper/2022/hash/a8901c5e85fb8e1823bbf0f755053672-Abstract-Conference.html) | TPR |
| LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers | [Olausson et al., EMNLP '23](https://aclanthology.org/2023.emnlp-main.313.pdf) | ATU, AUF |
| Scallop: A Language for Neurosymbolic Programming | [Li et al., PLDI '23](https://dl.acm.org/doi/pdf/10.1145/3591280) | NSP |
| Grammar Prompting for Domain-Specific Language Generation with Large Language Models | [Wang et al., NeurIPS '23](https://arxiv.org/pdf/2305.19234) | SSC |
| Automated Repair of Programs from Large Language Models | [Fan et al., ICSE '23](https://dl.acm.org/doi/10.1109/ICSE48619.2023.00128) | PRP |
| Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models | [Deng et al., ISSTA '23](https://dl.acm.org/doi/abs/10.1145/3597926.3598067) | TST |
| CODAMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models | [Lemieux et al., ICSE '23](https://www.carolemieux.com/codamosa_icse23.pdf) | TST |
| Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages | [Mora et al., NeurIPS '24](https://arxiv.org/pdf/2406.03636) | AUF, SSC, PRP |
| LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference | [Wu et al., ASE '24](https://dl.acm.org/doi/10.1145/3691620.3695014) | LCD, PRA |
| Specgen: Automated Generation Of Formal Program Specifications Via Large Language Models | [Ma et al., ICSE '25](https://dl.acm.org/doi/10.1109/ICSE55347.2025.00129) | AUF, LCD |
| Let a Neural Network Be Your Invariant | [Giacobbe et al., NeurIPS '25](https://openreview.net/forum?id=qBPb7g1SEa) | LCD, PRA |
| Large Language Model Powered Symbolic Execution | [Li et al., OOPSLA '25](https://doi.org/10.1145/3763163) | PRA |
| Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving | [ByteDance, Arxiv '25](https://arxiv.org/pdf/2507.23726) | TPR |
| Learning Context-Free Grammars for Grammar-Constrained Decoding via Declarative Agentic Programming with Guarantees | [Cheang et al., Arxiv '26](https://arxiv.org/abs/2608.05493) | ATU, LCD, AUF |
| Reinforcement Learning from Human Feedback, Chapter 13 | [Lambert, Textbook '26](https://rlhfbook.com/c/13-tools) | ATU |
| A Neurosymbolic Approach to Natural Language Formalization and Verification | [An et al., CAV '26](https://link.springer.com/chapter/10.1007/978-3-032-32526-6_28) | AUF |
| Agentic Verification of Software Systems | [Tu et al., FSE '26](https://arxiv.org/abs/2511.17330) | PRA |
| Domain-Specific Hyperspecialization (For SAT) | [Green, Blog '26](https://c.mov/lymphosat/) | SAT |
| Constrained Adaptive Rejection Sampling | [Parys et al., ICML '26](https://arxiv.org/pdf/2510.01902) | SSC |
| ChopChop: A Programmable Framework for Semantically Constraining the Output of Language Models | [Nagy et al., POPL '26](https://arxiv.org/pdf/2509.00360) | SSC |
