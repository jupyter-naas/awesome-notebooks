# %pip install pyvis
# run: python pyvis_naas.py data.json
# result: naas_graph.html
# logs: wrong_naas_logo.log

# Imports
import pandas as pd
from pyvis.network import Network
import logging
import argparse
import os
import sys

# Function to import data
def import_data(file):
    # Check if file exists
    if not os.path.exists(file):
        print(f"File {file} does not exist.")
        sys.exit(1)

    if  file.endswith('.json'):
        df = pd.read_json(file)
    elif file.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        print(f"File {file} is not a JSON or CSV file.")
        sys.exit(1)
   
    # Sanity check
    if isinstance(df, pd.DataFrame) and len(df.columns) > 0 and len(df) > 0:
        print("\nDataframe created successfully!")
    else:
        df = None
    
    return df

# Function to create the graph 
def create_graph(df_temp):

    # Initializing the Pyvis network
    net=Network(height='1400px', width='100%', bgcolor='#222222', font_color='white')

    # Physics solver
    net.force_atlas_2based()

    # Getting data
    tools = list(df_temp['tool'])
    images = list(df_temp['image_url'])
    notebooks = list(df_temp['notebook'])

    # Creating a dictionary of tool and image
    tool_img = dict(zip(tools, images))

    # Adding tool nodes
    for tool in tools:
        if tool == 'Naas':
            net.add_node(tool, title=tool, image=tool_img[tool], shape='image', size=150, level=1, borderWidth = 500, fixed=True, x=0, y=0,physics=False)
        if tool == 'OpenAI':
            #this node was bouncing around very fast, so I fixed it
            net.add_node(tool, title=tool, image=tool_img[tool], shape='image', size=60, level=1, fixed=True, x=-1000, y=2000, physics=False)
        else:
            net.add_node(tool, title=tool, image=tool_img[tool], shape='image',size=60,level=1, physics=False)

    # Adding notebook nodes
    for notebook in notebooks:
        net.add_node(notebook, title=notebook, size=30,level=2,color='#4d94db')
        
    # Adding edges
    for _, node_e in df_temp.iterrows():
        net.add_edge(node_e['tool'], node_e['notebook'], title=node_e['action'])

    # Saving the network to a HTML file
    net.write_html('naas_graph.html')

    # Sanity checks
    # checking if nodes showing wrong naas-logo image
    naas_logo = 'https://raw.githubusercontent.com/jupyter-naas/awesome-notebooks/master/.github/assets/logos/Naas.png'

    # set up logging
    logging.basicConfig(filename='wrong_naas_logo.log', level=logging.WARNING)
    for tool in tools:
        if tool_img[tool] == naas_logo and tool != 'Naas':
            logging.warning(f'{tool} {tool_img[tool]}')
    # end of sanity checks
    
    return net

# Main function
if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("json_csv_file", help="The JSON or CSV file to process")

    # Parse arguments
    args = parser.parse_args()
    file = args.json_csv_file

    # Import data
    df_temp = import_data(file)
    if df_temp is None:
        print("\nSomething went wrong with the data import.")
        exit(1)

    # Create network
    net = create_graph(df_temp)

     # Check the properties of the returned Network object
    if  isinstance(net, Network):
        print("Network created successfully! \n")    
    else:
        print("\nSomething went wrong with the network creation.\n")
        exit(1)
    
    # Print some network information
    level_1_count = 0
    level_2_count = 0
    for node in net.nodes:
        if node['level'] == 1:
            level_1_count += 1
        else:
            level_2_count += 1
    
    print("Number of tool nodes: ", level_1_count)
    print("Number of notebook nodes: ", level_2_count)
    print("Total number of nodes: ", len(net.nodes) , "\n")
    print("Total number of edges: ", len(net.edges), "\n")

    
