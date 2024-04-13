# Rtrafactor - LLMs on Steroids 

Welcome to Eternity AI's Rtrafactor workspace!

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nzJou9tONTF6AOKqJTZc8--rIwI38JuR?usp=sharing)

## Overview

Rtrafactor is a Python library developed at the Indian Institute of Technology, Patna, as part of the Real Time Retrieval Argumentation (RTRA) architecture. It integrates real-time access tools like search, retrieval, summarization, and argumentation into AI models via a Python library.

To read the research paper detailing RTRA, click [here](https://eternityai.tech).

## Installation

Install Rtrafactor into your project using pip:

```bash
pip install rtrafactor
```

## Package Validation

Ensure the authenticity of the installed package:

```bash
pip show rtrafactor
```

## Usage

Rtrafactor is available as a L2LM (Language-to-Language Model) architecture, currently integrated with HuggingFace's Inference API. Follow these steps to use Rtrafactor:

1. **Import RTRAConnector**: 

   ```python
   from rtrafactor import RTRAConnector
   ```

2. **Instantiate RTRAConnector**: 

   ```python
   connector = RTRAConnector(huggingface_model, huggingface_api_token)
   ```

3. **Query for Answers**: 

   ```python
   query = "Your question here?"
   one_shot_answer = connector.compare_answers(query)
   print(one_shot_answer)
   ```

## Examples

Here are some example queries you can try with Rtrafactor:

1. **Why is Delhi's CM in jail?**
2. **Who is Dr. Kuldip Singh Patel?**
3. **Who is Udit Akhouri?**

## Limitations & Future Scope

While RTRA enhances model capabilities, there are still limitations to address:

- **Hallucination & Citation**: Addressing false information and improving citation accuracy.
- **Latency**: Reducing response time and optimizing underlying architecture.

## Breakthrough

RTRA architecture challenges the conventional approach of relying on vast computational resources by democratizing access to the internet's information. It enables developers, including solo developers and small teams, to build efficient models without requiring extensive computational resources.

## Acknowledgements

This project was developed by udit Raj, Sanya Gupta, and other fellow researchers at the Indian Institute of Technology, Patna, as part of ongoing research in AI and natural language processing.

---

For detailed usage examples and code, visit [Rtrafactor on Google Colab](https://colab.research.google.com/drive/1nzJou9tONTF6AOKqJTZc8--rIwI38JuR?usp=sharing).


