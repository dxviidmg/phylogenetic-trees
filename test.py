from Bio import Phylo
import matplotlib.pyplot as plt


nhx_file = "data/birds_phylogeny.nhx"

# Parse the .nhx file
trees = Phylo.parse(nhx_file, "newick")

# Iterate over the trees
for tree in trees:
    # Access the tree structure and other information
    print(tree)
    output_image = "image.png"

    # Draw and save the tree as an image
#    Phylo.draw(tree, show_confidence=False, do_show=False, branch_labels=lambda c: c.branch_length)

#    plt.axis('off')  # Remove axes and labels
#    plt.savefig(output_image, dpi=300)

#    break