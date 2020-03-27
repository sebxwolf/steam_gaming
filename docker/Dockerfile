FROM jupyter/pyspark-notebook

RUN python --version

RUN conda install --quiet --yes -c \
    conda-forge jupyter_contrib_nbextensions jupyter_nbextensions_configurator

RUN pip install -U networkx \
                   sklearn \
                   plotly
VOLUME /home/jovyan/work
WORKDIR /home/jovyan/work
