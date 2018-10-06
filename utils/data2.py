import logging
from datetime import datetime

import pandas as pd
from Bio import SeqIO

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Guess: Feather is a fast, lightweight, and easy-to-use binary file format for storing data frames. 

def load_sequence_and_metadata(kind='feather'):
    """
    Returns the sequences as a list of SeqRecords, and metadata as a pandas
    DataFrame.
    """
    
    starttime = datetime.now()
    
    # *********** loading sequences *************
    if kind == 'addH3N2':
        sequences = [s for s                 
                     in SeqIO.parse('data/2000_2014_H3N2_global_626844955318.fasta', 'fasta')                                                                              
                     ]
    elif kind == 'pH1N1':          
        sequences = [s for s                 
                     in SeqIO.parse('data/2000_2018-pH1N1-global_87279350985.fasta', 'fasta')                                                                              
                     ]    
    elif kind == 'xpH1N1':          
        sequences = [s for s                 
                     in SeqIO.parse('data/2000_2018-xpH1N1-global_263410394807.fasta', 'fasta')                                                                              
                     ]            
    else:
        sequences = [s for s
                     in SeqIO.parse('data/20170531-H3N2-global.fasta', 'fasta')                            
                     ]  
        
        
    # *********** loading metadata *************
    if kind == 'addH3N2':          
        metadata = pd.read_csv('data/2000_2014_H3N2_global_589817715540-Results.tsv',
                               sep='\t',
                               parse_dates=['Collection Date'])
    elif kind == 'pH1N1': 
        metadata = pd.read_csv('data/2000_2018-pH1N1-global_287558903998.tsv',        
                               sep='\t',
                               parse_dates=['Collection Date'])         
    elif kind == 'xpH1N1': 
        metadata = pd.read_csv('data/2000_2018-xpH1N1-global_296089903487.tsv',        
                               sep='\t',
                               parse_dates=['Collection Date'])            
    elif kind == 'csv': 
        metadata = pd.read_csv('data/20170531-H3N2-global.tsv',        
                               sep='\t',
                               parse_dates=['Collection Date'])                  
    elif kind == 'feather':
        metadata = pd.read_feather('data/20170531-H3N2-global.feather')        
        
    endtime = datetime.now()
    elapsed = endtime - starttime
    print(f'load_sequence_and_metadata() took {elapsed} seconds.')
    return sequences, metadata

def load_prediction_coordinates():
    """
    Returns the coordinates of the predictions, and their associated colours,
    as a pandas DataFrame.
    """
    logger.debug('started load_prediction_coordinates()')
    df = pd.read_csv('data/oneQ_prediction_coords_with_colors.csv',
                     index_col=0)
    logger.debug('finished load_prediction_coordinates()')
    return df
