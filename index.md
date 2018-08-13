<body lang="en-HK" dir="ltr">
<h2 class="western">History</h2>
<p style="margin-bottom: 0in; line-height: 100%">There have been
about 9 influenza pandemics during the last 300 years. The worst is
the  1918 Spanish influenza pandemic, with record of deaths of
approximately 50–100 million people [1]. There have been about
three influenza pandemics in each century and the most recent one was
the 2009 flu pandemic. The pandemic began in November 2009 and was
ended on 10 August 2010 [2].</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%">Spanish Flu
	in 1918</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%">Asian Flu in
	1957f</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%">Hong Kong Flu
	in 1968</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%; text-decoration: none">
	Swine Flu in 2009</p>
</ul>
<p style="margin-bottom: 0in; line-height: 100%">where 2009 is the
only pandemic with large scale labeled sequences for analysis.</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<h2 class="western">Data processing</h2>
<p style="margin-bottom: 0in; line-height: 100%">Data of protein
sequences can be obtained from <a href="https://www.fludb.org/brc/influenza_sequence_search_segment_display.spg?method=ShowCleanSearch&amp;decorator=influenza">Influenza
Research Database (IRD)</a> in e.g. fasta format. To obtain the data,
make the following selection:</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-top: 0.17in; margin-bottom: 0.08in; line-height: 100%; page-break-after: avoid">
<font face="Liberation Sans, sans-serif"><font size="4" style="font-size: 14pt">Selection
of the 2009 pandemic:</font></font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Data Type: Genome Segments</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Virus Type: A</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Subtype: H1N1</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Date range: 2009 to 2010</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Complete Genome Only</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Segments: HA</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">select “2009 pH1N1 Sequence”</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">	Similarity (SOP) </font>
</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">		“Only pH1N1”</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Host: Human</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Country: USA</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Download options:</font></p>
<p style="margin-left: 0.98in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Segment FASTA</font></p>
<p style="margin-left: 0.98in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">Custom format:</font></p>
<p style="margin-left: 0.98in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">	Accession Number</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<br/>

</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
it returns 1470 segments.</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
Name: 2009_2010_pH1N1.fasta</p>
<p style="margin-top: 0.17in; margin-bottom: 0.08in; line-height: 100%; page-break-after: avoid">
<font face="Liberation Sans, sans-serif"><font size="4" style="font-size: 14pt">Download
non-pandemic sequences:</font></font></p>
<p style="margin-bottom: 0in; line-height: 100%">	same selection
criteria except: 
</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">select “2009 pH1N1 Sequence”</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">	Similarity (SOP) </font>
</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<font color="#006666">		“Exclude pH1N1”</font></p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<br/>

</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
it returns 198 segments.</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
Your search history: 2009-2010 Exclude pH1N1</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
Name: 2009_2010_non_pH1N1.fasta</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%">Sequences are
processed by the Biopython package (<a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html">Tutorial</a>)
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
