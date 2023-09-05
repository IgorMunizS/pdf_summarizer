
# PDF Summarizer      

This repository implements a solution using LLM to summarize a PDF File. 

Using PyPDF2, Langchain and OpenAI, my approach was to extract all the text from a PDF file and then split it into chunks of up to 4000 tokens so that it can be sent to LLM. As LLM, ChatGPT-3.5-Turbo-16k was used to perform the summarization. Langchain was used for flow orchestration and integration with the OpenAI API.
Additionally, a map-reduce approach was used where it summarize each document on it's own in a "map" step and then "reduce" the summaries into a final summary.

At the end, an API is available in which a summary is returned given a PDF file, and also a UI for testing the application using Gradio.

This tool presents potential use cases for academic research with summarizing articles and book chapters, business document management summarizing reports, recruitment and HR summarizing CVs and also in the IT area with summarizing log files and technical documents.


## Quick start

Start the project with docker-compose
```bash
 docker-compose up
```

The application may take a few minutes to run the build due to the installation of packages in the conda environment.
After the process of building the images is finished, go to `http://127.0.0.1:7861/`  

## Environment variables

To run this project, you will need to add the following environment variables to your .env

`API_HOST`
`API_PORT`
`OPENAI_API_KEY`

e.g

```
API_HOST=0.0.0.0
API_PORT=8000
OPENAI_API_KEY=sk-
```









## Stack


**Back-end:** Python 3.10, Langchain, OpenAI, PyPDF2



## API Documentation




#### Endpoint for generating a response to a question using LLM

```http
  POST /summarize
```

| Param  | Type         | Description                              |
|:-------|:-------------|:-----------------------------------------|
| `file` | `Bytes File` | **Required**. PDF File to be summarized  |



+ Request (application/json)

    + Body

            curl --location 'http://0.0.0.0:8000/summarize' --form 'file=@"/home/igor/Portfolio/Testes/b20Labs/pdf-summarizer/data/s43588-022-00234-z.pdf"'

+ Response 200 (application/json)

    + Body

            {
                "summary": "This a summary"
            }


## Live DEMO
https://d43697e57f7e6269ef.gradio.live