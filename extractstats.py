import os
import glob

def process_annotation_files(genome_name):
    # File names
    anno_file = f"{genome_name}_anno.out"
    de_file = f"{genome_name}_DE.out"
    go_file = f"{genome_name}_GO.out"

    # Process B*_anno.out
    with open(anno_file, "r") as f:
        anno_lines = f.readlines()
    anno_genes = {line.split("\t")[0] for line in anno_lines[1:] if line.split("\t")[1] == "original_DE"}

    # Process B*_DE.out
    with open(de_file, "r") as f:
        de_lines = f.readlines()
    de_genes = {line.split("\t")[0] for line in de_lines[1:]}
    pfam_domains = {line.split("\t")[8] for line in de_lines[1:]}

    # Process B*_GO.out
    with open(go_file, "r") as f:
        go_lines = f.readlines()
    go_genes = {line.split("\t")[0] for line in go_lines[1:]}
    go_terms = {line.split("\t")[2] for line in go_lines[1:]}

    return {
        "Total Annotated Genes": len(anno_genes),
        "Pannzer Annotated Genes": len(anno_genes),
        "Genes with Pfam Domains": len(de_genes),
        "Distinct Pfam Domains": len(pfam_domains),
        "Genes with GO terms": len(go_genes),
        "Distinct GO terms": len(go_terms)
    }

def main():
    # Extract genome names from anno files in the directory
    genomes = [os.path.basename(f).split('_anno.out')[0] for f in glob.glob('*_anno.out')]

    results = {}
    for genome in genomes:
        if os.path.exists(f"{genome}_anno.out"):
            results[genome] = process_annotation_files(genome)
        else:
            print(f"Files for genome {genome} not found. Skipping...")

    # Print the results in table format
    headers = ["Genome Name", "Total Annotated Genes", "Pannzer Annotated Genes", "Genes with Pfam Domains", "Distinct Pfam Domains", "Genes with GO terms", "Distinct GO terms"]
    print("\t".join(headers))
    for genome, data in results.items():
        print(f"{genome}\t{data['Total Annotated Genes']}\t{data['Pannzer Annotated Genes']}\t{data['Genes with Pfam Domains']}\t{data['Distinct Pfam Domains']}\t{data['Genes with GO terms']}\t{data['Distinct GO terms']}")

if __name__ == "__main__":
    main()

