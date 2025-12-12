from csv import DictReader, DictWriter
from pathlib import Path


DIR1 = Path("001_data/001_reference")
INPUT1 = "chr8.gtf"
INPUT2 = "chr8.fa"
INPUT3 = "genes.refFlat"

GENEID = "ENSG00000136997"
OUTPUT1 = "myc.gtf"
OUTPUT2 = "myc.fa"
OUTPUT3 = "myc.refFlat"

gtf_fieldnames = [
    "seqname",
    "source",
    "feature",
    "start",
    "end",
    "score",
    "strand",
    "frame",
    "attribute",
]
refFlat_fieldnames = [
    "geneName",
    "name",
    "chrom",
    "strand",
    "txStart",
    "txEnd",
    "cdsStart",
    "cdsEnd",
    "exonCount",
    "exonStarts",
    "exonEnds",
]

if __name__ == "__main__":
    # read GTF file
    with open(DIR1 / INPUT1, "r") as f:
        reader = DictReader(f, delimiter="\t", fieldnames=gtf_fieldnames)
        # extract lines for gene of interest & get range of gene
        myc_gtf = []
        start = 2**31
        end = 0
        for row in reader:
            if GENEID in row["attribute"]:
                myc_gtf.append(row)

                start = min(start, int(row["start"]))
                end = max(end, int(row["end"]))

    # calculate offset
    start_line = start // 60
    end_line = end // 60
    offset = start_line * 60

    # save offset
    with open(DIR1 / "myc_offset.txt", "w") as f:
        f.write(str(offset) + "\n")

    # write GTF file with offset locations
    with open(DIR1 / OUTPUT1, "w") as f:
        writer = DictWriter(f, delimiter="\t", fieldnames=gtf_fieldnames)
        for row in myc_gtf:
            row["start"] = str(int(row["start"]) - offset)
            row["end"] = str(int(row["end"]) - offset)
            writer.writerow(row)

    # extract sequence from FASTA file
    with open(DIR1 / INPUT2, "r") as in_f, open(DIR1 / OUTPUT2, "w") as out_f:
        out_f.write(in_f.readline())  # write header
        for line_idx, line in enumerate(in_f):
            if (line_idx < start_line) or (line_idx > end_line):
                continue
            out_f.write(line)

    # read & write refFlat file with offset locations
    with open(DIR1 / INPUT3, "r") as in_f, open(DIR1 / OUTPUT3, "w") as out_f:
        reader = DictReader(in_f, delimiter="\t", fieldnames=refFlat_fieldnames)
        writer = DictWriter(out_f, delimiter="\t", fieldnames=refFlat_fieldnames)
        for row in reader:
            if row["geneName"] == GENEID:
                row["txStart"] = str(int(row["txStart"]) - offset)
                row["txEnd"] = str(int(row["txEnd"]) - offset)
                row["cdsStart"] = str(int(row["cdsStart"]) - offset)
                row["cdsEnd"] = str(int(row["cdsEnd"]) - offset)
                row["exonStarts"] = ",".join(
                    [str(int(x) - offset) for x in row["exonStarts"].split(",")[:-1]]
                )
                row["exonEnds"] = ",".join(
                    [str(int(x) - offset) for x in row["exonEnds"].split(",")[:-1]]
                )
                writer.writerow(row)
