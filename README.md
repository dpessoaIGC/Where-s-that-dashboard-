<h1><span style="color:#2d7eea">Looker Vertex AI Hackathon: Where's that dashboard?</span></h1>

<h2><span style="color:#2d7eea">Overview</span></h2>
Task: How can a non-technical person find the most relevant Looker dashboard for their need expressed in plain text?

Solution: A BQML implementation of the Gemini Vertex AI LLM to parse the list of all dashboards titles. This list of titles is obtained using a Python query of the Looker API. The BQML model returns the title of the dashboard that is the most similar to the request input into the Looker dashboard that hosts the dashboard search functionality.

<h2><span style="color:#2d7eea">Exploring</span></h2>


<h2><span style="color:#2d7eea">Development</span></h2>

```bash
pyenv install 3.10.12
pyenv virtualenv 3.10.12 wheredashboard
pyenv local wheredashboard
pip install poetry
poetry install
```

<h2><span style="color:#2d7eea">Additional Resources</span></h2>
