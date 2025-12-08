# MiniDrop

**MiniDrop** is a compact, easy-to-follow collection of code and explanations for droplet-based experiments, algorithms, and implementation methods.

<br>

<img src="figures/figure_001.png" width="500px">

---

## Prior Knowledge (recommended)

Start here to understand the essential concepts before running any examples.

👉 **[Prior Knowledge — Droplet basics and concepts](https://keita-iida.github.io/MiniDrop/docs/priorknowledge_001.html)**

Reading this first will greatly help when following the tutorial.

---

## Tutorial (hands-on)

After reviewing the prior knowledge, move on to the guided tutorial.

👉 **[MiniDrop Tutorial — step-by-step guide](https://keita-iida.github.io/MiniDrop/docs/tutorial_minidrop.html)**

---

## Quick Start

**This repository uses Git LFS to manage large files. Make sure you have [Git LFS installed](https://git-lfs.com/) before cloning.**

After installing Git LFS, clone the repository with:

```bash
git clone https://github.com/keita-iida/MiniDrop.git
cd MiniDrop
```

Then follow the tutorial for full setup and usage instructions.

---

## Requirements

To run MiniDrop, you’ll need a Linux or Linux-like environment with the following tools installed:

- samtools
- Picard
- Dropseq Tools
- STAR

The specific versions of these tools can be found in the [`environment.yaml`](environment.yaml) file.

### Environment Setup

The recommended way to set up the environment is using [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
If you do not have it installed, consider using [Miniforge](https://conda-forge.org/download) or [Miniconda](https://docs.anaconda.com/miniconda/).

You can create and activate the environment with the provided `environment.yaml` file using the following commands:

```bash
conda env create -f environment.yaml
conda activate minidrop
```

### macOS Compatibility

Unfortunately, macOS was not fully compatible in our pretests. Support for macOS is under development.

---

## Licence

This project is available under the **MIT Licence**.
See the `LICENSE` file for details.
