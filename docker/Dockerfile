FROM jupyter/pyspark-notebook

RUN python --version

RUN conda install --quiet --yes -c \
    conda-forge jupyter_contrib_nbextensions jupyter_nbextensions_configurator

RUN pip install -U networkx \
                   sklearn \
                   plotly \
                   dash \
                   geopandas \
                   folium \
                   gif \
                   descartes \
                   cufflinks \
                   rise

RUN jupyter labextension install @jupyterlab/toc && \
jupyter-nbextension install rise --py --sys-prefix && \
jupyter-nbextension enable rise --py --sys-prefix

VOLUME /home/jovyan/work
WORKDIR /home/jovyan/work
