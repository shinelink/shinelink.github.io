## Seasonal Flu

Seasonal influenza is a common respiratory tract infection caused by human seasonal influenza viruses. In Hong Kong, seasonal influenza  is usually more common in periods from January to March and from July to August.

Influenz A(H3N2) had the greatest impact, contributing around half of the excess respiratory mortality and respiratory
hospitalizations on average, with influenza B contributing the second largest average during the study period of
15.5 years from 1998 through 2013[1].

## History
There have been about 9 influenza pandemics during the last 300 years. The worst is the 1918 Spanish influenza pandemic, with record of deaths of approximately 50–100 million people [2]. There have been about three influenza pandemics in each century and the most recent one was the 2009 flu pandemic. The pandemic began to taper off in November 2009 and was ended on On 10 August 2010[3]



<!--
The outbreaks of severe acute respiratory syndrome (SARS) started from 11 February 2003 when the World Health Organization first received reports from China on an outbreak of acute respiratory syndrome occurred in Guangdong province, to 28 May 2004 when the Hong Kong government lowered the Alert Level of SARS response system <a class="ptr">[1]</a>.
//-->

## Data processing
Data can be obtained from <a href='https://www.fludb.org/brc/influenza_sequence_search_segment_display.spg?method=ShowCleanSearch&decorator=influenza'>Influenza Research Database (IRD)</a> in e.g. fasta format and use the Biopython package (<a href='http://biopython.org/DIST/docs/tutorial/Tutorial.html'>Tutorial</a>) to process the downloaded sequence data.  

I use the approach stated by Eric Ma who uses deep learning & genotype network-based system for predicting new influenza protein sequences. You can check out details at <a href='https://fluforecaster.herokuapp.com/'>HeroKu</a> and the code <a href='https://github.com/ericmjl/flu-sequence-predictor/'>here</a>. Eric translates sequences to "latent" representation by variational autoencoder (VAE) and then uses Gaussian Processes (GPs) regression model to predict future sequences.


## Useful links

Information from the Centre for Health Protection in Hong Kong:

<li><a href='https://www.chp.gov.hk/en/static/24012.html'>The number of notifiable infectious diseases</a>
<li><a href='https://www.chp.gov.hk/en/statistics/data/10/641/642/2274.html'>Statistics on Laboratory Surveillance > Detection of pathogens from respiratory specimens</a>
<li><a href='https://www.chp.gov.hk/en/statistics/data/10/641/643/2275.html'>Statistics on Laboratory Surveillance > Influenza Virus Subtyping</a>
  
## References
<ol id="references">
        <li>Peng Wu, Anne M. Presanis, Helen S. Bond, Eric H. Y. Lau, Vicky J. Fang & Benjamin J. Cowling Scientific Reportsvolume 7, Article number: 929 (2017) 
        <li> Nicholls H (2006). "Pandemic influenza: the inside story". PLoS Biol. 4 (2): e50. doi:10.1371/journal.pbio.0040050. PMC 1363710 Freely accessible. PMID 16464130.
        <li>"WHO/Europe | WHO Director-General declares H1N1 pandemic over". World Health Organization (WHO). 10 August 2010. Archived from the original on 25 May 2011. Retrieved 24 May 2011.
</ol>  

