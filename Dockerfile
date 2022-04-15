FROM python:3.8
# Change to root for the following tasks.
USER root
# -- [Required]
ENV APP=/app
COPY . $APP

RUN chgrp -R 0 $APP && chmod -R 770 $APP
# Speed up download and instalation of dependencies, if possible.
COPY ./requirements.txt $APP/
RUN pip install --upgrade pip && \
    pip install -r $APP/requirements.txt --no-cache-dir

ENV PYTHONPATH=$APP

CMD sh $APP/api.sh