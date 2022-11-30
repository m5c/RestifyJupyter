# See: https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f#0ba2
FROM jupyter/minimal-notebook

LABEL author="Maximilian Schiedermeier"

# Switch off that anoying token thingy
RUN cd ~/.jupyter; jupyter notebook --generate-config; sed -i "s/.*c.NotebookApp.token.*/c.NotebookApp.token = \'\'/g" jupyter_notebook_config.py

## Copy notebook and all data in the container
COPY Restify.ipynb /home/jovyan/Restify.ipynb
COPY csv_tools /home/jovyan/csv_tools
COPY jupyter_snippets /home/jovyan/jupyter_snippets
COPY restify_mining /home/jovyan/restify_mining
COPY source-csv-files /home/jovyan/source-csv-files
RUN mkdir -p /home/jovyan/generated-csv-files
RUN mkdir -p /home/jovyan/generated-plots
RUN ls -al /home/jovyan

# Install co-dependencies
#RUN pip install pandas numpy matplotlib plotly scipy

## Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID
