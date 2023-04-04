# agbrain
---

In this study, we gathered data from various sources including webpages and PDF documents that are publicly available on the internet.
The majority of the data was derived from PDF documents, with a total of 1601 documents included in our dataset. The data was then utilized 
to refine the GPT2 model for generation task.

To ensure the safety and reliability of the generated content, we implemented an unsupervised model between the endpoint and the GPT2 model. 
This model is designed to guide users' prompts towards producing content that is relevant and unbiased, while avoiding any offensive or unsafe outputs.
Despite the extensive training of the GPT2 model, there is still a possibility of undesirable outputs. 
Therefore, the incorporation of the unsupervised model serves as an additional layer of protection to enhance the safety and quality of the generated content.
