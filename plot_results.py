import matplotlib.pyplot as plt


def plot_log_results(df, title, y_label, save_path):
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df["Actual"], label="Actual", alpha=0.8)
    plt.plot(df.index, df["Predicted"], label="Predicted", linestyle='--')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(visible=True, alpha=0.3, linestyle='--', axis='y')
    plt.grid(visible=False, alpha=0.0, axis='x')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    
def plot_results(df, title, y_label, save_path):
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df["Actual_days"], label="Actual", alpha=0.8)
    plt.plot(df.index, df["Predicted_days"], label="Predicted", linestyle='--')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(visible=True, alpha=0.3, linestyle='--', axis='y')
    plt.grid(visible=False, alpha=0.0, axis='x')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()