History
There have been about 9 influenza pandemics during the last 300 years. The worst is the  1918 Spanish influenza pandemic, with record of deaths of approximately 50–100 million people [1]. There have been about three influenza pandemics in each century and the most recent one was the 2009 flu pandemic. The pandemic began in November 2009 and was ended on 10 August 2010 [2].
Spanish Flu in 1918
Asian Flu in 1957
Hong Kong Flu in 1968
Swine Flu in 2009
where 2009 is the only pandemic with large scale labeled sequences for analysis.

Data processing
Data of protein sequences can be obtained from Influenza Research Database (IRD) in e.g. fasta format. To obtain the data, make the following selection:

Selection criteria
Data Type: Protein; Virus Type: A; Subtype: H1N1; Date range: 2000 to 2018; 'Classical' Proteins: Complete? HA

it returns 22,403 proteins
Download ticket: 28200724868
Downloaded filename: 28200724868-2000_2018-H1N1-global.tsv (2.1 MB) 

Data Type: Genome Segments; Virus Type: A; Subtype: H1N1; Date range: 2000 to 2018; 'Classical' Proteins: Complete? HA; Download options: Segment FASTA | Custom format: Accession Number

it returns 11,264 segments
Download ticket: 626844955318
Downloaded filename: 626844955318-2000_2018-H1N1-global.fasta (9.9 MB) 

update utils/data.py for according to the downloaded fileanames
The test data is set after November 2009 when the pandemic of Swine Flu occurred. In addition, the following code is added to select only “Complete Genome” of downloaded protein sequence.

Training data: 2000 to 2018 (exclude testing data) 
Testing data: >=1.11.2009 and <=10.8.2010

I use the approach stated by Eric Ma who uses deep learning & genotype network-based system for predicting new influenza protein sequences. You can check out details at HeroKu and the code here. Eric translates sequences to "latent" representation by variational autoencoder (VAE) and then he uses Gaussian Processes (GPs) regression model to predict future sequences. Then he use the variational autoencoder model to learn a latent representation of discrete sequence space as a continuous representation. VAE models the underlying probaility distribution of data and the resulting models are saved under the trained_models sub-folder. Sequences are processed by the Biopython package (Tutorial) to process the downloaded sequence data.  

During my own testing, the outcome of the data for the latent space and Sanity check (Euclidean and Levenshtein distances relationship) are different from the original data (downloaded on 31 May 2017) in the sense that the latent representation in my sample is more scatter while the linear relationship of Sanity check no longer maintained. 

To work out the reason making the different result, I downloaded H3N2 data from IRD from 2000 to 2014 for testing (downloaded on 28 Aug 2018) while screen out the original data for the same period of time for comparison.  The result for the  data of the original data was as follows:
