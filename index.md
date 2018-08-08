
<body lang="en-HK" dir="ltr">
<h2 class="western">History</h2>
<p style="margin-bottom: 0in; line-height: 100%">There have been
about 9 influenza pandemics during the last 300 years. The worst is
the  1918 Spanish influenza pandemic, with record of deaths of
approximately 50–100 million people [1]. There have been about
three influenza pandemics in each century and the most recent one was
the 2009 flu pandemic. The pandemic began in November 2009 and was
ended on 10 August 2010 [2].</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<h2 class="western">Data processing</h2>
<p style="margin-bottom: 0in; line-height: 100%">Data of protein
sequences can be obtained from <a href="https://www.fludb.org/brc/influenza_sequence_search_segment_display.spg?method=ShowCleanSearch&amp;decorator=influenza">Influenza
Research Database (IRD)</a> in e.g. fasta format and use the
Biopython package (<a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html">Tutorial</a>)
to process the downloaded sequence data.  
</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%">I use the approach
stated by Eric Ma who uses deep learning &amp; genotype network-based
system for predicting new influenza protein sequences. You can check
out details at <a href="https://fluforecaster.herokuapp.com/">HeroKu</a>
and the code <a href="https://github.com/ericmjl/flu-sequence-predictor/">here</a>.
Eric translates sequences to &quot;latent&quot; representation by
variational autoencoder (VAE) and then he uses Gaussian Processes
(GPs) regression model to predict future sequences.</p>
<p style="margin-bottom: 0in; line-height: 100%"> 
</p>
<h2 class="western">References</h2>
<ol>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%"><a name="__RefNumPara__77_1186524692"></a>
	Nicholls H (2006). &quot;Pandemic influenza: the inside story&quot;.
	PLoS Biol. 4 (2): e50. doi:10.1371/journal.pbio.0040050. PMC
	1363710 Freely accessible. PMID 16464130.</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%"><a name="__RefNumPara__79_1186524692"></a>
	&quot;WHO/Europe | WHO Director-General declares H1N1 pandemic
	over&quot;. World Health Organization (WHO). 10 August 2010.
	Archived from the original on 25 May 2011. Retrieved 24 May 2011.</p>
</ol>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
</body>

