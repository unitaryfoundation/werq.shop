---
title: "Scaling Quantum Error Mitigation in the Age of Distributed Quantum Computation"
speaker: "María Gragera Garcés"
website: ""
bio: ""
headshot: ""
slides: ""
---

Quantum Error Mitigation (QEM) has shown promise on near-term devices, but its scalability in future architectures, particularly those that distribute computation across multiple quantum processing units (QPUs), remains underexplored. This talk outlines key challenges and considerations for extending QEM to distributed quantum computing (DQC), where circuit partitioning, inter-QPU communication, and synchronization introduce new sources of error and resource tradeoffs. We examine why QEM must adapt to these emerging execution models, focusing on overheads from communication-induced decoherence, redundant mitigation across device boundaries, and the complexity introduced by heterogeneous noise profiles. Common QEM techniques such as zero-noise extrapolation and probabilistic error cancellation are evaluated in the context of partitioned circuits, using synthetic circuit studies to characterize their scalability and limitations. The discussion also considers how compilation-time decisions affect mitigation feasibility and cost, and highlights the role of hybrid classical-quantum feedback and scheduling in real-world deployments. The aim of this talk is to raise awareness of the need for distribution-aware QEM frameworks and to foster collaboration across compiler, mitigation, and architecture communities.
