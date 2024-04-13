
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

