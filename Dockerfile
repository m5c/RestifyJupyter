# See: https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f#0ba2
FROM jupyter/minimal-notebook

LABEL author="Maximilian Schiedermeier"

# Switch off that anoying token thingy
RUN cd ~/.jupyter; jupyter notebook --generate-config; sed -i "s/.*c.ServerApp.token.*/c.ServerApp.token = \'\'/g" jupyter_notebook_config.py
RUN cd ~/.jupyter; jupyter notebook --generate-config; sed -i "s/.*c.ServerApp.token.*/c.ServerApp.token = \'\'/g" jupyter_server_config.py

## Copy notebook and all data in the container
COPY Restify.ipynb /home/jovyan/Restify.ipynb
COPY static-figures /home/jovyan/static-figures
COPY csv_tools /home/jovyan/csv_tools
COPY jupyter_snippets /home/jovyan/jupyter_snippets
COPY restify_mining /home/jovyan/restify_mining
COPY source-csv-files /home/jovyan/source-csv-files
RUN mkdir -p /home/jovyan/generated-csv-files
RUN mkdir -p /home/jovyan/generated-plots
RUN mkdir -p /home/jovyan/generated-text-files
RUN ls -al /home/jovyan

# Install co-dependencies
RUN pip install pandas numpy matplotlib plotly scipy statsmodels seaborn

## Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

## Override default lab startup command of minimal-notebook image
EXPOSE 8889
CMD ["sh", "-c", "echo \"Your RESTify Notebook is up and running: http://127.0.0.1:8889/notebooks/Restify.ipynb\"; jupyter notebook --port=8889 /home/jovyan/Restify.ipynb --no-browser --allow-root --ip=* --NotebookApp.token=\"\" --NotebookApp.password=\"\" >/dev/null 2>&1"]
