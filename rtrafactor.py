
pip install rtrafactor
pip show rtrafactor

from rtrafactor import RTRAConnector

"""# Example #1
Why is Delhi's CM in jail?
"""

# Example usage:
huggingface_model = "username/huggingface_model"
huggingface_api_token = "write_api_token"

connector = RTRAConnector(huggingface_model, huggingface_api_token)
query = "Why is Delhi's CM in jail?"
one_shot_answer = connector.compare_answers(query)
print(one_shot_answer)

"""# Example #2
Who is Dr. Kuldip Singh Patel?
"""

# Example usage:
huggingface_model = "username/huggingface_model"
huggingface_api_token = "write_api_token"

connector = RTRAConnector(huggingface_model, huggingface_api_token)
query = "Who is Dr. Kuldip Singh Patel?"
one_shot_answer = connector.compare_answers(query)
print(one_shot_answer)

"""# Example #3

Who is Udit Akhouri?
"""

# Example usage:
huggingface_model = "username/huggingface_model"
huggingface_api_token = "write_api_token"

connector = RTRAConnector(huggingface_model, huggingface_api_token)
query = "Who is Udit Akhouri?"
one_shot_answer = connector.compare_answers(query)
print(one_shot_answer)


Currently, we are in the midst of a race of who can scrape the most of the interent and put it on their servers so their model can answer it. This requires a lot of computation and makes it impossible for solo developers and small teams to make a super efficient model.

RTRA architecture challenges this convection thought process. We belive that the interent is available for free and anyone can access it. That's why, you don't need to rely on huge computational resources (unline what Jansen Huang or Sam Altman says).

We are not on a war with Open AI, Nvidia or Google. However, we are just democratizing the resources so even a 1st year undergrad student can build models as efficient as GPT4 right from his Google Colab notebook.

We are currently testing our RTRA on low-parameter models and have successfully increased efficiency of Google's Gemma 7B to best Gemini 1.0 in multiple precision benchmarks. We are planning work specifically on models with <1 billion parameters to achieve the same efficiency of atleast a 7 billion parameter model with the help of RTRA architecture.
"""
