<body lang="en-HK" dir="ltr">
<h2 class="western">History</h2>
<p style="margin-bottom: 0in; line-height: 100%">There have been
about 9 influenza pandemics during the last 300 years. The worst is
the  1918 Spanish influenza pandemic, with record of deaths of
approximately 50–100 million people [1]. There have been about
three influenza pandemics in each century and the most recent one was
the 2009 flu pandemic. The pandemic began in <u>November 2009</u> and
was ended on <u>10 August 2010</u> [2].</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%">Spanish Flu
	in 1918</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 100%">Asian Flu in
	1957</p>
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
criteria</font></font></p>
<table width="642" cellpadding="4" cellspacing="0">
	<col width="632">
	<tr>
		<td width="632" valign="top" style="border: 1px solid #000000; padding: 0.04in">
			<p><font color="#000000">Data Type: Protein; Virus Type: A;
			Subtype: H1N1; Date range: <font color="#0000ff">2000 to 2018</font>;
			'Classical' Proteins: Complete? HA</font></p>
		</td>
	</tr>
</table>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%">it returns <font color="#0000ff">22,403</font>
proteins</p>
<p style="margin-bottom: 0in; line-height: 100%">Download ticket:
<font color="#0000ff">28200724868</font></p>
<p style="margin-bottom: 0in; line-height: 100%">Downloaded filename:
<span style="background: #ffff00">28200724868-2000_2018-H1N1-global.</span><span style="background: #ffff00">tsv</span>
(<font color="#0000ff">2</font><font color="#0000ff">.1 MB</font>) 
</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<br/>

</p>
<table width="642" cellpadding="4" cellspacing="0">
	<col width="632">
	<tr>
		<td width="632" valign="top" style="border: 1px solid #000000; padding: 0.04in">
			<p><font color="#000000">Data Type: Genome Segments; Virus Type:
			A; Subtype: H1N1; Date range: <font color="#0000ff">2000 to 2018</font>;
			'Classical' Proteins: Complete? HA; Download options: Segment
			FASTA | Custom format: Accession Number</font></p>
		</td>
	</tr>
</table>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%">it returns <font color="#0000ff">11,264</font>
segments</p>
<p style="margin-bottom: 0in; line-height: 100%">Download ticket:
<font color="#0000ff">626844955318</font></p>
<p style="margin-bottom: 0in; line-height: 100%">Downloaded filename:
<span style="background: #ffff00">626844955318-2000_2018-H1N1-global</span><span style="background: #ffff00">.fasta</span>
(9.9 MB) 
</p>
<p style="margin-left: 0.49in; margin-bottom: 0in; line-height: 100%">
<br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><span style="background: #ffff00">update
utils/data.py</span> for according to the downloaded fileanames</p>
<p style="margin-bottom: 0in; line-height: 100%">The test data is set
after November 2009 when the pandemic of Swine Flu occurred. In
addition, the following code is added to select only “Complete
Genome” of downloaded protein sequence.</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%">Training data: 2000
to 2018 (exclude testing data) 
</p>
<p style="margin-bottom: 0in; line-height: 100%">Testing data:
&gt;=1.11.2009 and &lt;=10.8.2010</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%">I use the approach
stated by Eric Ma who uses deep learning &amp; genotype network-based
system for predicting new influenza protein sequences. You can check
out details at <a href="https://fluforecaster.herokuapp.com/">HeroKu</a>
and the code <a href="https://github.com/ericmjl/flu-sequence-predictor/">here</a>.
Eric translates sequences to &quot;latent&quot; representation by
variational autoencoder (VAE) and then he uses Gaussian Processes
(GPs) regression model to predict future sequences. Then he use the
variational autoencoder model to learn a latent representation of
discrete sequence space as a continuous representation. <a href="https://wiseodd.github.io/techblog/2016/12/10/variational-autoencoder/">VAE
</a>models the underlying probaility distribution of data and the
resulting models are saved under the trained_models sub-folder.
Sequences are processed by the Biopython package (<a href="http://biopython.org/DIST/docs/tutorial/Tutorial.html">Tutorial</a>)
to process the downloaded sequence data.  
</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 100%"><br/>

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
<p style="margin-bottom: 0in; line-height: 100%"><br/>

</p>
<h2 class="western"></h2>
</body>
