#!/bin/sh

DIR1=007_bam
INCOMING=${DIR1}/pg_007_05_tiny1.clean.bam.sam
OUTGOING=${DIR1}/pg_007_06_tiny1.offset.bam
CHROM_LENGTH=145138636  # length of myc chromosome
OFFSET=$(cat 001_data/001_reference/myc_offset.txt)
#-----------------------------------------------------------------------------80
# Replace the length of the reference sequence in the header
# and shift the alignment positions by OFFSET.
#-----------------------------------------------------------------------------80
sed -E "s/LN:[0-9]+/LN:$CHROM_LENGTH/" ${INCOMING} | \
  awk -v offset=${OFFSET} -v OFS='\t' -F'\t' '/^@/ {print} !/^@/ {$4=$4+offset; print}' > ${OUTGOING}.sam

samtools view -bS ${OUTGOING}.sam > ${OUTGOING}
samtools index ${OUTGOING}
