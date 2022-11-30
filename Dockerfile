FROM jupyter/minimal-notebook

LABEL author="Maximilian Schiedermeier"

## Acclaim room priviledges so we can modify the container content
USER root

## Copy notebook and all data in the container
COPY Restify.ipynb /work/Restify.ipynb
COPY csv_tools /work/csv_tools
COPY jupyter_snippets /work/jupyter_snippets
COPY restify_mining /work/restify_mining
COPY source-csv-files /work/source-csv-files
#RUN mkdir -p /work/generated-csv-files
#RUN mkdir -p /work/generated-plots
RUN ls -al /work

# Give general access to work folder
#RUN chmod 777 /work

# See: https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f#0ba2
# Install co-dependencies
#RUN pip install pandas numpy matplotlib plotly

## Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID
