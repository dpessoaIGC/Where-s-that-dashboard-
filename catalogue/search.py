
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import json

default_instructions = """You are to provide the catalog's keys whose values titles and descriptions seem to best match the request, ordered by match quality.

Format the result in a list of strings. For example, for a query "where can i find the top sales?", return ['1']

catalog = {}
"""

generation_config = {
    "max_output_tokens": 1000,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

def generate(request, catalog, system_instructions_template=default_instructions, generation_config=generation_config, safety_settings=safety_settings):
  system_instructions = system_instructions_template.format(catalog)

  vertexai.init(project="queryable-dashboard-catalog", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-pro-001",
    system_instruction=[system_instructions]
  )
  responses = model.generate_content(
      [request],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )
  raw_response = "".join([response.text for response in responses])
  print(raw_response)
  json_response = raw_response.replace("\n", "").replace("'", '"')
  return json.loads(json_response)


def get_dashboards(request, catalog, instructions_template):
  gemini_r = generate(request, catalog, instructions_template)
  return [{"link": f"https://hack.looker.com/dashboards/{r}", "title": catalog[r]["title"]}
          for r in gemini_r[:5]]