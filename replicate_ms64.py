import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Configuraciones de estilo profesional para papers
plt.rcParams.update({
    "text.usetex": False, 
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "axes.labelsize": 12,
    "font.size": 11,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "axes.linewidth": 1.2,
    "lines.linewidth": 1.5,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--"
})

def create_dirs():
    os.makedirs('figures', exist_ok=True)

def load_data():
    # Cargar datos digitizados
    return pd.read_csv('data/digitized_profiles.csv')

def plot_figure_4(df):
    """Réplica de Figura 4: Equilibrio Térmico vs Radiativo"""
    fig, ax1 = plt.subplots(figsize=(6, 8))
    
    # Eje Y en log(Presión) invertido para que 1000 esté abajo
    ax1.plot(df['t_pure_rad_k'], df['pressure_mb'], 'k.-', label='Pure Radiative Equil.')
    ax1.plot(df['t_adj_10_k'], df['pressure_mb'], 'k.--', alpha=0.7, label='Dry Adiabatic Adj. (10°C/km)')
    ax1.plot(df['t_adj_65_k'], df['pressure_mb'], 'k.-.', label='6.5°C/km Adj.')
    
    ax1.set_yscale('log')
    ax1.invert_yaxis()
    ax1.set_yticks([1000, 100, 10, 2.3])
    ax1.get_yaxis().set_major_formatter(plt.ScalarFormatter())
    
    ax1.set_xlabel('Temperature (K)')
    ax1.set_ylabel('Pressure (mb)')
    ax1.set_xlim(180, 340)
    ax1.set_ylim(1000, 2.0)
    
    # Eje altitud aproximada a la derecha
    ax2 = ax1.twinx()
    ax2.set_ylim(0, 42)
    ax2.set_ylabel('Altitude (km)')
    ax2.set_yticks([0, 10, 20, 30, 40])
    
    ax1.legend(loc='lower left', bbox_to_anchor=(0.3, 0.2), frameon=False)
    plt.title('Figure 4: Thermal Equilibrium vs Radiative Equilibrium')
    
    plt.tight_layout()
    plt.savefig('figures/Figure_4_Replication.pdf')
    plt.savefig('figures/Figure_4_Replication.png', dpi=300)
    plt.close()

def plot_figure_5(df):
    """Réplica de Figura 5a y 5b: Absorbedores"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6), sharey=True)
    
    # 5a: H2O
    ax1.plot(df['h2o_mix_ratio_35N'], df['pressure_mb'], 'k.-')
    ax1.set_xscale('log')
    ax1.set_xlim(1e-6, 1e-1)
    ax1.set_xlabel('Mixing ratio of Water Vapor (g/g)')
    ax1.set_ylabel('Pressure (mb)')
    ax1.set_yscale('log')
    ax1.invert_yaxis()
    ax1.set_yticks([1000, 100, 10, 2.3])
    ax1.get_yaxis().set_major_formatter(plt.ScalarFormatter())
    ax1.set_title('Fig 5a: $H_2O$ Profile (35°N, April)')
    
    # 5b: O3
    ax2.plot(df['o3_amount_35N'], df['pressure_mb'], 'k.-')
    ax2.set_xlim(0, 18)
    ax2.set_xlabel('Ozone Amount ($10^{-3}$ cm/km)')
    ax2.set_title('Fig 5b: Ozone Profile (35°N, April)')
    
    plt.tight_layout()
    plt.savefig('figures/Figure_5_Replication.pdf')
    plt.savefig('figures/Figure_5_Replication.png', dpi=300)
    plt.close()

def plot_figure_6a(df):
    """Réplica de Figura 6a: Impacto de absorbedores individuales"""
    fig, ax1 = plt.subplots(figsize=(6, 8))
    
    ax1.plot(df['t_rad_h2o'], df['pressure_mb'], 'k-', label='$H_2O$')
    ax1.plot(df['t_rad_h2o_co2'], df['pressure_mb'], 'k--', label='$H_2O + CO_2$')
    ax1.plot(df['t_rad_h2o_co2_o3'], df['pressure_mb'], 'k.-', label='$H_2O + CO_2 + O_3$')
    
    ax1.set_yscale('log')
    ax1.invert_yaxis()
    ax1.set_yticks([1000, 100, 10, 2.3])
    ax1.get_yaxis().set_major_formatter(plt.ScalarFormatter())
    
    ax1.set_xlabel('Temperature (K)')
    ax1.set_ylabel('Pressure (mb)')
    ax1.set_xlim(100, 340)
    
    ax1.legend(loc='center right', frameon=False)
    plt.title('Figure 6a: Pure Radiative Equil. for Various Absorbers')
    
    plt.tight_layout()
    plt.savefig('figures/Figure_6a_Replication.pdf')
    plt.savefig('figures/Figure_6a_Replication.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    create_dirs()
    df = load_data()
    plot_figure_4(df)
    plot_figure_5(df)
    plot_figure_6a(df)
    print("Figuras generadas exitosamente en el directorio /figures")