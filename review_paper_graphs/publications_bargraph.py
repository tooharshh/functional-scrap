import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def count_publications_per_year(publications_data):
 
    year_counts = Counter([year for _, year in publications_data])
    years = sorted(year_counts.keys())
    counts = [year_counts[year] for year in years]
    return years, counts

def create_publication_bargraph():
    publications_data = [
        ("Rafiei and Adeli", 2017),
        ("Kong et al.", 2019),
        ("van den Ende and Ampuero", 2020),
        ("Hsu and Huang", 2021),
        ("Jozinović et al.", 2021),
        ("Abdatzaher et al.", 2022),
        ("Chakraborty et al.", 2022),
        ("Cofre et al.", 2022),
        ("Khan and Kwon", 2022),
        ("Liao et al.", 2022),
        ("Song et al.", 2022),
        ("Zhang et al.", 2022),
        ("Zhu et al.", 2022),
        ("Hou et al.", 2023),
        ("Lara et al.", 2023),
        ("Banar and Mohammadi", 2024),
        ("F. Li et al.", 2024),
        ("Joshi et al.", 2024),
        ("Khattak et al.", 2024),
        ("Lian et al.", 2024),
        ("Meng et al.", 2024),
        ("Murshed et al.", 2024),
        ("Saad et al.", 2024),
        ("Wibowo et al.", 2024),
        ("Yang et al.", 2024),
        ("Zhu et al.", 2024),
        ("Fayaz et al.", 2025),
        ("Huang et al.", 2025),
        ("Joshi et al.", 2025),
        ("Zheng et al.", 2025),
        ("Zhexebay et al.", 2025)
    ]
    
    
    years, counts = count_publications_per_year(publications_data)
    
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    
    bar_color = '#4A90E2'  # Professional blue shade
    
    
    bars = ax.bar(years, counts, color=bar_color, alpha=0.7, edgecolor='white', linewidth=1.5)
    
    
    ax.set_xlabel('Publication Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('No. of Authors', fontsize=14, fontweight='bold')
    ax.set_title('Annual Publication Trends', fontsize=24, fontweight='bold', pad=20)
    
    
    ax.set_xticks(years)
    ax.set_xticklabels(years, rotation=45, ha='right')
    
    # Add 2018 to x-axis for better spacing
    all_years = list(range(2017, 2026))  # Include all years from 2017 to 2025
    ax.set_xticks(all_years)
    ax.set_xticklabels(all_years, rotation=45, ha='right')
    
    # Add some space between x-axis labels and x-axis title
    ax.xaxis.labelpad = 15
    
    
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    
    
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                str(count), ha='center', va='bottom', fontweight='bold')
    
    
    plt.tight_layout(pad=2.0)
    
    # Save the plot as SVG with reduced padding
    plt.savefig('annual_publication_trends.svg', format='svg', 
                bbox_inches='tight', pad_inches=0.3, dpi=300, facecolor='white')
    print("Bar graph saved as 'annual_publication_trends.svg'")
    
    plt.show()

if __name__ == "__main__":
    create_publication_bargraph()
