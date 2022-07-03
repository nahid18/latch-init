"""
Rapid efficient extraction of SNPs from multi-FASTA alignments
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile, LatchDir


@small_task
def snp_sites_task(
    aln: LatchFile,
    is_m: bool = True,
    is_r: bool = False
) -> LatchFile:
    log_file = Path(f"/root/snp_sites_log.txt")
    output_dir = Path(f"/root/SNPsitesRun/")

    _snp_cmd = [
            "snp-sites", 
            "-V", 
        ]

    with open(log_file, "w") as f:
            subprocess.run(_snp_cmd, stdout=f, stderr=f)

    return LatchFile(str(log_file), f"latch://{log_file}")


@workflow
def snp_sites(
    aln: LatchFile, 
    is_m: bool = True,
    is_r: bool = False
) -> LatchFile:
    """Rapid efficient extraction of SNPs from multi-FASTA alignments

    SNP-sites
    ----

    ## SNP-sites: rapid efficient extraction of SNPs from multi-FASTA alignments

    Rapidly decreasing genome sequencing costs have led to a proportionate increase in the number of samples used in prokaryotic population studies. Extracting single nucleotide polymorphisms (SNPs) from a large whole genome alignment is now a routine task, but existing tools have failed to scale efficiently with the increased size of studies. These tools are slow, memory inefficient and are installed through non-standard procedures. We present SNP-sites which can rapidly extract SNPs from a multi-FASTA alignment using modest resources and can output results in multiple formats for downstream analysis. SNPs can be extracted from a 8.3 GB alignment file (1,842 taxa, 22,618 sites) in 267 seconds using 59 MB of RAM and 1 CPU core, making it feasible to run on modest computers. It is easy to install through the Debian and Homebrew package managers, and has been successfully tested on more than 20 operating systems. SNP-sites is implemented in C and is available under the open source license GNU GPL version 3.

    ## Citation

    "SNP-sites: rapid efficient extraction of SNPs from multi-FASTA alignments", Andrew J. Page, Ben Taylor, Aidan J. Delaney, Jorge Soares, Torsten Seemann, Jacqueline A. Keane, Simon R. Harris, [Microbial Genomics 2(4), (2016)](http://mgen.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.000056)



    __metadata__:
        display_name: SNP-sites
        author:
            name:
            email:
            github:
        repository:
        license:
            id: MIT

    Args:

        aln:
          Alignment file in FASTA format
          __metadata__:
            display_name: Alignment File

        is_m:
          Generate a multi fasta alignment file output
          __metadata__:
            display_name: Output a multi fasta alignment file

        is_r:
          Generate internal pseudo reference sequence output
          __metadata__:
            display_name: Output internal pseudo reference sequence

    """
    return snp_sites_task(aln=aln, is_m=is_m, is_r=is_r)
