---
title: "Drift-resilient mitigation techniques for dynamic circuits and QEM-QEC integration"
speaker: "Raam Uzdin"
website: ""
bio: ""
headshot: ""
slides: ""
---

This talk reviews several mitigation techniques we have developed that are compatible with dynamic circuits. Dynamic circuits encapsulate both error correction codes and efficient circuits for entangled state preparation, gate teleportation, semi-classical Fourier transform, barren plateau free VQE, and more. The gate error is mitigated using the recently introduced Layered KIK protocol which extends the Adaptive KIK protocol to dynamic circuits. We will also present a mid-circuit measurement mitigation protocol based on the parity of consecutive measurements. This idea is also extended to terminating measurements and preparation error. As such, it offers an efficient alternative to gate set alternative. Finally, we present pseudo-twirling for mitigating coherent error in non-Clifford gates. Contrary to previous work on this topic, we provide a theoretical analysis that describes the nature of the residual incoherent error and the effect of the protocol on the native incoherent errors. Crucially, all the above-described methods are resilient to time drifts in the noise parameters and require no noise characterization. Supporting experimental results will be presented. This work paves the way to integration of error mitigation and error correction where error correction will do the heavy lifting of addressing local error, and error mitigation will mitigate errors that challenge error correction codes such as correlated errors and leakage errors.
