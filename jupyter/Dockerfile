FROM  jupyter/base-notebook:python-3.8.8
WORKDIR /jupyter
RUN rm /home/jovyan/.jupyter/jupyter_notebook_config.py
COPY jupyter_notebook_config.py /home/jovyan/.jupyter
COPY jupyter_notebook_config.json /home/jovyan/.jupyter
RUN pip install psycopg2-binary
RUN pip install matplotlib
RUN pip install pandas
CMD jupyter notebook