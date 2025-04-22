import sys, os, pandas as pd, numpy as np, matplotlib.pyplot as plt

def main(csv_path, out_dir='figures'):
    os.makedirs(out_dir, exist_ok=True)
    df = pd.read_csv(csv_path)

    plt.figure()
    plt.hist(df['SOC (%)'], bins=30)
    plt.xlabel("SOC (%)"); plt.ylabel("Frequency"); plt.title("Distribution of State of Charge")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir,'fig_soc_hist.png'), dpi=300); plt.close()

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(6,5))
    plt.imshow(corr, interpolation='nearest'); plt.colorbar()
    plt.xticks(range(len(numeric_cols)), numeric_cols, rotation=90)
    plt.yticks(range(len(numeric_cols)), numeric_cols)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir,'fig_corr_heat.png'), dpi=300); plt.close()

    plt.figure()
    plt.scatter(df['Charging Cycles'], df['Degradation Rate (%)'])
    plt.xlabel("Charging Cycles"); plt.ylabel("Degradation Rate (%)")
    plt.title("Charging Cycles vs Degradation Rate")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir,'fig_cycles_deg.png'), dpi=300); plt.close()

    modes = df['Charging Mode'].unique()
    data_plot = [df[df['Charging Mode']==m]['Degradation Rate (%)'] for m in modes]
    plt.figure()
    plt.boxplot(data_plot, labels=modes)
    plt.xlabel("Charging Mode"); plt.ylabel("Degradation Rate (%)")
    plt.title("Degradation Rate by Charging Mode")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir,'fig_box_deg_mode.png'), dpi=300); plt.close()

    plt.figure()
    plt.scatter(df['Charging Duration (min)'], df['Battery Temp (°C)'])
    plt.xlabel("Charging Duration (min)"); plt.ylabel("Battery Temp (°C)")
    plt.title("Charging Duration vs Battery Temperature")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir,'fig_duration_temp.png'), dpi=300); plt.close()

    plt.figure()
    plt.scatter(df['Ambient Temp (°C)'], df['Efficiency (%)'])
    plt.xlabel("Ambient Temp (°C)"); plt.ylabel("Efficiency (%)")
    plt.title("Ambient Temp vs Charging Efficiency")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir,'fig_ambient_eff.png'), dpi=300); plt.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_figures.py <path_to_csv> [output_dir]")
        sys.exit(1)
    csv_path = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else 'figures'
    main(csv_path, out_dir)