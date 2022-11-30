FROM jupyter/minimal-notebook

LABEL author="Maximilian Schiedermeier"

## Copy notebook and all data in the container
COPY Restify.ipynb /home/jovyan/Restify.ipynb
COPY csv_tools /home/jovyan/csv_tools
COPY jupyter_snippets /home/jovyan/jupyter_snippets
COPY restify_mining /home/jovyan/restify_mining
COPY source-csv-files /home/jovyan/source-csv-files
RUN mkdir -p /home/jovyan/generated-csv-files
RUN mkdir -p /home/jovyan/generated-plots
RUN ls -al /home/jovyan


## Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID
