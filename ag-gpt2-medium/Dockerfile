FROM tensorflow/serving:latest

RUN apt-get update && \
    apt-get install -y git

RUN git clone https://huggingface.co/gpt2-medium

ENV MODEL_NAME=gpt2-medium
ENV MODEL_BASE_PATH=/models/${MODEL_NAME}
ENV MODEL_PATH=${MODEL_BASE_PATH}/1

RUN mkdir -p ${MODEL_PATH}
RUN cp -r gpt2-medium/* ${MODEL_PATH}

EXPOSE 8500

ENTRYPOINT ["tensorflow_model_server"]

CMD ["--port=8500", "--rest_api_port=8501", "--model_name=gpt2-medium", "--model_base_path=/models/gpt2-medium/1"]
