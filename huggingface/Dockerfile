FROM python:3.9-slim-buster

COPY . /endpoint/

WORKDIR /endpoint/

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt


ENV A=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 
ENV B=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 
ENV C=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
ENV D=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 
ENV E=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 
ENV F=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 
ENV G=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 
ENV H=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 
ENV I=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 
ENV J=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

ENV AGBRAIN=https://api-inference.huggingface.co/models/benkimz/agbrain
ENV GPT2_LARGE=https://api-inference.huggingface.co/models/gpt2-large
ENV SUMMARIZER=https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum

EXPOSE 8765

ENTRYPOINT ["python", "api.py"]